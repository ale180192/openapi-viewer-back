"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import url
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from core import views as views_core

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


schema_view_ = get_swagger_view(title='openapi doc api')

urlpatterns = [
    path(r'doc/', schema_view_),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path(r'admin/', admin.site.urls),
    # path(r'api/v1/api_view', views_core.test_api_view, name='api_view'),
    # path(r'api/v1/api_view_detail', views_core.test_api_view_detail, name='api_view_detail'),
    path(r'api/v1/examples-openapi/', include('examples_openapi.urls'), name='examples-openapi'),
    # path(r'api/v1/', include('apis.urls'), name='apis'),
    # path(r'api/v1/', include('core.urls'), name='core'),
    path(r'api/v1/authentication/token',  views.ObtainAuthToken.as_view()),
    # path(r'api/v1/authentication/bad_token',  views_core.ObtainBadAuthToken.as_view())
]
