from rest_framework.pagination import PageNumberPagination


class CustomNumberPagination(PageNumberPagination):
    page_size_query_param = 'pagesize'
    page_query_param = 'page'
    max_page_size = 100
    last_page_strings = ('last', )