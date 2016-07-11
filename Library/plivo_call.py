import json

import requests
from robot.utils.asserts import assert_equal, fail

from Library.api_list import PlivoApi
from Library.utils.message_dto import EndpointToJson, CallToJson, PlayToJson
from Resources.rahul_account import ApiParam, AuthId

_API_BASEPATH = ApiParam.api_basepath


class plivo_call(object):
    def create_endpoint(self, user, password, alias, application_id):
        msg = EndpointToJson(user, password, alias, application_id)
        headers = {'Content-Type': 'application/json'}

        response = requests.post(_API_BASEPATH + PlivoApi.ENDPOINT, data=msg.to_json(msg),
                                 headers=headers, auth=(AuthId.auth_id, AuthId.auth_token))
        content = str(response.content, encoding='utf-8')
        assert_equal(response.status_code, 201, msg='Api response fails with message ' + content)
        res_msg = {}
        try:
            res_msg = json.loads(content)
        except json.JSONDecodeError:
            fail("Endpoint api response is not JSON.")
        assert_equal(res_msg['message'], 'created')
        global end_id
        end_id = res_msg['endpoint_id']

        return end_id

    def delete_endpoint(self):
        api = _API_BASEPATH + PlivoApi.ENDPOINT + end_id + '/'

        response = requests.delete(api, auth=(AuthId.auth_id, AuthId.auth_token))
        assert_equal(response.status_code, 204)

    def make_a_call(self, fromNo, toNo, answer_url):
        msg = CallToJson(fromNo, toNo, answer_url)
        headers = {'Content-Type': 'application/json'}

        response = requests.post(_API_BASEPATH + PlivoApi.CALL, data=msg.to_json(),
                                 headers=headers, auth=(AuthId.auth_id, AuthId.auth_token))
        content = str(response.content, encoding='utf-8')
        assert_equal(response.status_code, 201, msg='Api response fails with message ' + content)
        try:
            res_msg = json.loads(content)
        except json.JSONDecodeError:
            fail("Make call api response is not JSON.")

        global call_uuid
        call_uuid = self.get_live_call_id()

    def make_conference_call(self, fromNo, toNo, answer_url):
        if ',' in toNo:
            for no in toNo.split(','):
                msg = CallToJson(fromNo, no, answer_url)
                print("JSON", msg.to_json())
                headers = {'Content-Type': 'application/json'}
                response = requests.post(_API_BASEPATH + PlivoApi.CALL, data=msg.to_json(),
                                         headers=headers, auth=(AuthId.auth_id, AuthId.auth_token))
                content = str(response.content, encoding='utf-8')
                try:
                    res_msg = json.loads(content)
                except json.JSONDecodeError:
                    fail("Conference api response is not JSON.")
                print("RESPONSE IS : ", response.status_code, "   ", response.content, "   ")
                assert_equal(response.status_code, 201, msg='Api response fails with message ' + content)

    def play_music(self, url):
        data = PlayToJson(url).to_json()
        api = _API_BASEPATH + PlivoApi.PLAY_MUSIC % call_uuid
        headers = {'Content-Type': 'application/json'}

        response = requests.post(api, data=data, headers=headers, auth=(AuthId.auth_id, AuthId.auth_token))
        content = str(response.content, encoding='utf-8')
        assert_equal(response.status_code, 202, msg='Api response fails with message ' + content)
        try:
            res_msg = json.loads(content)
        except json.JSONDecodeError:
            fail("Play music api response is not JSON.")
        assert_equal(res_msg['message'], 'play started')

    def get_live_call_details(self):
        params = {
            'status': 'live'
        }
        api = _API_BASEPATH + PlivoApi.CALL + call_uuid + "/"

        response = requests.get(api, params=params, auth=(AuthId.auth_id, AuthId.auth_token))
        content = str(response.content, encoding='utf-8')
        assert_equal(response.status_code, 200, msg='Api response fails with message ' + content)
        try:
            res_msg = json.loads(content)
        except json.JSONDecodeError:
            fail_message = "Live call details api response is not JSON" + content
            fail(fail_message)

            # Content verification is pending

    def disconnect_live_call(self):
        api = _API_BASEPATH + PlivoApi.CALL + call_uuid + "/"
        response = requests.delete(api, auth=(AuthId.auth_id, AuthId.auth_token))
        assert_equal(response.status_code, 204)

    def get_live_call_id(self):
        params = {
            'status': 'live'
        }
        api = _API_BASEPATH + PlivoApi.CALL

        uuid_call = ''
        while not uuid_call:
            uuid_call = self.get_call_details(api, params)
        return uuid_call

    def get_call_details(self, api, params={}):
        response = requests.get(api, params=params, auth=(AuthId.auth_id, AuthId.auth_token))
        content = str(response.content, encoding='utf-8')
        assert_equal(response.status_code, 200)
        try:
            res_msg = json.loads(content)
        except json.JSONDecodeError:
            fail_message = "Calls get api response is not JSON" + content
            fail(fail_message)
        print("RES ", res_msg)
        try:
            uuid_call = res_msg['calls'][0]
        except IndexError:
            uuid_call = ''
        except KeyError:
            uuid_call = ''

        return uuid_call


a = plivo_call()
print("API ", _API_BASEPATH + PlivoApi.CALL)
a.get_call_details(_API_BASEPATH + PlivoApi.CALL)
