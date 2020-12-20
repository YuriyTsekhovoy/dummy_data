from django.urls import path

from fake_data.views import (
    FakeListView, SchemaListView, GenerateDataView,
    SchemaCreateView, SchemaDetailView, DataDetailView,
    DataListView)

urlpatterns = [
    path('', FakeListView.as_view(), name='home'),
    path('schema_create', SchemaCreateView.as_view(), name='schema-create'),
    path('schema_list', SchemaListView.as_view(), name='schema-list'),
    path('schema_detail/<pk>', SchemaDetailView.as_view(), name='schema-detail'),
    path('data_sets/<pk>/generate', GenerateDataView.as_view(), name='generate-data'),
    path('data_sets/<pk>/', DataDetailView.as_view(), name='data-detail'),
    path('data_sets/', DataListView.as_view(), name='data-list'),

]
