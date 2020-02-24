from django.urls import path

from apis.views import ApiListView

urlpatterns = [
    path(r'apis', ApiListView.as_view()),
]