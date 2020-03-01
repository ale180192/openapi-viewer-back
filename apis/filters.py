from django_filters import rest_framework as filters

from apis.models import Api

class ApiFilter(filters.FilterSet):
    def __init__(self, *args, author=None, **kwargs):
        super().__init__(*args, **kwargs)

    name = filters.CharFilter(field_name='name', lookup_expr='contains')
    username = filters.CharFilter(field_name='user__username', lookup_expr='contains')

    class Meta:
        model: Api
        fields = ['user__username', 'name']