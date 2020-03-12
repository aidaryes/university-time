from rest_framework import viewsets,status
from rest_framework.views import APIView, Response
from django.views.generic.edit import CreateView
from .models import Panel, OneHourElectricity, User, SensorData, UserCommands,  CameraTrigger, HealthSensorData, Visitors
from .serializers import PanelSerializer, OneHourElectricitySerializer, UserSerializer, UserAgeCommandsSerializer, UserDiseaseCommandsSerializer, HealthSensorDataSerializer, SensorDataSerializer, UserCommandsSerializer, PhotoTriggerSerializer, VisitorsSerializer
from .test import run_on_file

from datetime import datetime, date, timedelta
import random
import time
import csv
import pandas as pd
import numpy as np
import json
import copy
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.utils.timezone import make_aware
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import svm, neighbors
from sklearn.ensemble import VotingClassifier, RandomForestClassifier
import requests

class UserView(APIView):
    serializer_class = UserSerializer

    def get(self, request):
        queryset=User.objects.all()
        items = UserSerializer(queryset, many=True)
        return Response(items.data)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDataViewID(APIView):
    serializer_class = UserSerializer

    def get(self, request, userid):
        queryset=User.objects.filter(pk=userid)
        items = UserSerializer(queryset, many=True)
        return Response(items.data)

class ChangeUserDataViewID(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        queryset=User.objects.filter(pk=userid)
        items = UserSerializer(queryset, many=True)
        return Response(items.data)        

def do_ml(data):
    size = len(data['data'])
    
    X = data[['data','body_temp','syst_pres','dias_pres']]
    y = data['triggered']
           
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
    clf = VotingClassifier([
                            ('lsvc', svm.SVC(kernel='linear')),
                            ('nlsvc', svm.SVC(kernel='rbf', C=1, gamma=0.01)),
                            ('knn', neighbors.KNeighborsClassifier(n_neighbors=5, weights='distance', algorithm='auto')),
                            ('rfor', RandomForestClassifier(n_estimators=100, max_depth=None, random_state=None)),
                            ('tree', DecisionTreeClassifier(splitter='best', max_depth=None, random_state=None))
                           ], voting='hard')
    
    clf.fit(X_train, y_train)
    y_pred = clf.predict([[data.values[-1][2],data.values[-1][6],data.values[-1][7],data.values[-1][8]]])
    
    return y_pred

class SensorDataView(APIView):

    serializer_class = SensorDataSerializer

    def get(self, request):
        queryset=SensorData.objects.all()
        items = SensorDataSerializer(queryset, many=True)
        return Response(items.data)
    def post(self, request):
        # print(request.data['owner'])
        # print("Date:"+request.data['date'])
        request.data['date'] = (datetime.now()+timedelta(hours=6)).strftime('%Y-%m-%dT%H:%M:%S')
        # print("Date:"+request.data['date'])
        new_data = User.objects.get(pk=request.data['owner'])
        


        serializer = SensorDataSerializer(data=request.data)


        csv.register_dialect('myDialect',
                             quoting=csv.QUOTE_ALL,
                             skipinitialspace=True)

        data = SensorData.objects.last()
        bodyTempInstance = HealthSensorData.objects.filter(sensortype="Body_Temp").order_by('-id')[0]
        systolicBloodPressureInstance = HealthSensorData.objects.filter(sensortype="Systolic_Blood_Pressure").order_by('-id')[0]
        diastolicBloodPressureInstance = HealthSensorData.objects.filter(sensortype="Diastolic_Blood_Pressure").order_by('-id')[0]
        
        with open('data.csv', 'a') as f:
            writer = csv.writer(f, dialect='myDialect')
            row = [data.id, data.owner_id, data.sensortype, data.data, data.date, data.attached_status, data.triggered,
                   bodyTempInstance.data, systolicBloodPressureInstance.data, diastolicBloodPressureInstance.data]
            writer.writerow(row)
        f.close()

        df = pd.read_csv('data.csv', parse_dates=True, index_col=0)
        size = len(df)           

        # desirable action
        tempDesAct = 1
        humidDesAct = 1

        tempData = df.loc[df['sensortype'] == 'Temp']
        tempLastInfo = tempData.values[-1]
        tempLastData = tempLastInfo[2]

        
        tempResult = do_ml(tempData)
        
        if tempResult == 0:
            if tempLastData >= 22 and tempLastData <= 24:
                tempDesAct = 0
            elif (tempLastData >= 18 and tempLastData < 22) or (tempLastData > 24 and tempLastData <= 26):
                if new_data.ageCategory == 0:
                    if new_data.diseaseCategory == 0:
                        tempDesAct = 0
                    else:
                        tempDesAct = 1
                else:
                    tempDesAct = 1
            else:
                tempDesAct = 1

        print("Should activate AC: ", tempDesAct)
        
        humidData = df.loc[df['sensortype'] == 'Humid']
        humidLastInfo = humidData.values[-1]
        humidLastData = humidLastInfo[2]
        
        humidResult = do_ml(humidData)
        if humidResult == 0:
            if humidLastData >= 15 and humidLastData <= 20:
                humidDesAct = 0
            elif (humidLastData >= 12 and humidLastData < 15) or (humidLastData > 20 and humidLastData <= 25):
                if new_data.ageCategory == 0:
                    if new_data.diseaseCategory == 0:
                        humidDesAct = 0
                    else:
                        humidDesAct = 1
                else:
                    humidDesAct = 1
            else:
                humidDesAct = 1
               

        print("Should activate Humidifier: ", humidDesAct)

        if request.data['sensortype'] == 'Temp':
            request.data['shouldActivate'] = tempDesAct
        if request.data['sensortype'] == 'Humid':
            request.data['shouldActivate'] = humidDesAct
            
        if serializer.is_valid():

            serializer.save()
    

        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteSensorDataView(APIView):
    serializer_class = SensorDataSerializer

    def get(self, request):
        queryset = SensorData.objects.all().delete()

class SensorDataViewID(APIView):
    serializer_class = SensorDataSerializer

    def get(self, request, userid):
        queryset=SensorData.objects.filter(owner=userid)
        items = SensorDataSerializer(queryset, many=True)
        return Response(items.data)

                        

class SensorDataViewIDTemp(APIView):
    serializer_class = SensorDataSerializer
    def get(self,request,userid):
        queryset=SensorData.objects.filter(owner=userid, sensortype="Temp")
        items = SensorDataSerializer(queryset, many=True)
        return Response(items.data)

class SensorDataViewIDGas(APIView):
    serializer_class = SensorDataSerializer
    def get(self,request,userid):
        queryset=SensorData.objects.filter(owner=userid, sensortype="Gas")
        items = SensorDataSerializer(queryset, many=True)
        return Response(items.data)

class SensorDataViewIDHumid(APIView):
    serializer_class = SensorDataSerializer
    def get(self,request,userid):
        queryset=SensorData.objects.filter(owner=userid, sensortype="Humid")
        items = SensorDataSerializer(queryset, many=True)
        return Response(items.data)

class UserCommandsView(APIView):
    serializer_class = UserCommandsSerializer

    def get(self, request):
        queryset=UserCommands.objects.all()
        items = UserCommandsSerializer(queryset, many=True)
        return Response(items.data)
    def post(self, request):
        serializer = UserCommandsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            new_data = SensorData.objects.filter(owner=request.data['fromuser']).filter(sensortype=request.data['command']).order_by('date')
            #new_data[len(new_data)-1]['triggered']=request.data['status']
            setattr(new_data[len(new_data)-1], "triggered", request.data['status'])
            new_data[len(new_data)-1].save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AgeCategoryChangeView(APIView):
    serializer_class = UserAgeCommandsSerializer

    
    def post(self, request, userid):
        # print("asd" , request.data['fromuser'])# new_data.ageCategory = request.data['ageCategory']

        serializer = UserAgeCommandsSerializer(data=request.data)
        if serializer.is_valid():
            # print("asdasdasdd")
            serializer.save()

            new_data = User.objects.get(pk=request.data['fromuser'])
            new_data.ageCategory = request.data['ageCategory']
            new_data.save()
            # print(new_data)
            # # new_data.diseaseCategory = request.data['diseaseCategory']
            # #new_data[len(new_data)-1]['triggered']=request.data['status']
            
            # new_data.save(update_fields=["ageCategory"])

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class DiseaseCategoryChangeView(APIView):
    serializer_class = UserDiseaseCommandsSerializer

    
    def post(self, request, userid):
        serializer = UserDiseaseCommandsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            new_data = User.objects.get(pk=request.data['fromuser'])
            # new_data.ageCategory = request.data['ageCategory']
            new_data.diseaseCategory = request.data['diseaseCategory']
            #new_data[len(new_data)-1]['triggered']=request.data['status']
            
            new_data.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                

class DeleteAllCommandsView(APIView):
    serializer_class = UserCommandsSerializer

    def get(self, request):
        queryset=UserCommands.objects.all().delete()

class UserCommandsViewID(APIView):
    serializer_class = UserCommandsSerializer

    def get(self,request,userid):
        queryset=UserCommands.objects.filter(fromuser=userid)
        items = UserCommandsSerializer(queryset, many=True)
        return Response(items.data)

class UserCommandsViewTempID(APIView):
    serializer_class = UserCommandsSerializer
    def get(self,request,userid):
        queryset=UserCommands.objects.filter(fromuser=userid, command="Temp", status__gte=0).order_by('-date')
        items = UserCommandsSerializer(queryset, many=True)

        if len(items.data) <= 0:
            return Response(items.data)
        # print(type(items.data[0]))    
        return Response(items.data[0])

class UserCommandsViewTempOKID(APIView):
    serializer_class = UserCommandsSerializer
    def get(self,request,userid):
        queryset=UserCommands.objects.filter(fromuser=userid, command="Temp", status__gte=0).order_by('-date').update(status=-1)
        items = UserCommandsSerializer(queryset, many=True)
        if len(items.data) <= 0:
            return Response(items.data)
        return Response(items.data[0])

class UserCommandsViewHumidID(APIView):
    serializer_class = UserCommandsSerializer
    def get(self,request,userid):
        queryset=UserCommands.objects.filter(fromuser=userid, command="Humid", status__gte=0).order_by('-date')
        items = UserCommandsSerializer(queryset, many=True)
        if len(items.data) <= 0:
            return Response(items.data)
        return Response(items.data[0])

class UserCommandsViewHumidOKID(APIView):
    serializer_class = UserCommandsSerializer
    def get(self,request,userid):
        queryset=UserCommands.objects.filter(fromuser=userid, command="Humid", status__gte=0).order_by('-date').update(status=-1)
        items = UserCommandsSerializer(queryset, many=True)
        if len(items.data) <= 0:
            return Response(items.data)
        return Response(items.data[0])

class UserCommandsViewGasID(APIView):
    serializer_class = UserCommandsSerializer
    def get(self,request,userid):
        queryset=UserCommands.objects.filter(fromuser=userid, command="Gas", status__gte=0).order_by('-date')
        items = UserCommandsSerializer(queryset, many=True)
        if len(items.data) <= 0:
            return Response(items.data)
        return Response(items.data[0])

class UserCommandsViewGasOKID(APIView):
    serializer_class = UserCommandsSerializer
    def get(self,request,userid):
        queryset=UserCommands.objects.filter(fromuser=userid, command="Gas", status__gte=0).order_by('-date').update(status=-1)
        items = UserCommandsSerializer(queryset, many=True)
        if len(items.data) <= 0:
            return Response(items.data)
        return Response(items.data[0])

class VisitorsByIdView(APIView):
    serializer_class = VisitorsSerializer

    def get(self, request, userid):
        queryset1=Visitors.objects.filter(owner=userid, sent=0)
        items1=VisitorsSerializer(queryset1, many=True)
        clones=copy.deepcopy(items1.data)
        # print(clones)
        queryset1 = queryset1.update(sent=1)
        # print(clones)
        return Response(items1.data)

class VisitorsPost(APIView):
    serializer_class = VisitorsSerializer

    def get(self, request):
        queryset=Visitors.objects.all()
        items = VisitorsSerializer(queryset, many=True)
        return Response(items.data)

    def post(self, request):
        serializer = VisitorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhotoTriggerView(APIView):
    serializer_class = PhotoTriggerSerializer

    def get(self, request):
        queryset=CameraTrigger.objects.all()
        items = PhotoTriggerSerializer(queryset, many=True)
        return Response(items.data)
    def post(self,request):
        serializer = PhotoTriggerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            queryset=CameraTrigger.objects.all()
            items = PhotoTriggerSerializer(queryset, many=True)

            # print('~/django/smartnu/smartenv/cross{0}'.format(items.data[len(items.data)-1]['photo']))
            responce = run_on_file(items.data[len(items.data)-1]['photo'])
            # responce = "unknown"
            if responce != "unknown":
                dicti={"owner":1, "sent":0, "who":responce}
                requests.post("http://localhost:8080/visitors/", dicti)
                # vSerializer = VisitorsSerializer(data=visitor)
                # vSerializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhotoTriggerUserView(APIView):
    serializer_class = PhotoTriggerSerializer

    def get(self, request, userid):
        queryset=CameraTrigger.objects.filter(touser=userid, sent=0).order_by('-date').reverse()
        items = PhotoTriggerSerializer(queryset, many=True)
        return Response(items.data)

class PhotoAcceptedView(APIView):
    serializer_class = PhotoTriggerSerializer

    def get(self, request, photoid):
        queryset=CameraTrigger.objects.filter(id=photoid)
        queryset=queryset.update(sent=1)
        items = PhotoTriggerSerializer(CameraTrigger.objects.filter(id=photoid), many=True)
        return Response(items.data)

class PanelView(APIView):
    serializer_class = PanelSerializer

    def get(self, request):
        queryset=Panel.objects.all()
        items = PanelSerializer(queryset, many=True)
        return Response(items.data)

    def post(self, request):
        serializer = PanelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PanelViewID(APIView):
    serializer_class = PanelSerializer

    def get(self,request,panelid):
        queryset=Panel.objects.filter(id=panelid)
        items = PanelSerializer(queryset, many=True)
        return Response(items.data)

class HourAnalyticsView(APIView):
    serializer_class = OneHourElectricitySerializer
#
#     def get(self, request, panelid):
#         panelid = int(self.kwargs.get('panelid', 0))
#         queryset = OneHourElectricity.objects.filter(panel_id=panelid)
#         items = OneHourElectricitySerializer(queryset, many=False)
#         return Response(items.data)
#
#     def post(self, request, panelid):
#         panelid = int(self.kwargs.get('panelid', 0))
#         serializer = OneHourElectricitySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
class DayAnalyticsView(APIView):
    def get(self, request, panelid):
        # Please implement this method to return Panel's daily analytics data
        #get all id`s data
        panelid = int(panelid)
        allData = OneHourElectricity.objects.all().order_by('-date_time')
        idsData=[]
        curr_date=0
        responce=[]
        sameday_counter=1
        for i in range(len(allData)):
            if int(allData[i].panel.id) == panelid:
                if allData[i].date_time.date() < datetime.today().date():
                    if curr_date == 0 or (curr_date.date().year != allData[i].date_time.date().year or curr_date.date().month != allData[i].date_time.date().month or curr_date.date().day != allData[i].date_time.date().day):
                        if curr_date != 0 :
                            responce[len(responce)-1]['average'] = responce[len(responce)-1]['sum']/sameday_counter
                        curr_date = allData[i].date_time
                        responce.append({
                            "date_time": curr_date.date(),
                            "sum": int(allData[i].kilo_watt),
                            "average": int(allData[i].kilo_watt),
                            "maximum": int(allData[i].kilo_watt),
                            "minimum": int(allData[i].kilo_watt),
                            })
                        sameday_counter=1
                    else:
                        sameday_counter += 1
                        ii = len(responce)-1
                        responce[ii]['sum'] += allData[i].kilo_watt
                        if responce[ii]['maximum'] < allData[i].kilo_watt:
                            responce[ii]['maximum'] = allData[i].kilo_watt
                        elif responce[ii]['minimum'] > allData[i].kilo_watt:
                            responce[ii]['minimum'] = allData[i].kilo_watt
        return Response(responce)

class CreateCsv(APIView):
    # bodyTempInstance = list(HealthSensorData.objects.filter(sensortype="Body_Temp"))
    # diastolicBloodPressureInstance = list(HealthSensorData.objects.filter(sensortype="Diastolic_Blood_Pressure"))
    #
    # systolicBloodPressureInstance = list(HealthSensorData.objects.filter(sensortype="Systolic_Blood_Pressure"))
    #
    #
    # tempInstance = list(SensorData.objects.filter(sensortype="Temp"))
    #
    # humidInstance = list(SensorData.objects.filter(sensortype="Humid"))
    #
    # gasInstance = list(SensorData.objects.filter(sensortype="Gas"))
    #
    #
    #
    # maxSize = max(len(bodyTempInstance), len(systolicBloodPressureInstance), len(diastolicBloodPressureInstance), len(tempInstance), len(humidInstance), len(gasInstance))
    #
    # #
    # # some.data = maxSize
    # # some.date = randomDate("2019-01-01 01:30", "2019-04-27 04:50", random.random())
    # # some.owner_id = 1
    # # some.sensortype = "", len(tempInstance), len(humidInstance), len(gasInstance)
    # # some.save()
    #
    # k = 0
    # l = 0
    # for i in range(3*maxSize):
    #     if len(tempInstance) < maxSize:
    #         if i >= len(tempInstance):
    #             tempInstance.append(SensorData.objects.filter(sensortype="Temp").order_by('-id')[0])
    #     if len(humidInstance) < maxSize:
    #         if i >= len(humidInstance):
    #             humidInstance.append(SensorData.objects.filter(sensortype="Humid").order_by('-id')[0])
    #     if len(gasInstance) < maxSize:
    #         l = 2
    #         if i >= len(gasInstance):
    #             gasInstance.append(SensorData.objects.filter(sensortype="Gas").order_by('-id')[0])
    #     if len(systolicBloodPressureInstance) < 3*maxSize:
    #         if i >= len(systolicBloodPressureInstance):
    #             systolicBloodPressureInstance.append(HealthSensorData.objects.filter(sensortype="Systolic_Blood_Pressure").order_by('-id')[0])
    #     if len(bodyTempInstance) < 3*maxSize:
    #
    #         if i >= len(bodyTempInstance):
    #             bodyTempInstance.append(HealthSensorData.objects.filter(sensortype="Body_Temp").order_by('-id')[0])
    #
    #     if len(diastolicBloodPressureInstance) < 3*maxSize:
    #         k = 1
    #         if i >= len(diastolicBloodPressureInstance):
    #
    #             diastolicBloodPressureInstance.append(HealthSensorData.objects.filter(sensortype="Diastolic_Blood_Pressure").order_by('-id')[0])
    #
    #
    #
    #
    #
    # person = [['id', 'owner_id', 'sensortype', 'data', 'date','attached_status', 'triggered', 'body_temp', 'syst_pres', 'dias_pres' ]]
    # mergedlist = sorted((tempInstance + humidInstance + gasInstance), key = lambda x: x.id)
    # for i in range(3*maxSize):
    #     person.append([mergedlist[i].id, mergedlist[i].owner_id, mergedlist[i].sensortype, mergedlist[i].data,
    #                    mergedlist[i].date, mergedlist[i].attached_status, mergedlist[i].triggered,
    #                    bodyTempInstance[i].data, systolicBloodPressureInstance[i].data, diastolicBloodPressureInstance[i].data])
    # csv.register_dialect('myDialect',
    #                      quoting=csv.QUOTE_ALL,
    #                      skipinitialspace=True)
    #
    # with open('data.csv', 'w') as f:
    #     writer = csv.writer(f, dialect='myDialect')
    #     for row in person:
    #         writer.writerow(row)
    #
    # f.close()
    #
    # df = pd.read_csv('data.csv', parse_dates=True, index_col=0)
    #
    def get(self, request):
        # do something with 'GET' method
        return Response("")

class DeleteHealthSensorDataView(APIView):
    serializer_class = HealthSensorDataSerializer

    def get(self, request):
        queryset = HealthSensorData.objects.all().delete()


def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))

def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y-%m-%d %H:%M', prop)
class CreateHealthSensorData(APIView):
    def get(self, request):
        # do something with 'GET' method
    #     return Response("some data")

    # for i in range(100):
    #     t = randomDate("2019-01-01 01:30", "2019-04-27 04:50", random.random())

    #     instance = HealthSensorData(owner_id=1, sensortype="Body_Temp", data=(round(random.uniform(36.5, 37.1), 1)),
    #                                 date=t)
    #     # instance.data = "",39.2
    #     # instance.sensortype = type(instance.data) , instance.data
    #     print(instance.data)

    #     instance.save()
    #     instance = HealthSensorData(owner_id=1, sensortype="Systolic_Blood_Pressure", data=random.randint(105, 120),
    #                                 date=t)
    #     instance.save()
    #     instance = HealthSensorData(owner_id=1, sensortype="Diastolic_Blood_Pressure", data=random.randint(70, 80),
    #                                 date=t)
    #     instance.save()
        print("ok")

 
class HealthSensorDataView(APIView):
    serializer_class = HealthSensorDataSerializer

    def get(self, request):
        queryset=HealthSensorData.objects.all()
        items = HealthSensorDataSerializer(queryset, many=True)
        return Response(items.data)
    def post(self, request):
        # print(request)
        # print("Date:"+request.data['date'])
        request.data['date'] = (datetime.now()+timedelta(hours=6)).strftime('%Y-%m-%dT%H:%M:%S')
        # print("Date:"+request.data['date'])

        serializer = HealthSensorDataSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
