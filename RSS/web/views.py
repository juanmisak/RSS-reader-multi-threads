from django.shortcuts import render

# Create your views here.
# Create your views here.
import json
from django.db import transaction
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render_to_response]

def index(request):
    data = {}

    return render_to_response("home.html", data)
