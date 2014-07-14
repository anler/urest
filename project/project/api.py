import urest


class Projects(urest.Collection):
    "/projects"

    def get(self, request):
        return urest.response.Ok("Projects list")


class Project(urest.Document):
    "/projects/(?P<id>\d+)"

    def get(self, request, id):
        return urest.response.Ok("Project %s detail" % id)
