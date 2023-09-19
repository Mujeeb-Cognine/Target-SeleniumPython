# Any pytest file should start with test_ or end with _test pytest method name should start with test Any code should
# be wrapped in method only Method name should have sense -k Stands for method names execution , -s login in output,
# -v stands for more info metadata You can run specific file py.test <filename> You can mark (tag) test
# @pytest.mark.smoke and then run with -m You can skip tests with @pytest.mark.skip You can run the test without
# loggin in document if fail with @pytest.mark.xfail Fixtures are used as setup and tear down methods for test cases-
# conftest file to generalize fixture and make it available to all test cases
# datatdriven and parameterization can be done with return statement in tuple format
# When you define fixture scope to class only, it will run once before class is initiated and at the end
# To get reports during command line run use py.test --html=report.html



import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])
