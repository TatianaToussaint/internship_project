# Created by User at 12/20/2023
Feature:User can open Subscription & payments page

  Scenario: User can open Subscription & payments page
    Given Open the main page
    When Log in to the page
    Then Click on settings option
    And Click on Subscription & payments option
    Then Verify the right page opens
    Then Verify title “Subscription & payments” is visible
    Then Verify “back” and “upgrade plan” buttons are available
