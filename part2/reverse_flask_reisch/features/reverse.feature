# Created by Matthew B. Reisch at 2/7/2016
Feature: reverse_flask is operational in that users can submit a string via a form and view the word in reverse
  Scenario: successful string reversal
    Given reverse_flask is set up
    When we submit the form with the string "hello"
    Then we should see the output "olleh"

  Scenario: unsuccessful string reversal
    Given reverse_flask is set up
    When we submit the form with the string " "
    Then we should see the alert "This field is required."