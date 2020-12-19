from django.shortcuts import render
from django.views import generic

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from fake_data.models import FakeDataModel, SchemaDataModel
from fake_data.forms import SchemaCreateForm, GeneratorForm
# Create your views here.


@method_decorator([login_required, ], name='dispatch')
class FakeListView(generic.ListView):

    model = FakeDataModel
    template_name = "index.html"




@method_decorator([login_required, ], name='dispatch')
class SchemaCreateView(generic.CreateView):
    model = SchemaDataModel
    fields = ['name', 'email', 'phone_number', 'company',
              'text', 'random_int', 'date', 'address', 'row_num']
    template_name = "schema_create.html"
    success_url = "schema_list"

@method_decorator([login_required, ], name='dispatch')
class SchemaListView(generic.ListView):

    model = SchemaDataModel
    template_name = "schema_list.html"


@method_decorator([login_required, ], name='dispatch')
class GenerateDataView(generic.DetailView):
    model = SchemaDataModel
    # fields = ['model', ]
    # form_class = GeneratorForm
    template_name = "generator.html"


class FakeDataView(generic.DetailView):
    model = FakeDataModel
    template_name = "fake_data_view.html"
