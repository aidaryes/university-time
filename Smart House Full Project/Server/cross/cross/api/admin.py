from django.contrib import admin
from .models import User, SensorData, HealthSensorData, mSensorData

admin.site.register(User)
admin.site.register(SensorData)
admin.site.register(HealthSensorData)
admin.site.register(mSensorData)

