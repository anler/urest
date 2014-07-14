from django.conf import urls

from .resource import resource_as_view
from .utils import get_resource_metadata


class Site(object):
    def __init__(self):
        self._registry = {}  # url -> metadata

    def register(self, name, resource, url=None, args=None, kwargs=None):
        metadata = get_resource_metadata(name, resource, url, args, kwargs)
        self._registry[(metadata.url, metadata.args)] = metadata

    @property
    def urls(self):
        pattern_urls = [urls.url(m.url, resource_as_view(m.resource), *m.args, **m.kwargs)
                        for m in self._registry.values()]
        assert len(pattern_urls) == 2
        return urls.patterns('', *pattern_urls)
site = Site()
