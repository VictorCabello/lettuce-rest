Feature: Steps Implementation
    In order to make easy the Rest API tesing
    As a wise develper
    I want j collection of predefined steps that help with that

    Scenario: Set static value to base_url
        Given I set the property "staging_url" of the world to "fake_url"
        When I set base URL to "world.staging_url"
        Then the property "base_url" of the world should be "fake_url"

    Scenario: Set a value from other variable to base_url
        Given I set base URL to "http://fake.io"
        When I add path "appended" to base URL"
        Then the property "base_url" of the world should be "http://fake.io/appended"

    Scenario: Do not verify ssl
        Given I do not want to verify SSL certs
        Then the property "verify_ssl" of the world should be "False"

    Scenario: Verify ssl
        Given I want to verify SSL certs
        Then the property "verify_ssl" of the world should be "True"

    Scenario: Add static header
        Given I set "test_name" header to "test_value"
        Then the property "headers" of the world should be "{'test_name': 'test_value'}"

    Scenario: Add dynimic header
        Given I set the property "staging_url" of the world to "fake_url"
        When I set "test_name" header to "world.staging_url"
        Then the property "headers" of the world should be "{'test_name': u'fake_url'}"

    Scenario: delete header
        Given I set "test_name" header to "staging_url"
        And I set "test_name_2" header to "staging_url"
        When I clear "test_name" header
        Then the property "headers" of the world should be "{'test_name_2': 'staging_url'}"

    Scenario: delete all headers
        Given I set "test_name" header to "staging_url"
        And I set "test_name_2" header to "staging_url"
        When I clear all headers
        Then the property "headers" of the world should be "{}"
