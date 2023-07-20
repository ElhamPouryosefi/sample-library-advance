from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination

from core.library_modules.response_handler import Response


class DefaultPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'limit'
    max_page_size = 10000

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('all_page', self.page.paginator.num_pages),
            ('count', self.page.paginator.count),
            ('current', self.page.number),
            ('has_next', self.page.has_next()),
            ('has_previous', self.page.has_previous()),
            ('results', data)
        ]))
