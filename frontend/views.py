from django.shortcuts import render

import requests

# Create your views here.
def index(request):
    try:
        response = requests.get('https://api.ipify.org/?format=json')
        if response.status_code == 200:
            data = response.json()  # {'ip': 'x.x.x.x'}
            return render(request, 'frontend/home.html', data)
        else:
            return render(request, 'frontend/home.html', {'error': 'Failed to fetch IP'})
    except requests.exceptions.RequestException as e:
        return render(request, 'frontend/home.html', {'error': str(e)})