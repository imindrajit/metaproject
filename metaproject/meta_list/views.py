from django.shortcuts import render
import json
from meta_list.models import website
from django.shortcuts import render_to_response, RequestContext, HttpResponse

# Create your views here.
def view_meta(request):
	context = RequestContext(request)	

	#print json.dumps(response_data);	

	return render_to_response('index.html', {}, context)
	



def view_json(request):
	context = RequestContext(request)

	objects = website.objects.all()

	i=0
	response_data={};

	for obj in objects:
		array={};
		array["id"]=obj.id
		array["link"]=obj.link
		array["title"]=obj.title
		array["timestamp"]=obj.timestamp
		array["meta"]=obj.meta

		response_data[obj.id]=array

	return HttpResponse(json.dumps(response_data), content_type="application/json")