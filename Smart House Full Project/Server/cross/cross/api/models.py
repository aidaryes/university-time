from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator

class Panel(models.Model):
    brand = models.CharField(max_length=200)
    serial = models.CharField(max_length=16, validators=[MinLengthValidator(16)])
    latitude = models.DecimalField(decimal_places=6,max_digits=8, validators=[MaxValueValidator(90), MinValueValidator(-90)])
    longitude = models.DecimalField(decimal_places=6,max_digits=9, validators=[MaxValueValidator(180), MinValueValidator(-180)])
    def __str__(self):
        return "Brand: {0}, Serial: {1} ".format(self.brand, self.serial)

class OneHourElectricity(models.Model):
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE)
    kilo_watt = models.BigIntegerField()
    date_time = models.DateTimeField()
    def __str__(self):
        return "Hour: {0} - {1} KiloWatt".format(self.date_time, self.kilo_watt)

class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    ageCategory = models.IntegerField(default=0)
    diseaseCategory = models.IntegerField(default = 0)
    def __str__(self):
        return "Email: {0} with a key: {1}".format(self.email, self.key)
 
class SensorData(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    sensortype = models.CharField(max_length=50)
    data = models.BigIntegerField()
    date = models.DateTimeField(default="0")
    attached_status = models.BigIntegerField()
    triggered = models.BigIntegerField(default='0')
    shouldActivate = models.IntegerField(default = 0)
    def __str__(self):
        return "{0} sensor has {1} value at {2} and belongs to {3}".format(self.date, self.sensortype, self.data, self.owner)

class UserCommands(models.Model):
    fromuser = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    command = models.CharField(max_length=50)
    status = models.BigIntegerField()
    def __str__(self):
        return "Command from {0} to activate {1}".format(self.fromuser, self.command)

class UserAgeCommands(models.Model):
    fromuser = models.ForeignKey(User, on_delete=models.CASCADE)
    ageCategory = models.IntegerField(default = 0)
    

class UserDiseaseCommands(models.Model):
    fromuser = models.ForeignKey(User, on_delete=models.CASCADE)
    diseaseCategory = models.IntegerField(default = 0)

class CameraTrigger(models.Model):
    touser = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    choice = models.BigIntegerField()
    sent = models.BigIntegerField()
    photo = models.ImageField(upload_to = 'pic_folder', default = 'pic_folder/None')
    def __str__(self):
        return "Photo sent to {0} at {1}".format(self.touser.email, self.date)

class Visitors(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    sent = models.BigIntegerField()
    who = models.CharField(max_length=50)
    def __str__(self):
        return "Visitor: {0}".format(self.who)
class HealthSensorData(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    sensortype = models.CharField(max_length=50)
    data = models.FloatField()
    date = models.DateTimeField()
    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(self.date, self.sensortype, self.data, self.owner)
class mSensorData(models.Model):
    sensortype = models.CharField(max_length=50)
    data = models.IntegerField()
    date = models.CharField(max_length=50)
    owner_id = models.IntegerField()
    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(self.date, self.sensortype, self.data, self.owner)
