from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from academico.models import Curso

# Register your models here.


class CursoResources(resources.ModelResource):
    fields = {
        'codigo',
        'nombre',
        'creditos',
    }

    class Meta:
        model = Curso


@admin.register(Curso)
class CursoAdmin(ImportExportModelAdmin):
    resource_class = CursoResources
