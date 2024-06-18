Feature: Compare CSV files

  Scenario: CSV files should be identical
    Given I have two CSV files "data/identical1.csv" and "data/identical2.csv"
    When I compare the CSV files
    Then the CSV files should be identical

  Scenario: CSV files should have differences
    Given I have two CSV files "data/different1.csv" and "data/different2.csv"
    When I compare the CSV files
    Then the CSV files should have differences
