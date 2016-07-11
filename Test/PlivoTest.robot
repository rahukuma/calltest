*** Settings ***
Documentation    This suite created endpoint in setup.
...              Then makes an outbout call
...              Then makes conference call
...              Then play music in the call
...              After getting the live call details it disconnects the call
...              Finally deletes the created endpoint in teardown
...              Also answer url and music url are taken from plivo package
...              At present only mandatory params are used to make calls.This could be extended to other params.

Library     ..${/}Library${/}plivo_call.py
Variables   ..${/}Resources${/}rahul_account.py

Suite Setup      Create Endpoint       rahulk     RahulPlivo11        RahulPlivo      ${appid.demo_conference}
Suite Teardown   Delete endpoint

*** Test Cases ***
Make outbound call and conference call
    [Documentation]     The following two cases make an outbound call and conference call
     ...
    Make an outbound call     <fromNo>      <toNo>      http://morning-ocean-4669.herokuapp.com/speech/
    Place in a conference call      <fromNo>      <toNos>       https://morning-ocean-4669.herokuapp.com/response/conference/

Play music and verify the calls
     [Documentation]    Keyword 'Get live call details' is taken directly from Library file plivo_call.py
     Play Music in the live call     http://s3.amazonaws.com/plivocloud/music.mp3
     Get live call details

Disconnect the above live call
    [Documentation]    Keyword is taken directly from Library file plivo_call.py
    ...                Disconnects the call initiated above
     Disconnect live call

*** Keywords ***
Make an outbound call
    [Arguments]     ${from}     ${to}     ${answer_url}
    Make a call     ${from}     ${to}     ${answer_url}
Place in a conference call
    [Documentation]     Only mandatory params are supplied at present.Coulc be extended further
    ...                 Also answer method is hardcoded as "Get".Can be passed through arguments
    [Arguments]      ${from}     ${to}       ${answer_url}
    Make conference call      ${from}     ${to}       ${answer_url}

Play Music in the live call
    [Arguments]     ${music_urls}
    Play music      ${music_urls}
