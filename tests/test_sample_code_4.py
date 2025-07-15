from application.sample_code_4 import *


def test_deposit():
    obj = BankAccount(1, 1)
    result = obj.deposit(1)
    assert result


def test_withdraw():
    obj = BankAccount(1, 1)
    result = obj.withdraw(1)
    assert isinstance(result, int) # Replace expected_value with the actual expected value


def test_get_balance():
    obj = BankAccount(1, 1)
    result = obj.get_balance()
    assert result

