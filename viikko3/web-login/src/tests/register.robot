*** Settings ***
Resource            resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Reset Application Create User And Go To Register Page
# käyttäjätunnus a-z väh 3 merkkiä
# salasana väh 8 merkkiä ja ei saa olla pelkästään kirjaimia


*** Test Cases ***
Register With Valid Username And Password
    Set Username    tomppa
    Set Password    tomppa123
    Set Password Confirmation    tomppa123
    Click Register Button
    Page Should Contain    text=Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username    t
    Set Password    tomppa123
    Set Password Confirmation    tomppa123
    Click Register Button
    Page Should Contain    text=Username is too short, must be at least 3 chars

Register With Valid Username And Too Short Password
    Set Username    tomppa
    Set Password    t1
    Set Password Confirmation    t1
    Click Register Button
    Page Should Contain    text=Password is too short, it must be at least 8 chars

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username    tomppa
    Set Password    tomppaboiboi
    Set Password Confirmation    tomppaboiboi
    Click Register Button
    Page Should Contain    text=Password must contain other chars than A-Z

Register With Nonmatching Password And Password Confirmation
    Set Username    tomppa
    Set Password    tomppa123
    Set Password Confirmation    tomppa1233
    Click Register Button
    Page Should Contain    text=Passwords do not match

Register With Username That Is Already In Use
    Set Username    kalle
    Set Password    kalle123
    Set Password Confirmation    kalle123
    Click Register Button
    Page Should Contain    User with username kalle already exists


*** Keywords ***
Set Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Set Password
    [Arguments]    ${password}
    Input Password    password    ${password}

Set Password Confirmation
    [Arguments]    ${password}
    Input Password    password_confirmation    ${password}

Click Register Button
    Click Button    locator=Register

Reset Application Create User And Go To Register Page
    Reset Application
    Create User    kalle    kalle123
    Go To Register Page
