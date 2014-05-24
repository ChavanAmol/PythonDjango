from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hello world! Link to <a href ='/rango/about'> About </a> page.")

def about(request):
	return HttpResponse("This is about page. Here is link to <a href = '/rango/'> Index </a> page.")