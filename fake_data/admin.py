from django.contrib import admin

# Register your models here.

from fake_data.models import (FakeDataModel, SchemaDataModel)


class FakeDataModelAdmin(admin.ModelAdmin):
    class Meta:
        model = FakeDataModel
        fields = ['model', ]


class SchemaDataModelAdmin(admin.ModelAdmin):
    class Meta:
        model = SchemaDataModel


admin.site.register(FakeDataModel, FakeDataModelAdmin)
admin.site.register(SchemaDataModel, SchemaDataModelAdmin)