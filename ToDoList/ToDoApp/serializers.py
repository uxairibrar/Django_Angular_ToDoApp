from rest_framework import serializers
from ToDoApp.models import TODO

# Serializers in Django REST Framework are responsible for converting objects into data types 
# understandable by javascript and front-end frameworks

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model =TODO
        fields=('ID','text')
