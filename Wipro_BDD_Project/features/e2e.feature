@e2e
Feature: E2E Complete Flow
  Complete end-to-end BestBuy shopping flow in one browser session

  Scenario: Complete positive flow — open BestBuy to cart
    Given I open the BestBuy website
    When I select United States
    And I click Top Deals
    And I click the Headphones category
    And I select a random headphone category from Excel
    And I add products to the cart
    And I open the cart page
    Then the cart page should be displayed successfully