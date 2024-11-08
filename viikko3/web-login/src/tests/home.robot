*** Settings ***
Resource            resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Reset Application And Go To Starting Page


*** Test Cases ***
Click Login Link
    Click Link    Login
    Login Page Should Be Open

Click Register Link
    Click Link    Register new user
    Register Page Should Be Open


*** Keywords ***
Go To Starting Page
    Go To    ${HOME_URL}

Reset Application And Go To Starting Page
    Reset Application
    Go To Starting Page

Register Page Should Be Open
    Title Should Be    Register
    Page Should Contain    Register
