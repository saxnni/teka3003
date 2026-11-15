*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Create User  kalle  kalle123
    Input Login Command

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input Register Command
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Register Command
    Input Credentials  k  kalle123
    Output Should Contain  Username must be at least 3 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Register Command
    Input Credentials  !!!!  kalle123
    Output Should Contain  Username must contain only letters

Register With Valid Username And Too Short Password
    Input Register Command
    Input Credentials  kalle  1234
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Register Command
    Input Credentials  kalle  kalleonparas
    Output Should Contain  Password must contain at least one number or special character

*** Keywords ***
