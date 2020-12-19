from django.urls import path

from fake_data.views import (
    FakeListView, SchemaListView, GenerateDataView, SchemaCreateView, FakeDataView)

urlpatterns = [
    path('', FakeListView.as_view(), name='data'),
    path('schema_create', SchemaCreateView.as_view(), name='schema-create'),
    path('schema_list', SchemaListView.as_view(), name='schema-list'),
    path('schema/<pk>/generate', GenerateDataView.as_view(), name='generate-data'),
    path('schema/<pk>/', FakeDataView.as_view(), name='fake-data-view'),

]
