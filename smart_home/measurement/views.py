# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.forms import model_to_dict
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from measurement.models import Measurement, Sensor
from measurement.serializers import MeasurementSerializer, SensorSerializer


class SensorsView(APIView):
    def get(self, request):
        sensor = Sensor.objects.all()
        serializer = SensorSerializer(sensor, many=True)
        return Response(serializer.data)

    def post(self, request):
        post_new = Sensor.objects.create(
            name=request.data['name'],
            description=request.data['description']
        )
        return Response({'post': model_to_dict(post_new)})

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        sensor = Sensor.objects.get(id=pk)
        serializer = SensorSerializer(sensor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'post': model_to_dict(sensor)})
        return Response({'error': 'Ошибка в данных'})

class MeasurementView(APIView):
    def get(self, request):
        measurement = Measurement.objects.all()
        serializer = MeasurementSerializer(measurement, many=True)
        return Response(serializer.data)

    def post(self, request):
        post_new = Measurement.objects.create(
            temperature=request.data['temperature'],
            id_sensor=request.data['id_sensor']
        )
        return Response({'post': model_to_dict(post_new)})

class SensorView(RetrieveAPIView):
    def get(self, request, pk):
        sensor = Sensor.objects.get(id=pk)
        serializer = SensorSerializer(sensor)
        return Response(serializer.data)