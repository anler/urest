django-rest
===========

Django REST is a set of utilities that let you write beautiful REST APIs with total freedom.

## Examples ##

Use response classes to explicitly say the response type you want to send.

```python
import rest


@rest.handler
def gifts(request):
    return rest.Ok("list of gifts!")


@gifts.post
def gifts(request):
    return rest.Created("new gift created!")
```


Use `request.get_response` to create a response with a `Content-Type` accepted by the client:

```python
import rest


json_api = rest.handler(accept="application/json", serializer=json.dumps, unserializer=json.loads)


@json_api
def candies(request):
    candies = {}
    return request.get_response(candies)


@candies.post
def create_candy(request):
    return request.get_response(response_type=rest.Created)
```
