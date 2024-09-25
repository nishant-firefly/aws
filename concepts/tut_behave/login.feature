# Background: The Given step to navigate to the login page is common for all scenarios, so we use a background to avoid repetition.
# Scenario Outline: The Scenario Outline is used to test multiple sets of invalid credentials without repeating the steps.
# Tags: We use tags like @positive, @negative, and @parameterized to categorize tests and selectively run specific scenarios.

Feature: User login functionality

  # Background: Common setup for all scenarios in this feature
  Background:
    Given the user is on the login page

  # Scenario to test successful login
  @positive
  Scenario: Successful login
    When the user enters valid credentials
    Then the user should be redirected to the homepage

  # Scenario to test unsuccessful login with invalid credentials
  @negative
  Scenario: Unsuccessful login with invalid credentials
    When the user enters invalid credentials
    Then the user should see an error message

  # Scenario Outline: Tests multiple sets of credentials using examples
  @negative @parameterized
  Scenario Outline: Login with multiple invalid credentials
    When the user enters "<username>" and "<password>"
    Then the user should see an error message

    Examples:
      | username    | password    |
      | wronguser   | wrongpass   |
      | testuser    | wrongpass   |
