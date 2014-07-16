# -*- coding: utf-8 -*-
from collections import namedtuple

from . import responses
from . import serializers
from . import middlewares
from .dispatch import dispatch

MIDDLEWARES = (middlewares.ETag, middlewares.MethodOverride)
ViewMetadata = namedtuple("ViewMetadata", "view url args kwargs")


def as_view(view_class):
    """Use a resource class as a function-based django view."""
    def view(request, *args, **kwargs):
        return dispatch(view_class(), request, *args, **kwargs)
    for middleware in MIDDLEWARES:
        view = middleware(view)
    return view


class View:
    resource = None
    parent_resource = None

    def _get_resource(self, resource_class, request):
        resource = resource_class(request)
        for proxy in self.resource_proxies:
            resource = proxy(resource)
        return resource

    def get_resource(self, request):
        return self._get_resource(self.resource)

    def get_parent_resource(self, request):
        parent = self.parent_resource
        if parent:
            return self._get_resource(parent)


class Collection(View):

    def get(self, request, *args, **kwargs):
        resource = self.get_resource(request).list(self.get_parent_resource(request))
        return resource.list()

    def post(self, *args, **kwargs):
        pass


class Document(View):
    def get(self, *args, **kwargs):
        pass

    def put(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass


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
