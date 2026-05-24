@positive
Feature: Positive Test Cases
  Positive test scenarios for BestBuy BDD automation

  Scenario: TC01 — Open BestBuy website
    Given I open the BestBuy website
    Then the BestBuy website should load successfully

  Scenario: TC02 — Select United States
    Given I open the BestBuy website
    When I select United States
    Then the United States homepage should load

  Scenario: TC03 — Click Top Deals
    Given I open the BestBuy website
    When I select United States
    And I click Top Deals
    Then the Top Deals page should open

  Scenario: TC04 — Click Headphones category
    Given I open the BestBuy website
    When I select United States
    And I click Top Deals
    And I click the Headphones category
    Then the Headphones page should open

  Scenario: TC05 — Select random headphone category
    Given I open the BestBuy website
    When I select United States
    And I click Top Deals
    And I click the Headphones category
    And I select a random headphone category from Excel
    Then the headphone category page should open

  Scenario: TC06 — Add products to cart
    Given I open the BestBuy website
    When I select United States
    And I click Top Deals
    And I click the Headphones category
    And I select a random headphone category from Excel
    And I add products to the cart
    Then at least one product should be added to the cart

  Scenario: TC07 — Open cart page
    Given I open the BestBuy website
    When I select United States
    And I click Top Deals
    And I click the Headphones category
    And I select a random headphone category from Excel
    And I add products to the cart
    And I open the cart page
    Then the cart page should be displayed successfully