# Created by richard.pinedo at 3/12/24
Feature: # Enter feature name here
  # Enter feature description here

  @Regression
  Scenario: Create User
    Given launch on page home
    And the user enters "Admin" in Nombre field and "admin_password" in password field
    And the user clicks the "Acceder" button
    And the user clicks in Usuarios menu
    And the user clicks in Añadir nuevo usuario
    And the user fill in "test" in Nombre de usuario field and "test@gmail.com" in Correo electrónico field
    When the user clicks in Añadir nuevo usuario button
    Then the user can see the new user create "test"

  @Regression
  Scenario: Delete User
    Given launch on page home
    And the user enters "Admin" in Nombre field and "admin_password" in password field
    And the user clicks the "Acceder" button
    And the user clicks in Usuarios menu
    And the user clicks in Todos los usuarios menu
    And the user clicks in borrar "test" user
    When the user clicks in confirmar borrado button
    Then the user can't see "test" user