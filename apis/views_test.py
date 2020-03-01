from django.views import View
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response 


class TestApiView(APIView):

    def setup(self, request, *args, **kwargs):
        print('setup myview', request, args, kwargs)
        super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        print('dispatch myview', args, kwargs)
        return super().dispatch(request, *args, **kwargs)

    
    def get(self, request, format=None):
        msg = 'hola'
        return Response(data=msg)


class TestView(View):

    def setup(self, request, *args, **kwargs):
        print('setup myview', request, args, kwargs)
        super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        print('dispatch myview', args, kwargs)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        print('get myview')
        return HttpResponse('hola mundo :3')