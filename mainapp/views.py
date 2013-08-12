# Create your views here.

from django.shortcuts import render

from mainapp.models import Graph


def home(request):
	return render(request, 'home.html', {})


def graph(request, graph_id):
	graph = Graph.objects.get(id=int(graph_id))
	return render(request, 'home.html', {'graph': graph})
