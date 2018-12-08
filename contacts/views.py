from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from contacts.models import Contact


def contacts_list(request):
    return HttpResponse("Deu certo!")