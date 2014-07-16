# -*- coding: utf-8 -*-

__title__ = 'urest'
__version__ = '0.0.1'
__author__ = 'Anler Hp'
__license__ = 'MIT'
__copyright__ = 'Copyright 2014 Anler Hp'

from . import utils
from . import responses
from .sites import site
from .urls import url
from .views import View
from .resources import Resource


def autodiscover(module_to_search="api"):
    for name, resource in utils.autodiscover_resources(module_to_search):
        site.register(name, resource)
