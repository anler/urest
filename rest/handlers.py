# -*- coding: utf-8 -*-
from functools import wraps
from fnmatch import fnmatch

from . import http


def is_mediatype_supported(mediatype, accepted):
    return fnmatch(mediatype, accepted)


def handler(view=None, accept=None, serializer=None, unserializer=None):
    def decorator(view):
        wrapper = wraps(view)
        return wrapper(handler_property(view, accept=accept, serializer=serializer,
                                             unserializer=unserializer))

    return decorator if view is None else decorator(view)


class handler_property(object):

    def __init__(self, get=None, head=None, post=None, put=None, delete=None, accept=None,
                 serializer=None, unserializer=None):
        if accept is None:
            accept = "*/*"
        if serializer is None:
            serializer = lambda data: data
        if unserializer is None:
            unserializer = lambda data: data

        self._get = get
        self._head = head
        self._post = post
        self._put = put
        self._delete = delete
        self._accept = accept
        self._serializer = serializer
        self._unserializer = unserializer


    def __call__(self, *args, **kwargs):
        return self.dispatch(*args, **kwargs)

    def get(self, view):
        self._get = view
        return self

    def post(self, view):
        self._post = view
        return self

    def dispatch(self, request, *args, **kwargs):
        dispatcher = getattr(self, "_{}".format(request.method.lower(), None))
        if dispatcher is None:
            return http.MethodNotAllowed()

        content_type = strip_charset(request.META["CONTENT_TYPE"])
        if not is_mediatype_supported(content_type, self._accept):
            return http.UnsupportedMediaType()

        request.__class__.data = DataDescriptor(self._unserializer)
        request.__class__.get_response = ResponseDescriptor(self._serializer)

        return dispatcher(request, *args, **kwargs)


class DataDescriptor(object):
    def __init__(self, unserializer):
        self.unserializer = unserializer

    def __get__(self, request, request_class=None):
        try:
            data = self.unserializer(request.raw_post_data)
        except ValueError:
            data = {}
        return data


class ResponseDescriptor(object):
    def __init__(self, serializer):
        self.serializer = serializer

    def __get__(self, request, request_class=None):
        return partial(get_response, content_type=request.META["CONTENT_TYPE"],
                       serializer=self.serializer)


def get_response(content=None, content_type=None, response_type=None, extra_headers=None,
                 serializer=None):
    response = response_type(serializer(content), content_type=content_type)
    if extra_headers is not None:
        for header, header_value in extra_headers.iteritems():
            response[header] = header_value

    return response


def strip_charset(content_type):
    try:
        content_type, charset = content_type.split(";")
    except ValueError:
        pass
    return content_type
