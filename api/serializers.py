from rest_framework import serializers
from .models import Work

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'
        
