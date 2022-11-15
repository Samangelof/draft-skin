import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Warrior

# class WarriorModel:
#     def __init__(self, name, specialization) -> None:
#         self.name = name
#         self.specialization = specialization

  
        
class WarriorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Warrior
        fields = ('__all__')





