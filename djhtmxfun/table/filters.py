import django_filters
from .models import TableData

COL_CHOICES = [
    ("name", "name"),
    ("quantity", "quantity"),
    ("distance", "distance")
    ]

CONDITION_CHOICES = [
    ("exact", "Equals"),
    ("icontains", "Contains"),
    ("gt", "Greater than"),
    ("lt", "Less than")
    ]


class NewDataFilter(django_filters.FilterSet):
    name = django_filters.ChoiceFilter(label="Column",
                                       method="filter_column",
                                       choices=COL_CHOICES)
    date = django_filters.ChoiceFilter(label="Condition",
                                       method="filter_condition",
                                       choices=CONDITION_CHOICES)
    value = django_filters.CharFilter(label="Value", method="filter_value")

    class Meta:
        model = TableData
        fields = ["value"]

    def filter_condition(self, queryset, name, value):
        filter_kwargs = {}
        return queryset.filter(**filter_kwargs)

    def filter_column(self, queryset, name, value):
        value = self.data['value']
        condition = self.data['date']
        if value:
            column_name = self.data['name']
            column_with_con = f'{column_name}__{condition}'
            filter_kwargs = {column_with_con: value}
            return queryset.filter(**filter_kwargs)
        else:
            return queryset.filter(**{})

    def filter_value(self, queryset, name, value):
        filter_kwargs = {}
        return queryset.filter(**filter_kwargs)
