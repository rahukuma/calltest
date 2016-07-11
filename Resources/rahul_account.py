class AuthId(object):
    auth_id = 'MANZIXYTUYM2EYYJK3MT'
    auth_token = 'NTNmN2RkMjBiMzY4YjMyMzViYThlNmE4ZmIyYWRh'

class ApplicationId(object):
    demo_speak = '20606864222201741'
    demo_conference = '20611716947155740'
    demo_play = '20610745530655153'
    call_forward = '20609761279192238'
    direct_dial = '20608143519341859'

class ApiParam(object):
    api_basepath = 'https://api.plivo.com/v1/Account/%s' % AuthId.auth_id + '/'

authid = AuthId()
appid = ApplicationId()
apiparam = ApiParam()