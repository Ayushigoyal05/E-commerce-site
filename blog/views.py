from django.shortcuts import render
from django.http import HttpResponse


def index5(request):
	return render(request,'blog/index5.html')



# Create your views here.
