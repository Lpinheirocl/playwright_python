Feature: Site 1 testing

  Scenario Outline: Visit a page and check the title
    Given I open the page "<url>"
    Then I should see the title "<expected_title>"

  Examples:
    | url                       | expected_title       |
    | https://site1.example.com | Site 1 Title       |
