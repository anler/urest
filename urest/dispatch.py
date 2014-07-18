import inspect

from .exceptions import MissingSerializer, MissingMethod
from .response import statuses
from . import content_negotiation


HTTP_METHODS = {"get", "head", "options", "post", "put", "patch", "delete"}


def is_valid_method(obj):
    "Test if `obj` is a valid resource method."
    return inspect.ismethod(obj) and obj.__name__ in HTTP_METHODS


def get_dispatcher(view, method):
    try:
        return getattr(view, method)
    except AttributeError:
        allow = get_allowed_methods(view)
        raise MissingMethod(allow)


def get_allowed_methods(view):
    methods = inspect.getmembers(view, predicate=is_valid_method)
    return [name for name, _ in methods]


def dispatch(view, request, *args, **kwargs):
    method = request.method.lower()

    try:
        dispatcher = get_dispatcher(view, method)
        serializer = content_negotiation.get_serializer(request, view.get_serializers())
        data = dispatcher(request, *args, **kwargs)
        request.response.headers["Content-Type"] = serializer.content_type
        request.response.body = serializer.dumps(data)
    except MissingSerializer:
        request.response.status = statuses.NotAcceptable
    except MissingMethod as e:
        request.response.status = statuses.MethodNotAllowed
        request.response.headers["Allow"] = e.allow
    except Exception as e:
        request.response.status = statuses.InternalServerError
        request.response.body = serializer.dumps(e.message)

    return request.response
