import django_tables2 as tables

from .models import TableData


class DataHTMxMultiColumnTable(tables.Table):
    class Meta:
        model = TableData
        show_header = False
        template_name = "tables/bootstrap_col_filter.html"
