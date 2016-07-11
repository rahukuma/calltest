import json

class EndpointToJson(object):
    name = ''
    id = ''
    email = ''
    phone = ''
    address = ''

    def __init__(self, username, password, alias, app_id=None, message=None, endpoint_id=None):
        self.username = username
        self.password = password
        self.alias = alias
        self.app_id = app_id
        self.message = message
        self.endpoint_id = endpoint_id

    def to_json(self, endpoint):
        message = json.dumps(endpoint.__dict__)
        return message


class CallToJson(object):
    def __init__(self, from_no, to_no, answer_url):
        self.from_no = from_no
        self.to_no = to_no
        self.answer_url = answer_url

    def to_json(self):
        data = {}
        data['from'] = self.from_no
        data['to'] = self.to_no
        data['answer_url'] = self.answer_url
        data['answer_method'] = 'GET'

        return json.dumps(data)


class PlayToJson(object):
    def __init__(self, urls, lenght=None, legs=None, loop=None, mix=None):
        self.urls = urls
        self.length = lenght
        self.legs = legs
        self.loop = loop
        self.mix = mix

    def to_json(self):
        data = {}
        data['urls'] = self.urls
        data['lenght'] = self.length
        data['legs'] = self.legs
        data['loop'] = self.loop
        data['mix'] = self.mix

        return json.dumps(data)
