from django.urls import path

from .views import (
    DataHTMxMultiColumTableView
)

urlpatterns = [
    path(
        "table/",
        DataHTMxMultiColumTableView.as_view(),
        name="data_table",
    ),
]
