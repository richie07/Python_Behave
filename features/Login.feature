# Created by richard.pinedo at 5/11/24
Feature: Login user
  # Enter feature description here

@Regression
Scenario: Successful login to WordPress
    Given launch on page home
    And the user enters "Admin" in Nombre field and "admin_password" in password field
    When the user clicks the "Acceder" button
    Then the user should see the message "¡Te damos la bienvenida a WordPress!"

@Regression
Scenario: UnSuccessful login to WordPress
    Given launch on page home
    And the user enters "Admin" in Nombre field and "admin" in password field
    When the user clicks the "Acceder" button
    Then the user should see the message error
