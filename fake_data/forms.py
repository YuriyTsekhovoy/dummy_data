from django import forms
from fake_data.fake_factory import FakeDataGen, gen_fake_data
from fake_data.models import SchemaDataModel, FakeDataModel


class SchemaCreateForm(forms.ModelForm):

    class Meta:
        model = SchemaDataModel
        fields = '__all__'


class GeneratorForm(forms.ModelForm):

    class Meta:
        model = FakeDataModel
        fields = '__all__'
