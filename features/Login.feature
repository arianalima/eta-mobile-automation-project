Feature: Login

  Background: Setup
    Given I access the app
    When  I click on login page

  Scenario: Verify login fields
    Then   I should be able to see all fields displayed

  Scenario: Verify that invalid users aren't logged in and an error message is displayed
    When I insert a invalid user
    And  I insert a valid password
    And  I select the login button
    Then I should see a ERROR_MESSAGE_INVALID_USER error message

  Scenario: Verify that when a short password is used in login an error message is displayed
    When I insert a valid user
    And  I insert a short password
    And  I select the login button
    Then I should see a ERROR_MESSAGE_SHORT_PASSWORD error message

  Scenario: Verify that when a login is made with empty fields an error message is displayed
    When I select the login button
    Then I should see a ERROR_MESSAGE_EMPTY_LOGIN error message

  Scenario: Verify that when the cancel button is selected the login popup is closed
    When I select the cancel button
    Then I should not see the login popup anymore

  Scenario: Verify that when a successful login is made a logout can be made
    Given I insert a valid user
    And   I insert a valid password
    And   I select the login button
    Then  I should see that valid user is logged
    When  I select the logout button
    Then  I am logged out from the application

  Scenario: Verify that when logging in the app without network connection an error message is displayed
    Given I have no network connection
    And   I insert a valid user
    And   I insert a valid password
    When  I select the login button
    Then  I should see a ERROR_MESSAGE_NO_NETWORK error message



#  Inserir informações de credenciais, receber uma chamada, aceitá-la, finalizá-la e verificar que as informações inseridas nos campos de credenciais foram mantidas.