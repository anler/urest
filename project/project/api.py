import urest

from . import models


class UserResource(urest.resources.Resource):
    name = urest.resources.CharField()


class ProjectResource(urest.resources.Resource):
    def list(self, request):
        pass

    def retrieve(self, request, id):
        pass


class ProjectMixin:
    resource = ProjectResource()


class Projects(ProjectMixin, urest.Collection):
    "/projects"


class Project(ProjectMixin, urest.Document):
    "/projects/(?P<pk>\d+)"
    lookup = lambda args, kwargs: kwargs["pk"]


class ProjectUserMixin:
    resource = UserResource()
    parent = ProjectResource()
    parent_lookup = lambda args, kwargs: kwargs["project_id"]


class ProjectUsers(ProjectUserMixin, urest.Collection):
    "/projects/(?P<project_id>\d+)/users"
    parent =

    def get(self):
        objects = self.resource.list(self.parent)
        return self.get_response(object, response_class=urest.Ok)


class ProjectUser(urest.Document):
    "/projects/(?P<id>\d+)/users/(?P<user_id>\d+)"
    resource = UserResource
    parent = urest.parent(Project, param="project_id")

    def get(self):
        object = self.resource.retrieve(self.parent.resource)
        return self.get_response(object, response_class=urest.Ok)


class ProjectUserSongs(urest.Collection):
    "/projects/(?P<project_id>\d+)/users/(?P<user_id>)\d+"
    resource = UserSongResource
    parent = urest.parent(ProjectUser, param="user_id")

    def get(self):
        objects = self.resource.list(self.parent.resource)
        return self.get_response(object, response_class=urest.Ok)
