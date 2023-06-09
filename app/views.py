from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework import status


class ProductCrud(APIView):
    def get(self,request):
        PQS=Product.objects.all()
        PJD=ProductSerializer(PQS,many=True)
        return Response(PJD.data)

    def post(self,request):
        PSMD=ProductSerializer(data=request.data)
        if PSMD.is_valid():
            PSMD.save()
            return Response({'Message':'Product Is Created'})
        return Response({'Failed':'Product Creation Is Failed'})

    def put(self,request):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        UPO=ProductSerializer(PO,data=request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({'Message':'Product Is Updated'})
        return Response({'Failed':'Product Is Not Updated'})