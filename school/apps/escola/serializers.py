from rest_framework import serializers
from .models import Estudante, Curso, Matricula
from . import validators as val

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = '__all__'

    def validate(self, dados):
        if val.validate_nome(dados['nome']):
            raise serializers.ValidationError({'nome': 'o mome deverá conter apenas letras!'})
        if val.validate_cpf(dados['cpf']):
            raise serializers.ValidationError({'cpf': 'o cpf inserido deve ser um cpf válido!'})
        if val.validate_telefone(dados['telefone']):
            raise serializers.ValidationError({'telefone': 'o telefone inserido deve ser um telefone válido!'})

        return dados

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso','periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')

    class Meta:
        model = Matricula
        fields = ['estudante_nome']
    