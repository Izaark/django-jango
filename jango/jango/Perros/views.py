from django.shortcuts import render
from django.http import HttpResponse 
import random
def saluda(request):
	return HttpResponse("Hola soy un perro y me llamo fido")
