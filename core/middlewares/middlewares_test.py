'''
    To test function it of middlewares must added this classes to MIDDLEWARE variable into settings.py file

    MIDDLEWARE = [
        'core.middlewares.middlewares_test.Log1Middleware',
        'core.middlewares.middlewares_test.Log2Middleware',
        .
        .
    ]
'''
class Log1Middleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.META.update({'msg': 'Este es un mensaje agregado desde log 1'})
        response = self.get_response(request)
        return response

class Log2Middleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('call __call__ before Log2Middleware')
        print('msg recibido en log2 es: ', request.META['msg'])
        response = self.get_response(request)
        print('Log2Middleware after of get_response')
        return response
