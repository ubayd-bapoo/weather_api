from django.conf.urls import include, url
from .views import weather

urlpatterns = [
    url(r'^weather', weather.as_view()),
]