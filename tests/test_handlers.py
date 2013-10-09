# -*- coding: utf-8 -*-
import rest
import rest.test


request_factory = rest.test.RequestFactory()


class TestApiEndpointDecorator:

    def test_unsupported_media_type(self):
        @rest.api_endpoint(accept="")
        def view(request):
            return rest.Ok()

        response = view(request_factory.get('/url'))

        assert response.status_code == 415

    def test_not_allowed_method(self):
        @rest.api_endpoint
        def view(request):
            return rest.Ok()

        response = view(request_factory.post('/url'))

        assert response.status_code == 405
