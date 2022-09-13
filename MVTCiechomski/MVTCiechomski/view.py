from django.http import HttpResponse
from django.template import loader
from AppFamilia.models import Familia

def familia(self):
    plantilla = loader.get_template('index.html')
    familiar = f'Familia: {familia.nombre} edad: {familia.edad} fecha: {familia.fecha}'
    return HttpResponse(familiar)