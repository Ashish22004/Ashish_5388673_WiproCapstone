@negative
Feature: Negative Test Cases
  Negative test scenarios for BestBuy BDD automation

  Scenario: NC01 — Wrong website URL
    Given I open a wrong misspelled website URL
    Then bestbuy.com should not be in the URL

  Scenario: NC02 — Wrong country selected
    Given I open the BestBuy website
    When I select Canada instead of United States
    Then united-states should not be in the URL

  Scenario: NC03 — Wrong section clicked
    Given I open the BestBuy website
    When I select United States
    And I click Deal of the Day instead of Top Deals
    Then top-deals should not be in the URL