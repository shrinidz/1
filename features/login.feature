Feature: Successful Login

Scenario: 1 Successful Login
    Given I am on the Demo Login Page
    When I fill the account information for account StandardUser into the Username field and the Password field
    And I click the Login Button
    Then I am redirected to the Demo Main Page
    And I verify the App Logo exists



Scenario: Failed Login with LockedOutUser
    Given I am on the Demo Login Page
    When I fill the account information for account LockedOutUser into the Username field and the Password field
    And I click the Login Button
    Then I verify the Error Message contains the text "Sorry, this user has been banned."
