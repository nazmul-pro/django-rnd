from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views.generic import TemplateView
#rest
from rest_framework import status , generics , mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product , Location ,Family ,Transaction 
from .serializers import *  
#end-rest

class ExamList(generics.GenericAPIView):
    template_name = 'exam-list.html'
    def get(self, request):
        return render(request, self.template_name)

class IndexPageView(generics.GenericAPIView):
    template_name = 'home.html'
    def get(self, request):
        return render(request, self.template_name)

class family_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    queryset = Family.objects.all()
    serializer_class = FamilySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class family_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

    queryset = Family.objects.all()
    serializer_class = FamilySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    

class location_list(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class location_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class =  LocationSerializer

class transaction_list(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class transaction_detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class =  TransactionSerializer
