from django.shortcuts import render
from django.views.generic import View, ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse, HttpResponseForbidden
from .models import JsonEndpoint, AuthEndpoint, MockObjectClass, MockObject
from django.http import Http404
from django.utils import simplejson


class IndexView(ListView):
    #template_name = "index.html"
    model = JsonEndpoint


class DetailView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(DetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        
        if not slug:
            raise Http404

        try:
            endpoint = JsonEndpoint.objects.get(slug=slug)
        except JsonEndpoint.DoesNotExist:
            raise Http404

        return HttpResponse(simplejson.dumps(endpoint.blob), mimetype="application/json")

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        
        if not slug:
            raise Http404

        try:
            endpoint = JsonEndpoint.objects.get(slug=slug)
        except JsonEndpoint.DoesNotExist:
            raise Http404

        endpoint.blob = simplejson.loads(request.body)
        endpoint.save()

        return HttpResponse()


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


class MockObjectView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(MockObjectView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        class_name = self.kwargs['class_name']
        object_id = self.kwargs['object_id']
        
        if not class_name:
            raise Http404

        mock_object_class = MockObjectClass.objects.get(class_name=class_name)

        matching_objects = None
        try:
            if not object_id:
                matching_objects = MockObject.objects.all(mock_class=mock_object_class)
                return HttpResponse(simplejson.dumps([mock_object.blob for mock_object in matching_objects]), mimetype="application/json")
            else:
                matching_object = MockObject.objects.get(object_id=object_id)
                return HttpResponse(simplejson.dumps(matching_object.blob), mimetype="application/json")
        except MockObject.DoesNotExist:
            raise Http404


    @csrf_exempt
    def post(self, request, *args, **kwargs):
        class_name = self.kwargs['class_name']
        object_id = self.kwargs['object_id']
        
        if not class_name and object_id:
            raise Http404

        mock_object_class = MockObjectClass.objects.get(class_name=class_name)

        matching_object = None
        try:
            matching_object = MockObject.objects.get(object_id=object_id)
        except MockObject.DoesNotExist:
            matching_object = MockObject()
            matching_object.object_id = object_id
            matching_object.mock_class = mock_object_class

        matching_object.blob = simplejson.loads(request.body)
        matching_object.save()

        return HttpResponse()
