Feature: Steps Implementation
    In order to make easy the Rest API tesing
    As a wise develper
    I want j collection of predefined steps that help with that

    Scenario: Add a person with name and phone number
        Given I set the property "staging_url" of the world to "fake_url"
        When I set base URL to "world.staging_url"
        Then the property "base_url" of the world should be "fake_url"
