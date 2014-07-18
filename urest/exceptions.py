# -*- coding: utf-8 -*-


class MissingSerializer(Exception):
    "Exception raised to indicate that a serializer couldn't be found to fullfill the request"


class MissingMethod(Exception):
    "Exception raised to indicate that the resource can't handle the request method"


class RaisedResponse(Exception):
    "Wrapper around a response object to allow it to be raised and catched"

    def __init__(self, response):
        self.response = response

    def __str__(self):
        return "Raised response ({})".format(self.response)
