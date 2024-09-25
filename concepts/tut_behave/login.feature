# features/login.feature

Feature: User login functionality with and without context

  Background:
    Given the user is on the login page

  # Scenario using context to share data across steps
  Scenario: Successful login using context
    When the user enters valid credentials
    Then the user should be redirected to the homepage

  # Scenario using direct assertions without context
  Scenario: Unsuccessful login without context
    When the user enters invalid credentials directly
    Then the user should see an error message

  # Scenario outline using both context and non-context for invalid credentials
  Scenario Outline: Login attempts with different invalid credentials
    When the user enters "<username>" and "<password>" using context
    Then the user should see an error message

    Examples:
      | username    | password    |
      | wronguser   | wrongpass   |
      | testuser    | wrongpass   |

