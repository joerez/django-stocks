from django.shortcuts import render

# Create your views here.
def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get('https://cloud.iexapis.com/stable/stock/' + ticker + '/quote/?token=pk_273fa449cb194ac1884930b5938ab43b')
        
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': 'enter a ticker symbol above'})





def about(request):
    return render(request, 'about.html', {})