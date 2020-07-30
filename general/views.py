import requests

from django.contrib import messages
from django.shortcuts import redirect, render

# ------------------------------------------------------------------------------
def index(request):
    if request.user.is_authenticated:
        weather_data = {}
        if request.method == 'POST':
            try:
                response = requests.get(
                    '%s://%s/apis/v1/weather' % (request.scheme, request.META['HTTP_HOST']),
                    params={'city': request.POST['city'],
                            'period': ','.join([request.POST['from_date'], request.POST['to_date']])},
                )

                if response.status_code == 200 and response.json():  # Checking if everything is correct
                    weather_data = response.json()
                    messages.success(request, 'Successfully retrieved data')
                else:
                    messages.warning(request, 'Something went wrong, check input and try reloading')
            except:
                messages.warning(request, 'Something went wrong, try reloading')

        return render(request, 'general/index.html', {'weather_data': weather_data})
    else:
        return redirect('/accounts/login/')
