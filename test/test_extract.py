# test_example.py
import pytest
from src.extract import function_to_test

def test_lambda_handler():
    expected_value="dummy"
    assert function_to_test() == expected_value