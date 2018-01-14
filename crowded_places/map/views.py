from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from pymongo import MongoClient



def index(request):
    template = loader.get_template('map/map_page.html')
    context = {}
    return HttpResponse(template.render(context, request))

def add(request):
    connection = MongoClient("nick1-Lenovo-IdeaPad-Y550P")
    db = connection.crowded_places.doc
    for i in range(10):
        number = str(i)
        place = {'town': "SPb", 'place_name': "place " + number, "lat": 60,"long": 30, "couter": 10 + i*3}
        db.insert(place)
    connection.close()
    return HttpResponse("added <a href='./'>Back</a>")

def search(request):
    text = request.GET.get('text', None)
    connection = MongoClient("nick1-Lenovo-IdeaPad-Y550P")
    db = connection.crowded_places.doc
    #place_name text: { $regex: 'находить'} })
    allDocs = db.find({"place_name": { "$regex": text}})

    connection.close()
    return HttpResponse(render(request, "map/search.html",{"find":allDocs}))
    #return HttpResponse("search " + text)


