from django.conf import urls

from .views import as_view
from .utils import get_view_metadata


class Site(object):
    def __init__(self):
        self.registry = {}  # url -> metadata

    def register(self, name, view, url=None, args=None, kwargs=None):
        metadata = get_view_metadata(name, view, url, args, kwargs)
        self.registry[(metadata.url, metadata.args)] = metadata

    @property
    def urls(self):
        pattern_urls = [urls.url(m.url, as_view(m.view), *m.args, **m.kwargs)
                        for m in self.registry.values()]
        return urls.patterns('', *pattern_urls)
site = Site()
