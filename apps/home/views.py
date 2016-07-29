from django.shortcuts import render, redirect, HttpResponse
from .models import MarkerIcon
import json

def index(request):
	if not'user_id' in request.session:
		return redirect('/entry')
	else:
		return render(request, 'home/map.html')

def listmenu(request):
	if request.method == "POST":
		title = request.POST["title"]
		description = request.POST["description"]
		eventDay = request.POST["eventDay"]
		eventStart = request.POST["eventStart"]
		eventEnd = request.POST["eventEnd"]
		requirements = request.POST["requirements"]
		lat = request.POST["x"]
		lon = request.POST["y"]

		new_marker = MarkerIcon.objects.create(
			title = title,
			description = description,
			eventDay = eventDay,
			eventStart = eventStart,
			eventEnd = eventEnd,
			requirements = requirements,
			lat = lat,
    		lon = lon)
		setList = MarkerIcon.objects.all()
		results = [ob.as_json() for ob in setList]
		return HttpResponse(json.dumps(results), content_type="application/json")
	setList = MarkerIcon.objects.all()
	results = [ob.as_json() for ob in setList]
	return HttpResponse(json.dumps(results), content_type="application/json")

def test(request):
	if request.method == "POST":
		message = 'something wrong!'
		print message
	return HttpResponse()

def logout(request):
	request.session.clear()
	return redirect('/')

