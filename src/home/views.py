
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    View,
)
import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import Template


class HomeView(View):
    def get(self, request, *args, **kwargs):
        data = get_object_or_404(Template, pk=1)
        decoded_json = json.loads(data.social)  # from string to json
        context = {
            'data': data,
            'json_data': decoded_json,  # add de result to the context
        }

        template = 'home/index.html'
        return render(request, template, context)


class AjaxHomeView(View):
    def get(self, request, *args, **kwargs):
        data = serializers.serialize('json', Template.objects.filter(id=1))
        return JsonResponse(data, safe=False)# safe when serialized object
