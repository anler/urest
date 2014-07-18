# -*- coding: utf-8 -*-
from collections import namedtuple

from . import serializers
from .dispatch import dispatch

ViewMetadata = namedtuple("ViewMetadata", "view url args kwargs")


def as_view(view_class):
    """Use a resource class as a function-based django view."""
    def view(request, *args, **kwargs):
        return dispatch(view_class(), request, *args, **kwargs)
    return view


class View:
    def get_serializers():
        return (serializers.Json,)


class Collection(View):
    def get(self, request, *args, **kwargs):
        return self.resource.list(request)

    def post(self, request, *args, **kwargs):
        return self.resource.create(request)


class Document(View):
    parent = None
    lookup = lambda args, kwargs: None
    parent_lookup = lookup

    def get(self, request, *args, **kwargs):
        return self.resource.retrieve(request, self.lookup(args, kwargs))

    def put(self, request, *args, **kwargs):
        return self.resource.update(request, self.lookup(args, kwargs))

    def patch(self, request, *args, **kwargs):
        return self.resource.update_partial(request, self.lookup(args, kwargs))

    def delete(self, request, *args, **kwargs):
        return self.resource.delete(request, self.lookup(args, kwargs))


class Store(View):
    def get(self, *args, **kwargs):
        pass

    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass


class Controller(View):
    def post(self, *args, **kwargs):
        pass
