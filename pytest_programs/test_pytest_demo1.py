"""
- Any pytest file should start with 'test_' or end with '_test'
- pytest test method name must start with 'test'
- Any code should be wrapped in method
- method name should have sense in its name
- while executing, -k is for method name, -s is for logs in output, -v is for more data
- We can run specific file with py.test <filename>
- You can mark or tag "smoke" to the test methods add "@pytest.mark.smoke" before that test method and then
  run with "-m smoke"
- You can skip a test methods add "@pytest.mark.skip" before that test method and then run with "-m skip"
- "@pytest.mark.xfail" is used so that the pytest will treat a failure as a "known issue" rather than a full failure,
  allowing you to keep track of such tests without them impacting the overall test suite result.
- Fixtures are used as setup and tear down methods for tes cases
- conftest file is to generalise fixture and make it available to all testcases in that folder
- Datadriven and Parameterisation can be done with return statements on tuple format
- When fixture scope is defined to class only, it will run only once before class initialisation and at the end after
all the class methods are run.
- for creating html report, use "pytest --html=reportname.html" command in the terminal
 """
import pytest


'''
@pytest.mark.smoke
def test_first_pytest_program():
    print("Hello..!")


@pytest.mark.skip
def test_credit_card_program():
    a = 3
    b = 5
    assert a + 2 == b, "The summation is not correct"
    print(f"{a + 2} is the answer")
'''

#
# @pytest.fixture()
# def setup():
#     print("I am printing from the fixtures, I print first")


def test_check_fixtures(setup):
    print("I am printing this after fixture is called from conftest file")


