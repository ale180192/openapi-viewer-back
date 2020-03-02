from pprint import pprint

from django.test import TestCase
from django.test import RequestFactory

from core.middlewares import Log1Middleware, Log2Middleware

factory = RequestFactory()
request = factory.get('api/v1/apis')
print('---- request before call Log1Middleware')
pprint(request)
request_modified_by_midleware = Log1Middleware(request)
print('after Log1Middleware')
pprint(request_modified_by_midleware)
request_modified_by_midleware = Log2Middleware(request_modified_by_midleware)
print('---- request after call Log2Middleware')
pprint(request_modified_by_midleware)