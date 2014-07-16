# -*- coding: utf-8 -*-
import json


class Serializer:
    media_type = "*/*"

    def dumps(self):
        pass

    def loads(self, string):
        pass

    def match(self, media_type):
        pass


class Json(Serializer):
    media_type = "application/json"

    def dumps(self, data):
        return json.dumps(data)

    def loads(self, text):
        return json.loads(text)
