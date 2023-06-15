import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Women


class WomenModel:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    class Meta:
        model = Women
        fields = ("__all__")

#     def create(self, validated_data):
#         return Women.objects.create(**validated_data)
#
#     def update(self, instanse, validated_data):
#         instanse.title = validated_data.get("title", instanse.title)
#         instanse.time_update = validated_data.get("time_update", instanse.time_update)
#         instanse.is_published = validated_data.get("is_published", instanse.is_published)
#         instanse.cat_id = validated_data.get("cat_id", instanse.cat_id)
#         instanse.save()
#         return instanse
#
#
#
#
# def encode():
#     model = WomenModel("Title 1", "Content : Title 1 Content")
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json, type(json), sep='\n')
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Title 1","content":"Content : Title 1 Content"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)



