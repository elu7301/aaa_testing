import pytest
from unittest.mock import patch
import urllib.request
import json


API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock
        и извлекает из поля 'currentDateTime' год

    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)


def test_year_with_YMD_format():
    with patch('json.load') as mock_json_load:
        with patch('urllib.request.urlopen') as mock_urlopen:
            mock_response = {
                'currentDateTime': '2023-11-06'
            }
            mock_json_load.return_value = mock_response
            mock_urlopen.return_value.__enter__.return_value = 'dummy_response'

            year = what_is_year_now()

            assert year == 2023

            mock_urlopen.assert_called_once_with(API_URL)
            mock_json_load.assert_called_once_with('dummy_response')


def test_year_with_DMY_format():
    with patch('json.load') as mock_json_load:
        with patch('urllib.request.urlopen') as mock_urlopen:
            mock_response = {
                'currentDateTime': '06.11.2023'
            }
            mock_json_load.return_value = mock_response
            mock_urlopen.return_value.__enter__.return_value = 'dummy_response'

            year = what_is_year_now()

            assert year == 2023

            mock_urlopen.assert_called_once_with(API_URL)
            mock_json_load.assert_called_once_with('dummy_response')


def test_invalid_format():
    with patch('json.load') as mock_json_load:
        with patch('urllib.request.urlopen') as mock_urlopen:
            mock_response = {
                'currentDateTime': '2023/11/06'
            }
            mock_json_load.return_value = mock_response
            mock_urlopen.return_value.__enter__.return_value = 'dummy_response'

            with pytest.raises(ValueError):
                what_is_year_now()

            mock_urlopen.assert_called_once_with(API_URL)
            mock_json_load.assert_called_once_with('dummy_response')