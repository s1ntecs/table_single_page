from django.core.paginator import Paginator, EmptyPage

from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

from .models import TableData
from .tables import (
    DataHTMxMultiColumnTable,
)
from .filters import NewDataFilter


class CustomPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                return self.num_pages
            elif int(number) < 1:
                return 1
            else:
                raise


class DataHTMxMultiColumTableView(SingleTableMixin, FilterView):
    table_class = DataHTMxMultiColumnTable
    queryset = TableData.objects.all()
    filterset_class = NewDataFilter
    paginate_by = 10
    paginator_class = CustomPaginator

    def get_template_names(self):
        if self.request.htmx:
            template_name = "data_table/product_table_partial.html"
        else:
            template_name = "data_table/product_table_col_filter.html"

        return template_name
