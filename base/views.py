from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Add_Profile,Cameras,FaceImages


@csrf_protect
def loginpage(request):
	if request.method == 'POST':
		username=request.POST.get('username') 
		password=request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request,user)
			return redirect('Statics')
		else:
			messages.error(request,'cerdentials does not match')
	context={}
	return render (request,'login.html',context)
	# return HttpResponse ('login.html')

    
    
def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def Statics(request):
	return render(request,'statics.html')


@login_required(login_url='login')
def add_profile(request):
	form= Add_Profile()
	form1 = FaceImages(request.FILES)
	context= {'form':form, 'form1':form1 }
	if request.method == 'POST':
		CNIC=Add_Profile.objects.filter(percnic=request.POST.get('Pcnic'))
		
		if (request.POST.get('Pcnic') == None ):
			return render(request,'add_profile.html',context)

		else:
			if CNIC:
				msg=("Employee Already Exist ")
				messages.error(request,msg)
				return render(request,'add_profile.html',context)
			else:
				print(request.POST)
				print(request.FILES)
		
				form.pernme=request.POST.get('Pname') 
				form.percnic=request.POST.get('Pcnic')
				form.perrnk=request.POST.get('Prnk')
				form.perposition=request.POST.get('Ppos')
				form.perroomno=request.POST.get('Prom')
				form.perwrkhr=request.POST.get('Pwrkhr')
				form.perwrkdys=request.POST.get('PWrkds')
				form.pertype=request.POST.get('PType')

				form1.facecnic=request.POST.get('Pname')
				# for i in request.POST.get('ProfImage'):  
				# 	print(i)
				# form1.faceimgpath1= request.POST.get('profImage')

				form.save()
				form1.save()
				return render(request,'add_profile.html',context)
	else:
		
		return render(request,'add_profile.html',context)


@login_required(login_url='login')
def add_camera(request):
	form= Cameras()
	context= {'form':form}
	if request.method == 'POST':
		CID=Cameras.objects.filter(camid=request.POST.get('camid'))
		
		if (request.POST.get('CamID') == None ):
			return render(request,'add_camera.html',context)

		else:
			if CID:
				msg=("Employee Already Exist ")
				messages.error(request,msg)
				return render(request,'add_camera.html',context)
			else:
				print(request.POST)
		
				form.camid=request.POST.get('CamID') 
				form.camip=request.POST.get('CamIP')
				form.camloc=request.POST.get('CamLoc')
				form.cammotion=request.POST.get('CamMotion')
				form.camdetect=request.POST.get('CamDetect')
				form.save()
				return render(request,'add_camera.html',context)
	else:
		
		return render(request,'add_camera.html',context)

		
		
	