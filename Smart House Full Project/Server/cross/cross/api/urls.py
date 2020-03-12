# api/urls.py

from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers
from api import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^panel/(?P<panelid>\d+)/analytics/$', views.HourAnalyticsView.as_view()),
    url(r'^panel/(?P<panelid>\d+)/analytics/day/$', views.DayAnalyticsView.as_view()),
    url(r'^panel/$', views.PanelView.as_view()),
    url(r'^panel/(?P<panelid>\d+)/$', views.PanelViewID.as_view()),
    url(r'^users/$', views.UserView.as_view()),
    url(r'^users/(?P<userid>\d+)/$', views.UserDataViewID.as_view()),
    url(r'^users/(?P<userid>\d+)/changeAgeCategoryData/$', views.AgeCategoryChangeView.as_view()),
    url(r'^users/(?P<userid>\d+)/changeDiseaseCategoryData/$', views.DiseaseCategoryChangeView.as_view()),

    url(r'^data/$', views.SensorDataView.as_view()),
    url(r'^healthdata/$', views.HealthSensorDataView.as_view()),
    url(r'^healthdata/create/$', views.CreateHealthSensorData.as_view()),
    url(r'^createCSV/$', views.CreateCsv.as_view()),
    url(r'^data/(?P<userid>\d+)/$', views.SensorDataViewID.as_view()),
    url(r'^data/(?P<userid>\d+)/temp/$', views.SensorDataViewIDTemp.as_view()),
    url(r'^data/(?P<userid>\d+)/gas/$', views.SensorDataViewIDGas.as_view()),
    url(r'^data/(?P<userid>\d+)/humid/$', views.SensorDataViewIDHumid.as_view()),
    url(r'^commands/$', views.UserCommandsView.as_view()),
    url(r'^commands/(?P<userid>\d+)/$', views.UserCommandsViewID.as_view()),
    url(r'^commands/(?P<userid>\d+)/temp/$', views.UserCommandsViewTempID.as_view()),
    url(r'^commands/(?P<userid>\d+)/humid/$', views.UserCommandsViewHumidID.as_view()),
    url(r'^commands/(?P<userid>\d+)/gas/$', views.UserCommandsViewGasID.as_view()),
    url(r'^commands/(?P<userid>\d+)/temp/accepted$', views.UserCommandsViewTempOKID.as_view()),
    url(r'^commands/(?P<userid>\d+)/humid/accepted$', views.UserCommandsViewHumidOKID.as_view()),
    url(r'^commands/(?P<userid>\d+)/gas/accepted$', views.UserCommandsViewGasOKID.as_view()),
    url(r'^photos/$', views.PhotoTriggerView.as_view()),
    url(r'^photos/(?P<userid>\d+)/$', views.PhotoTriggerUserView.as_view()),
    url(r'^photos/accepted/(?P<photoid>\d+)/$', views.PhotoAcceptedView.as_view()),
    url(r'^visitors/(?P<userid>\d+)/$', views.VisitorsByIdView.as_view()),
    url(r'^visitors/$', views.VisitorsPost.as_view()),
    #DeleteAllCommandsView
    url(r'^deleteData/2255225252555415$', views.DeleteSensorDataView.as_view()),
    url(r'^deleteCommands/4561984156198/$', views.DeleteAllCommandsView.as_view()),
    #DeleteAllCommandsView
    url(r'^deleteHealthData/$', views.DeleteHealthSensorDataView.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)