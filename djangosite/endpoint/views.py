from django.shortcuts import render
from django.views.generic import View, ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseForbidden
from .models import JsonEndpoint, AuthEndpoint
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


class AuthView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(AuthView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        
        if not slug:
            raise Http404

        try:
            endpoint = AuthEndpoint.objects.get(slug=slug)
        except AuthEndpoint.DoesNotExist:
            raise Http404

        if not endpoint.enabled:
            return HttpResponseForbidden()

        return HttpResponse()

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        
        if not slug:
            raise Http404

        try:
            endpoint = AuthEndpoint.objects.get(slug=slug)
        except AuthEndpoint.DoesNotExist:
            raise Http404

        endpoint.enabled = False
        endpoint.save()

        return HttpResponse()
