Feature: Order a Product

Scenario: Order a product and complete checkout
    Given I am on the inventory page
    When user sorts products from low price to high price
    And user adds lowest priced product
    And user clicks on cart
    And user clicks on checkout
    And user enters first name John
    And user enters last name Doe




    And user enters zip code 123
    And user clicks Continue button
    Then I verify in Checkout overview page if the total amount for the added item is $8.63
    When user clicks Finish button
    Then Thank You header is shown in Checkout Complete page

