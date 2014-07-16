import urest

from . import models


class UserResource(urest.resources.Resource):
    name = urest.resources.CharField()


class ProjectResource(urest.resources.Resource):
    id = urest.resources.UrlField()
    name = urest.resources.CharField()
    order = urest.resources.IntegerField()
    owner = urest.resources.ResourceField("UserResource")


class Projects(urest.Collection):
    "/projects"
    resource = ProjectResource
    resource_proxies = (urest.proxies.PartialResponse,
                        urest.proxies.EmbeddedResource,
                        urest.proxies.OptimisticConcurrency,
                        urest.proxies.Pagination)


class Project(urest.Document):
    "/projects/(?P<id>\d+)"
    resource = ProjectResource

    def get(self):
        object = self.resource.retrieve(self.url_kwargs["id"])
        return self.get_response(object, response_class=urest.Ok)


class ProjectUsers(urest.Collection):
    "/projects/(?P<project_id>\d+)/users"
    resource = UserResource
    parent = urest.parent_resource(ProjectResource, param="project_id")

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
