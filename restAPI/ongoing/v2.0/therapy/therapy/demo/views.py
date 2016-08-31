import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.views import View
from rest_framework.response import Response
from .serializers import *

def index(request):
    return HttpResponse("<h1>Demo App index Page</h1>")

class DemoView(View):
    def get(self,request):
        return HttpResponse("<h1>DemoView Class as get method</h1>")

    # def put(self,request):
    #     return HttpResponse("<h1>DemoView Class as post method</h1>")

class ModifiedDemoView(DemoView):
    pass

class demomodel():
    """
    Description for class demo. can be accesed via class.__doc__
    """
    static_variable = 0

    def __init__(self,id,name):
        self.id = id
        self.name = name


def demojsonresponse(request):
    return JsonResponse(json.dumps(demomodel(1,'demo').__dict__), safe=False)

def employees(request):
    emps = Employee.objects.filter(manager_id=1)
    serializer = EmployeeSerializer(emps, many=True)
    return JsonResponse(serializer.data, safe=False)