"""
Parameterized Steps: The step @when('the user enters "{username}" and "{password}"') is parameterized to handle different inputs.

Context Object: The context object is shared across steps in a scenario, allowing us to pass data like login status or credentials between steps.

Assertions: Each @then step contains assertions to validate the test outcomes, using AssertionError to fail tests when necessary.
"""
# features/steps/login_steps.py

from behave import given, when, then

# Simulating a user database
USER_DB = {
    "validuser": "validpass"
}

# Scenario 1: Using context to share data between steps
@given('the user is on the login page')
def step_user_on_login_page(context):
    context.page = "login_page"  # Store in context
    print("User is on the login page")

@when('the user enters valid credentials')
def step_user_enters_valid_credentials(context):
    context.credentials_valid = True  # Storing result in context
    print("User enters valid credentials")

@then('the user should be redirected to the homepage')
def step_user_redirected_to_homepage(context):
    # Using context to check if login was successful
    assert context.credentials_valid, "User not redirected to the homepage"
    print("User is redirected to the homepage")

# Scenario 2: Not using context, handling data directly in steps
@when('the user enters invalid credentials directly')
def step_user_enters_invalid_credentials_directly(context):
    username = "invaliduser"
    password = "invalidpass"
    # Not storing in context, doing the validation directly
    if USER_DB.get(username) == password:
        credentials_valid = True
    else:
        credentials_valid = False
    
    assert not credentials_valid, "User should not be able to login"
    print(f"User entered invalid credentials: {username}, {password}")


# Scenario Outline: Using both context and direct validation in the same test
@when('the user enters "{username}" and "{password}" using context')
def step_user_enters_credentials_with_context(context, username, password):
    # Store result in context
    if USER_DB.get(username) == password:
        context.credentials_valid = True
    else:
        context.credentials_valid = False
    print(f"User enters credentials: {username}, {password}")

@then('the user should see an error message')
def step_user_sees_error_message(context):
    # Using context to check the login result
    assert not context.credentials_valid, "Expected an error message"
    print("User sees an error message")



