from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json
    # pk_273fa449cb194ac1884930b5938ab43b
    api_request = requests.get('https://cloud.iexapis.com/stable/stock/aapl/quote/latestPrice?token=pk_273fa449cb194ac1884930b5938ab43b')
    
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..." + e


    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})