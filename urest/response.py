# -*- coding: utf-8 -*-


class Statuses(dict):
    def __getattr__(self, name):
        if name in self:
            return self[name]
        raise AttributeError


statuses = Statuses({
    "Ok": 200,
    "Created": 201,
    "Accepted": 202,
    "NoContent": 204,
    "MultipleChoices": 300,
    "MovedPermanently": 301,
    "Found": 302,
    "SeeOther": 303,
    "NotModified": 304,
    "TemporaryRedirect": 307,
    "BadRequest": 400,
    "Unauthorized": 401,
    "Forbidden": 403,
    "NotFound": 404,
    "MethodNotAllowed": 405,
    "NotAcceptable": 406,
    "Conflict": 409,
    "Gone": 410,
    "PreconditionFailed": 412,
    "UnsupportedMediaType": 415,
    "TooManyRequests": 429,
    "InternalServerError": 500,
    "NotImplemented": 501,
})
