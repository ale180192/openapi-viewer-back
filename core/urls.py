from django.urls import path

from core import views

urlpatterns = [
    path(r'users', views.UsersApiViewList.as_view())
]