from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil


def index4(request):
	# products=Product.objects.all()
	# print(products)
	# n=len(products)
	# nSlides=n//4+ceil((n/4)-(n//4))
	allprods=[]
	catprods=Product.objects.values('category','id')
	#we made cats as set does not contain ambigious values then unique categories in it
	cats={item['category'] for item in catprods}
	for cat in cats:
		#compare category woth categories in cat and filter the same category product from products
		prod=Product.objects.filter(category=cat)
		n=len(prod)
		nSlides=n//4+ceil((n/4)-(n//4))
		allprods.append([prod,range(1,nSlides),nSlides])
	#params={'no_of_slides':nSlides,'range':range(1,nSlides),'products':products}
	#allprods=[[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
	params={'allprods':allprods}
	return render(request,'shop/index4.html',params)

def about(request):
	return render(request,'shop/about.html')

def contact(request):
	if request.method=="POST":
		name=request.POST.get('name','')
		email=request.POST.get('email','')
		desc=request.POST.get('desc','')
		contact=Contact(name=name,email=email,desc=desc)
		contact.save()
	return render(request,'shop/contact.html')

def tracker(request):
	return render(request,'shop/tracker.html')

def search(request):
	return render(request,'shop/index4.html')

def productview(request,myid):
	product=Product.objects.filter(id=myid)
	
	return render(request,'shop/productview.html',{'product':product[0]})


def checkout(request):
	if request.method=="POST":
		name=request.POST.get('name','')
		email=request.POST.get('email','')
		address=request.POST.get('address','')
		city=request.POST.get('city','')
		state=request.POST.get('state','')
		zip_code=request.POST.get('zip_code','')
		contact=Contact(name=name,email=email,desc=desc)
