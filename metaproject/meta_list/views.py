from django.shortcuts import render
from meta_list.models import website
from django.shortcuts import render_to_response, RequestContext, HttpResponse

# Create your views here.
def view_meta(request):
	context = RequestContext(request)

	objects = website.objects.all()

	return render_to_response('index.html', {'objects' : objects}, context)
