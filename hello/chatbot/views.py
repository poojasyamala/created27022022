from django.shortcuts import render
from rest_framework.decorators import api_view
import json
from rest_framework.response import Response
import googlemaps
from dicttoxml import dicttoxml
from chatbot.models import CustomUser
from django.contrib.auth import login, authenticate, logout
from chatbot.utils import register_user
@api_view(["POST"])
def getAddressDetails(request):
    address = request.data
    API_KEY = 'AIzaSyCOD3KvY2DDzEfel-NZ_LKIWXr86EF_EUw'
    gmaps = googlemaps.Client(API_KEY)
    location = address["address"]
    add = gmaps.geocode(location)
    lat = add[0]['geometry']['location']['lat']
    lng = add[0]['geometry']['location']['lng']
    address_response = {"coordinates":{
                         "lat":lat,
                         "lng":lng},
                         "address":address["address"]}
    if address["output_format"] == "json":
        addressDetails = json.dumps(address_response)
    else:
        addressDetails = dicttoxml(address_response, custom_root='root', attr_type = False)
    return Response(addressDetails)
@api_view(["POST"])
def login_user(request):
    details = request.data
    username = details["username"]
    password = details["password"]
    objects = {}
    obj = CustomUser.objects.filter(username=username, password=password)
    if obj:
        objects["username"] = obj.username
        objects["password"] = obj.password
    else:
        objects = "invalid username or password"
    return Response(json.dumps(objects))
@api_view(["GET"])
def login_template(request):
    return render(request, 'login.html')
@api_view(["POST"])
def registerUser(request):
    details = request.data
    if register_user(details):
        return Response("Successfully created")
    else:
        return Response("This user already existed")
