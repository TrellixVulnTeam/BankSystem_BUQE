from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Bank, Customer
from .serializers import BankSerializer, CustomerSerializer
from rest_framework import viewsets
from rest_framework import permissions

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

class BankViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to be viewed or edited.
    """
    queryset = Bank.objects.all().order_by('name')
    serializer_class = BankSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def bank_list(request):
    """
    List all code bank, or create a new bank.
    """
    if request.method == 'GET':
        bank = Bank.objects.all()
        serializer = BankSerializer(bank, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BankSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def bank_detail(request, pk):
    """
    Retrieve, update or delete a code bank.
    """
    try:
        bank = Bank.objects.get(pk=pk)
    except Bank.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BankSerializer(bank)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BankSerializer(bank, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        bank.delete()
        return HttpResponse(status=204)

### api view of bank ###

@api_view(['GET', 'POST'])
def bank_list(request):
    """
    List all code banks, or create a new bank.
    """
    if request.method == 'GET':
        bank = Bank.objects.all()
        serializer = BankSerializer(bank, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


######### Customer ###########


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

@csrf_exempt
def customer_list(request):
    """
    List all code customer, or create a new customer.
    """
    if request.method == 'GET':
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def customer_detail(request, pk):
    """
    Retrieve, update or delete a code customer.
    """
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CustomerSerializer(customer, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        customer.delete()
        return HttpResponse(status=204)

### api view of customer ###

@api_view(['GET', 'POST'])
def customer_list(request):
    """
    List all code customer, or create a new customer.
    """
    if request.method == 'GET':
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

