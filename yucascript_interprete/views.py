from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from backend.parser import Parser
import json
import traceback

# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

def index(request):
    return render(request, 'yucascript_interprete/index.html')

@csrf_exempt
def validar(request):
    if request.method == "POST":
        
        data = request.body.decode('utf-8')
        print(str(data))
        parser = Parser()
        try:
            res = parser.parse(str(data))
            return JSONResponse("Compilación exitosa", status=200)
        except:
            return JSONResponse("Error de sintaxis: \n"+traceback.format_exc()[650:],status=200)