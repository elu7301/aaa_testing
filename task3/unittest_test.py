import unittest
from typing import List, Tuple


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in
                        bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


class FitTransformUnitTest(unittest.TestCase):
    def test_fit_transform(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        expected_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, expected_transformed_cities)

    def test_fit_transform_type_error(self):
        with self.assertRaises(TypeError) as context:
            fit_transform()
        self.assertEqual(str(context.exception),
                         'expected at least 1 arguments, got 0')

    def test_fit_transform_with_additional_category(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        additional_category = 'Paris'
        transformed_cities = fit_transform(cities)
        for val, transformed_val in transformed_cities:
            self.assertNotIn(additional_category, val)

    def test_fit_transform_args(self):
        transformed_letters = fit_transform('a', 'b', 'c', 'a')
        expected_transformed_letters = [
            ('a', [0, 0, 1]),
            ('b', [0, 1, 0]),
            ('c', [1, 0, 0]),
            ('a', [0, 0, 1])
        ]
        self.assertEqual(transformed_letters, expected_transformed_letters)
