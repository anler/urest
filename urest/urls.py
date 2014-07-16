from .sites import site


def url(url, *args, **kwargs):
    """Resource decorator to define its route."""
    def decorator(resource):
        site.register(url, *args, **kwargs)
        return resource

    if "resource" in kwargs:
        return decorator(kwargs.pop("resource"))

    return decorator
