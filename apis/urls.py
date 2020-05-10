from django.urls import path

from apis.views import ApiViewList, ApiFakeViewList
from apis.views import ApiViewDetail, ApiFakeViewDetail, ApiSerializerPagination
from apis.views_test import TestApiView, TestView

urlpatterns = [
    path(r'apiview/<int:pk>', ApiViewDetail.as_view()), # on 2.2+
    path(r'apis', ApiViewList.as_view()),
    path(r'apisfake', ApiFakeViewList.as_view()),
    path(r'apisfake-pagination', ApiSerializerPagination.as_view()),
    path(r'apisfake/<int:pk>', ApiFakeViewDetail.as_view()),
    path(r'testapiview', TestApiView.as_view()),
    path(r'testview', TestView.as_view(), name='test-view'),
    path(r'apiview', ApiViewList.as_view(), name='list'),
]