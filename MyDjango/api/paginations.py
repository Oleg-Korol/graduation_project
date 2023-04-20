from rest_framework.pagination import PageNumberPagination


class BasePagination(PageNumberPagination):
    page_size = 1000
    page_query_param = 'page_size'
    max_page_size = 100000


class StandartPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 100