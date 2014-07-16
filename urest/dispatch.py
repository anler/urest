import inspect

from .exceptions import MissingSerializer, MissingDispatcherMethod


HTTP_METHODS = {"get", "head", "options", "post", "put", "patch", "delete"}


def is_valid_method(obj):
    "Test if `obj` is a valid resource method."
    return inspect.ismethod(obj) and obj.__name__ in HTTP_METHODS


def get_dispatcher(view, method):
    try:
        return getattr(view, method)
    except AttributeError:
        raise MissingDispatcherMethod


def get_allowed_methods(view):
    methods = inspect.getmembers(view, predicate=is_valid_method)
    return [name for name, _ in methods]


def dispatch(view, request, *args, **kwargs):
    method = request.headers.get("X-Http-Method-Override", request.method).lower()

    try:
        dispatcher = get_dispatcher(view, method)
        response = dispatcher(request, *args, **kwargs)
    except MissingSerializer:
        response = response.UnsupportedMediaType()
    except MissingDispatcherMethod:
        response = response.MethodNotAllowed(allowed=get_allowed_methods(view))

    return response
