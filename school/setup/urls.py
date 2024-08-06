from django.contrib import admin
from django.urls import path, include
from apps.escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculasEstudante, ListaMatriculasCurso
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename="Estudantes")
router.register('cursos', CursoViewSet, basename="Cursos")
router.register('matriculas', MatriculaViewSet, basename="Matriculas")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudante/<int:pk>/matriculas/', ListaMatriculasEstudante.as_view()),
    path('curso/<int:pk>/matriculas/', ListaMatriculasCurso.as_view()),
]
