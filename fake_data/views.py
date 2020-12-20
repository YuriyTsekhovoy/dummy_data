from django.shortcuts import render
from django.views import generic

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from fake_data.models import FakeDataModel, SchemaDataModel


@method_decorator([login_required, ], name='dispatch')
class FakeListView(generic.ListView):
    model = FakeDataModel
    template_name = "index.html"


@method_decorator([login_required, ], name='dispatch')
class SchemaListView(generic.ListView):

    model = SchemaDataModel
    template_name = "schema_list.html"


@method_decorator([login_required, ], name='dispatch')
class SchemaCreateView(generic.CreateView):
    model = SchemaDataModel
    fields = ['title', 'name', 'email', 'phone_number', 'company',
              'text', 'random_int', 'date', 'address', ]
    template_name = "schema_create.html"
    success_url = "schema_list"


class SchemaDetailView(generic.DetailView):
    model = SchemaDataModel
    template_name = "schema_detail.html"


@method_decorator([login_required, ], name='dispatch')
class GenerateDataView(generic.CreateView):
    model = FakeDataModel
    fields = ['row_num', ]
    success_url = "/data_sets/"
    template_name = "generate_data.html"

    def form_valid(self, form):
        schema_model = SchemaDataModel.objects.get(pk=self.kwargs['pk'])
        self.object = form.save(commit=False)
        self.object.model = schema_model
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@method_decorator([login_required, ], name='dispatch')
class DataDetailView(generic.DetailView):
    model = FakeDataModel
    template_name = "data_detail.html"


@method_decorator([login_required, ], name='dispatch')
class DataListView(generic.ListView):
    model = FakeDataModel
    template_name = "data_list.html"
