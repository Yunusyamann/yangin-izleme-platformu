import csv
import requests
from .models import FirePoint
from io import StringIO
from celery import shared_task

NASA_URL = "https://firms.modaps.eosdis.nasa.gov/api/country/csv/323bb12c550fa2b8f247559865c483a6/VIIRS_SNPP_NRT/TUR/10/2025-07-20"

@shared_task
def fetch_fire_data():
    response = requests.get(NASA_URL)
    response.encoding = 'utf-8'
    data = StringIO(response.text)
    reader = csv.DictReader(data)
    FirePoint.objects.all().delete()  # Eski verileri temizle
    for row in reader:
        FirePoint.objects.create(
            latitude=float(row['latitude']),
            longitude=float(row['longitude']),
            bright_ti4=float(row['bright_ti4']),
            acq_date=row['acq_date'],
            acq_time=row['acq_time'],
            confidence=row['confidence'],
            frp=float(row['frp']),
            daynight=row['daynight'],
        )
