from django.shortcuts import render
from django.http import HttpResponse
#from models import EmbalseTest

from main.models import EmbalseTest

#from models import HumMaxV
from datetime import datetime
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
from django import template

from django.template import Library, Node



register = template.Library()
@register.filter(name='graf')
@register.filter(name='nivel_em')

def graf(request):
     embalse = EmbalseTest.objects.all().order_by('-fecha')[:144]
#      a1 = '<div id="graphdiv-' + x + '" style="clear:both;width:500px;height:200px;"></div>'
#      a2 = '<script type="text/javascript">g = new Dygraph(document.getElementById("graphdiv'
#      for i in embalse:
#        a3 = a3 + '"' + i.fecha + ',' + i.temperatura + '\n"'
#      a3 = a3 + ','
#     print "funca filter"
     return "nivel 1" + request

def nivel_em(value):
#    embalse = EmbalseTest.objects.all().last
    return value
