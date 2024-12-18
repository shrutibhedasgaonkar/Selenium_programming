import pytest
#from test_pytest_demo1 import setup


def test_credit_card_other_program():
    print("this is from demo2 file")

'''
@pytest.mark.xfail
def test_credit_card():
    print("ended function with _test")
'''


@pytest.mark.smoke
def test_no_cc_test():
    print("nothing")

"""
def test_check_fixture_2(setup):
    print("I am printing this after fixture is called from Demo2 file")
"""