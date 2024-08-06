from django.contrib import admin
from .models import Estudante, Curso, Matricula

@admin.register(Estudante)
class EstudanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'nascimento', 'telefone')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_per_page = 10

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descricao', 'nivel')
    search_fields = ('codigo',)

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('estudante','curso','periodo')
    search_fields = ('estudante','curso',)
