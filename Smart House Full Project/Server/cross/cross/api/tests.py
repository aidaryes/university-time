from rest_framework.test import APITestCase
from rest_framework import status
from datetime import datetime, date
from .models import Panel, OneHourElectricity

class PanelTestCase(APITestCase):
    def setUp(self):
        Panel.objects.create(brand="Areva", serial="AAAA1111BBBB2222", latitude=12.345678, longitude=98.7655432)
        OneHourElectricity.objects.create(id='1', panel=Panel.objects.all()[0], kilo_watt="20", date_time=datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p'))
        OneHourElectricity.objects.create(id='2', panel=Panel.objects.all()[0], kilo_watt="11", date_time=datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p'))
        OneHourElectricity.objects.create(id='3', panel=Panel.objects.all()[0], kilo_watt="255", date_time=datetime.strptime('Jun 2 2005  1:33PM', '%b %d %Y %I:%M%p'))
        OneHourElectricity.objects.create(id='4', panel=Panel.objects.all()[0], kilo_watt="1", date_time=datetime.strptime('Jun 2 2005  1:33PM', '%b %d %Y %I:%M%p'))
        OneHourElectricity.objects.create(id='5', panel=Panel.objects.all()[0], kilo_watt="454", date_time=datetime.strptime('Jun 3 2005  1:33PM', '%b %d %Y %I:%M%p'))

    def test_panel_listing(self):
        response = self.client.get('/panel/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_panel_get(self):
        response = self.client.get('/panel/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["serial"], "AAAA1111BBBB2222")

    def test_analysis_get(self):
        response = self.client.get('/panel/1/analytics/day/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['average'], 454)

