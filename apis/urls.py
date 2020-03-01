from django.urls import path

from apis.views import ApiViewList
from apis.views import ApiViewDetail
from apis.views_test import TestApiView, TestView

urlpatterns = [
    path(r'apiview/<int:pk>', ApiViewDetail.as_view()), # on 2.2+
    path(r'apis', ApiViewList.as_view()),
    path(r'testapiview', TestApiView.as_view()),
    path(r'testview', TestView.as_view(), name='test-view'),
    path(r'apiview', ApiViewList.as_view(), name='list'),
]