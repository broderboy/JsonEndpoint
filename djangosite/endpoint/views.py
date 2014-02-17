from django.shortcuts import render
from django.views.generic import View, ListView
from django.http import HttpResponse
from .models import JsonEndpoint
from django.http import Http404
from django.utils import simplejson

class IndexView(ListView):
    #template_name = "index.html"
    model = JsonEndpoint

class DetailView(View):
	def get(self, request, *args, **kwargs):
		slug = self.kwargs['slug']
		
		if not slug:
			raise Http404

		try:
			endpoint = JsonEndpoint.objects.get(slug=slug)
		except JsonEndpoint.DoesNotExist:
			raise Http404

		return HttpResponse(simplejson.dumps(endpoint.blob), mimetype="application/json")