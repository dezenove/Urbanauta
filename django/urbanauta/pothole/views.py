from django.http import HttpResponse
from django.template import RequestContext
from django.core import serializers # for models of django
from django.utils import simplejson # for dictionary(json)
from django.shortcuts import render_to_response
from django.contrib.gis.shortcuts import render_to_kml

from models import Pothole

def index(request):
    return render_to_response('pothole/index.html', {})

def kml(request):
    potholes = Pothole.objects.kml()
    return render_to_kml("pothole/pothole.kml", {'potholes' : potholes}, context_instance=RequestContext(request))

def json(request):
    potholes = Pothole.objects.geojson()
    json = serializers.serialize('json', potholes)
    return HttpResponse(json, mimetype='application/json')

def geojson(request):
    potholes = Pothole.objects.geojson()
    json = []
    for pothole in potholes:
        json.append({
            u'name' : u'Buraco',
            u'description' : u'<b>Descricao:</b> ' + pothole.description,
            u'point' : simplejson.loads(pothole.geojson),
        })
    return HttpResponse(simplejson.dumps(json), mimetype='application/json')

def add(request):
    import pdb
    pdb.set_trace()
    if request.method == 'GET':
        print 'GET'
    elif request.method == 'POST':
        print 'POST'
    return HttpResponse(request.method)