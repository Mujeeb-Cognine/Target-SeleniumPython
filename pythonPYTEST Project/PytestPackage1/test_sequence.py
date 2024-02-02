import pytest
from PytestPackage1.test_Login import TestCustomerLogin  # Import the login test class
from PytestPackage1.test_logout import TestCustomerLogout  # Import the logout test class


# Define a sequence of test cases
class TestLoginAndLogoutSequence:
    @pytest.mark.run(order=1)  # Use a custom marker to specify the order
    def test_login_sequence(self):
        login_test = TestCustomerLogin()
        login_test.setup_method()
        # login_test.test_customer_login()
        # login_test.teardown_method()

    @pytest.mark.run(order=2)  # Use a custom marker to specify the order
    def test_logout_sequence(self):
        logout_test = TestCustomerLogout()
        logout_test.setup_method()
        logout_test.test_customer_logout()
        logout_test.teardown_method()


# Run the sequence of test cases
if __name__ == "__main__":
    pytest.main()
