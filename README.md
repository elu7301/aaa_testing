## **Task 1**
python -m doctest task1/encode_test.py  
python -m doctest -v task1/encode_test.py  
python -m doctest -o NORMALIZE_WHITESPACE task1/encode_test.py  
python -m doctest -o NORMALIZE_WHITESPACE -v task1/encode_test.py
## **Task 2**
python -m pytest task2/decode_test.py  
python -m pytest -v task2/decode_test.py
## **Task 3**
python -m unittest task3/unittest_test.py  
python -m unittest -v task3/unittest_test.py
## **Task 4**
python -m pytest task4/pytest_test.py  
python -m pytest -v task4/pytest_test.py
## **Task 5**
cd task5
python -m pytest year_test.py
python -m pytest -v year_test.py  
python -m pytest year_test.py --cov . --cov-report html  
python -m pytest -v year_test.py --cov . --cov-report html