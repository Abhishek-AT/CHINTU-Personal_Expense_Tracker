from django.shortcuts import render
from .models import Transaction
from account.models import User
from django.http import HttpResponse

# Create your views here.

def transactionreview(request):
    transaction_list= Transaction.objects.filter(request.id).order_by('-timestamp')[:30]
    return HttpResponse(transaction_list)

def addtransaction(request):
    