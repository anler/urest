# -*- coding: utf-8 -*-
from . import serializers


class Resource:
    __serializers__ = (serializers.Json,)

    def __init__(self, request):
        self.request = request

    @classmethod
    def list(self, parent=None):
        pass

    @classmethod
    def retrieve(self, id, parent=None):
        pass

    @classmethod
    def create(self, data, id=None, parent=None):
        pass

    def update(self, data):
        pass

    def partial_update(self, data):
        pass

    def delete(self):
        pass
