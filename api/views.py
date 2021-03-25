from django.shortcuts import render
from ranking.models import Score
from ranking.forms import PlayerForm

#API
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ScoreSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class BeefWeekAPI(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Score.objects.all()
        serializer = ScoreSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
