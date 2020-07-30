from rest_framework.views import APIView
from rest_framework.response import Response

from apis.api_controller import Controller

# ------------------------------------------------------------------------------
class weather(APIView):

    def get(self, request):
        city = request.query_params['city']
        period = request.query_params['period']
        api_cntrl = Controller(city, period)

        data = {}
        try:
            data = api_cntrl.weather_info()
            return Response(data, status=200, template_name=None, headers=None, content_type=None)
        except:
            return Response(data, status=400, template_name=None, headers=None, content_type=None)
