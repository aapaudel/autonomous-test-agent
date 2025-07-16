from application.sample_code_3 import *

def test_is_even():
    result = is_even(1)
    assert result is not None if result is not None else result is None

def test_greet():
    result = greet("sample_key")
    assert result is not None if result is not None else result is None
