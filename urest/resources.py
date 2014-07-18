# -*- coding: utf-8 -*-


class Resource:

    def list(self, parent=None):
        pass

    def retrieve(self, id, parent=None):
        pass

    def create(self, data, id=None, parent=None):
        pass

    def update(self, data):
        pass

    def partial_update(self, data):
        pass

    def delete(self):
        pass
