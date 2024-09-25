from django.urls import path

from measurement.views import SensorsView, MeasurementView, SensorView

urlpatterns = [
    path('api/sensors/', SensorsView.as_view()),     # TODO: зарегистрируйте необходимые маршруты
    path('api/sensors/<int:pk>/', SensorsView.as_view()),
    path('api/measurements/', MeasurementView.as_view()),
    path('api/sensor/<int:pk>/', SensorView.as_view()),
]