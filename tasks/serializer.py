from rest_framework import serializers
from .models import Task 
class TaskSerializar(serializers.ModelSerializer):
    class Meta:
        model = Task
      #  fields = ('id', 'title', 'description','f_creation', 'done')
        fields = '__all__'