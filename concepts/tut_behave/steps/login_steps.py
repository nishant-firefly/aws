"""
Parameterized Steps: The step @when('the user enters "{username}" and "{password}"') is parameterized to handle different inputs.

Context Object: The context object is shared across steps in a scenario, allowing us to pass data like login status or credentials between steps.

Assertions: Each @then step contains assertions to validate the test outcomes, using AssertionError to fail tests when necessary.
"""
from behave import given, when, then

# In-memory simulation of a user database (for demo purposes)
USER_DB = {
    "validuser": "validpass"
}

@given('the user is on the login page')
def step_user_on_login_page(context):
    """
    This step simulates navigating to the login page.
    The context object can store state shared across steps.
    """
    context.page = "login_page"
    print("User is on the login page")

@when('the user enters valid credentials')
def step_user_enters_valid_credentials(context):
    """
    Simulates entering valid credentials and stores the result in the context.
    """
    context.credentials_valid = True
    print("User enters valid credentials")

@when('the user enters invalid credentials')
def step_user_enters_invalid_credentials(context):
    """
    Simulates entering invalid credentials and stores the result in the context.
    """
    context.credentials_valid = False
    print("User enters invalid credentials")

@when('the user enters "{username}" and "{password}"')
def step_user_enters_credentials(context, username, password):
    """
    This is a parameterized step that takes a username and password as input.
    It checks the credentials against the in-memory user database.
    """
    if USER_DB.get(username) == password:
        context.credentials_valid = True
    else:
        context.credentials_valid = False
    print(f"User enters username: {username}, password: {password}")

@then('the user should be redirected to the homepage')
def step_user_redirected_to_homepage(context):
    """
    Asserts whether the user is redirected to the homepage based on the credentials.
    """
    if context.credentials_valid:
        print("User is redirected to the homepage")
    else:
        raise AssertionError("User was not redirected to the homepage")

@then('the user should see an error message')
def step_user_sees_error_message(context):
    """
    Asserts that the user sees an error message based on invalid credentials.
    """
    if not context.credentials_valid:
        print("User sees an error message")
    else:
        raise AssertionError("User did not see an error message")
