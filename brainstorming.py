import urest


@urest.controller
def gifts(request):
    return urest.Ok()


@urest.store
def gifts(request):
    return urest.NoContent()


class Gifts(urest.Collection):
    pass


class Gift(urest.Document):
    pass
