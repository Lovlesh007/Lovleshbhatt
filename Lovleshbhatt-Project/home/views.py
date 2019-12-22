from django.shortcuts import render,redirect
from .models import Contact
# Create your views here.
def index(request):
	return render(request,'home/index.html')


def contact(request):
	if request.method =='POST':
		if request.POST['fcname'] and request.POST['fcemail'] and request.POST['fcphone'] and request.POST['fcmessage']:
			ocontact = Contact()  # object of a class contact is created to access their attributes
			ocontact.Name =request.POST['fcname']
			ocontact.Email=request.POST['fcemail']
			ocontact.Phone=request.POST['fcphone']
			ocontact.Message=request.POST['fcmessage']
			ocontact.save()
			return render(request,'home/index.html',{'response':'Your Query has been submitted, We will response You Back regarding your Query.'})
		else:
			return render(request,'home/index.html',{'response':'All Fields must be filled'})
	else:
		return render(request,'home/index.html')


