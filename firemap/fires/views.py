from django.shortcuts import render
from .models import FirePoint
from django.http import JsonResponse

def map_view(request):
    return render(request, 'fires/map.html')

def firepoints_api(request):
    qs = FirePoint.objects.all()
    data = [
        {
            "lat": f.latitude,
            "lon": f.longitude,
            "acq_date": f.acq_date,
            "confidence": f.confidence,
            "frp": f.frp,
            "daynight": f.daynight,
        }
        for f in qs
    ]
    return JsonResponse(data, safe=False)
