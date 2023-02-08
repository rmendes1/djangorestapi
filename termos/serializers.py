# serializers.py
from rest_framework import serializers
from .models import Term1, Term2, Term3, Term4


# class TermSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = None
#         fields = '__all__'


class Term1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Term1
        fields = '__all__'


class Term2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Term2
        fields = '__all__'


class Term3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Term3
        fields = '__all__'


class Term4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Term4
        fields = '__all__'
