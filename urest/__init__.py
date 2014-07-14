# -*- coding: utf-8 -*-

from .resource import Collection, Document, Store, Controller
from .sites import site
from . import response, utils

__version__ = '0.0.1'

# Version synonym
VERSION = __version__


def autodiscover(module_to_search="api"):
    for name, resource in utils.autodiscover_resources(module_to_search):
        site.register(name, resource)


def url(url, *args, **kwargs):
    def decorator(resource):
        site.register(url, *args, **kwargs)
        return resource

    if "resource" in kwargs:
        return decorator(kwargs.pop("resource"))

    return decorator
