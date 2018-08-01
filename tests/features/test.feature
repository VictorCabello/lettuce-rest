Feature: Steps Implementation
    In order to make easy the Rest API tesing
    As a wise develper
    I want j collection of predefined steps that help with that

    Scenario: Add a person with name and phone number
        Given I set the property "staging_url" of the world to "fake_url"
        When I set base URL to "world.staging_url"
        Then the property "base_url" of the world should be "fake_url"

    Scenario: Add a person with name and phone number
        Given I set base URL to "http://fake.io"
        When I add path "appended" to base URL"
        Then the property "base_url" of the world should be "http://fake.io/appended"
