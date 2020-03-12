from rest_framework import serializers
from .models import Panel, OneHourElectricity, User, SensorData,HealthSensorData, UserCommands, UserAgeCommands, UserDiseaseCommands, CameraTrigger, Visitors

class PanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panel
        fields = ('id', 'brand', 'serial', 'latitude', 'longitude')

class OneHourElectricitySerializer(serializers.ModelSerializer):
    class Meta:
        panel = serializers.PrimaryKeyRelatedField(queryset=Panel.objects.all())
        model = OneHourElectricity
        fields = ('id', 'panel', 'kilo_watt','date_time')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'email', 'password', 'key', 'ageCategory', 'diseaseCategory')

class SensorDataSerializer(serializers.ModelSerializer):
	class Meta:
		owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
		model = SensorData
		fields = ('id', 'owner', 'sensortype', 'data', 'date','attached_status', 'triggered', 'shouldActivate')

class HealthSensorDataSerializer(serializers.ModelSerializer):
	class Meta:
		owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
		model = HealthSensorData
		fields = ('id', 'owner', 'sensortype', 'data', 'date')

 
class UserCommandsSerializer(serializers.ModelSerializer):
	class Meta:
		fromuser = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
		model = UserCommands
		fields = ('id', 'fromuser', 'date', 'command', 'status')

class UserAgeCommandsSerializer(serializers.ModelSerializer):
	class Meta:
		fromuser = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
		model = UserAgeCommands
		fields = ('id', 'fromuser', 'ageCategory')

class UserDiseaseCommandsSerializer(serializers.ModelSerializer):
	class Meta:
		fromuser = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
		model = UserDiseaseCommands
		fields = ('id', 'fromuser', 'diseaseCategory')



class PhotoTriggerSerializer(serializers.ModelSerializer):
	class Meta:
		touser = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
		model = CameraTrigger
		fields = ('id', 'touser', 'date', 'choice', 'sent', 'photo')

class VisitorsSerializer(serializers.ModelSerializer):
	class Meta:
		owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
		model = Visitors
		fields = ('id', 'owner', 'sent', 'who')