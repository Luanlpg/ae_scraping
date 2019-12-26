from django.shortcuts import render

from .serializers import LogSerializer
from .serializers import ParseSerializer

from .models import LogModel

from .utils import ScrapingService

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.views import status


class ParseView(APIView):
    """=========================================================================\n
    View que lista logs e aciona parser.\n
    ========================================================================="""
    serializer_class = ParseSerializer
    log_serializer_class = LogSerializer

    def get(self, request, format=None):
        serializer = self.log_serializer_class(LogModel.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            crawler = ScrapingService(request.data['url'])
            response = crawler.parse()

            LogModel.objects.create(
                url = request.data['url'],
                success = True
                )
            return Response(f'{response}', status=status.HTTP_201_CREATED)

        except Exception as error:
            LogModel.objects.create(
                url = request.data['url'],
                success = False
                )
            return Response('{ message: "Check url and try again" }', status=status.HTTP_400_BAD_REQUEST)
