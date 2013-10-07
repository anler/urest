# -*- coding: utf-8 -*-

import json

from restart import http


# class UsersEndpoint(http.ApiEndpoint):
#     def get(self):
#         pass


api_endpoint = http.api_endpoint(accept="application/json", serializer=json.dumps,
                                 unserializer=json.loads)


@api_endpoint
def users(request):
    return request.get_response(request.data, response_type=http.Ok)


@users.post
def users(request):
    return http.Ok("post request")
