from restart import http


# class UsersEndpoint(http.ApiEndpoint):
#     def get(self):
#         pass


@http.api_endpoint
def users(request):
    return http.Ok("get request")


@users.post
def users(request):
    return http.Ok("post request")
