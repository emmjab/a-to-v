from django.shortcuts import render

# Create your views here.
def index(req):

	return render(req, 'AtoV/index.html')

def app(req):

	return render(req, 'AtoV/app.html')
