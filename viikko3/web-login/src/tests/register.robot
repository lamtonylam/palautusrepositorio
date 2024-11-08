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

Login After Successful Registration
    Register With Username And Password    tomppa    tomppa123
    Logout
    Set Username    tomppa
    Set Password    tomppa123
    Click Login Button
    Page Should Contain    Ohtu Application main page

Login After Failed Registration
    Register With Username And Password    tomppa    t
    Click Link    /login
    Set Username    tomppa
    Set Password    t
    Click Login Button
    Page Should Contain    Invalid username or password
    Title Should Be    Login


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

Click Login Button
    Click Button    Login

Reset Application Create User And Go To Register Page
    Reset Application
    Create User    kalle    kalle123
    Go To Register Page

Logout
    Click Link    ohtu
    Page Should Contain    Ohtu Application main page
    Click Button    Logout
    Page Should Contain    Login

Register With Username And Password
    [Arguments]    ${username}    ${password}
    Set Username    ${username}
    Set Password    ${password}
    Set Password Confirmation    ${password}
    Click Button    locator=Register
