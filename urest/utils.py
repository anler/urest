import inspect

from django.utils.module_loading import import_module

from .resource import BaseResource, ResourceMetadata


def is_resource(definition):
    return inspect.isclass(definition) and issubclass(definition, BaseResource)


def autodiscover_resources(module_to_search):
    from django.apps import apps
    for app_config in apps.get_app_configs():
        try:
            module = import_module('%s.%s' % (app_config.name, module_to_search))
        except:
            pass
        else:
            for member in inspect.getmembers(module, predicate=is_resource):
                yield member


def get_resource_metadata(name, resource, url=None, args=None, kwargs=None):
    doc = inspect.getdoc(resource)
    if not doc:
        doc = "/{}".format(url=name.lower())
    if args is None:
        args = ()
    if kwargs is None:
        kwargs = {}
    if url is None:
        url = doc.split("\n")[0]

    urlname = "{module}.{name}".format(module=inspect.getmodule(resource).__name__, name=name)
    kwargs.setdefault("name", urlname)

    return ResourceMetadata(resource, clean_url(url), args, kwargs)


def clean_url(url):
    return "{}$".format(url.lstrip("/"))
