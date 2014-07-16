import pytest

from urest.exceptions import MissingDispatcherMethod
from urest.dispatch import is_valid_method, get_allowed_methods, get_dispatcher


def test_is_valid_method():
    class View:
        def get(self):
            pass

        def unknown(self):
            pass

    assert is_valid_method(View().get)
    assert not is_valid_method(View().unknown)


def test_get_allowed_methods():
    class View:
        def get(self):
            pass

        def post(self):
            pass

        def unknown(self):
            pass

    assert get_allowed_methods(View()) == ["get", "post"]


def test_get_dispatcher():
    class View:
        def get(self):
            pass

    view = View()

    assert get_dispatcher(view, "get") == view.get
    with pytest.raises(MissingDispatcherMethod):
        get_dispatcher(view, "post")
