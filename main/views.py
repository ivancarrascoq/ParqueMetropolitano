#csv
import csv
#from models import ExportarEmbalseV
#from models import ExportarEstanqueV
#from models import ExportarEToV

#
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from models import *
#from models import EmbalseTest
#from models import EstanqueTest
##views
#from models import NivelEmbalseV
#from models import NivelEstanqueV  
#pmet
#from models import LluviaAcV
#from models import TemperaturaV
#from models import TempMaxV
#from models import TempMinV
#from models import PresionV
#from models import HumedadV
#from models import RocioV
#from models import HumMinV
#from models import HumMaxV
#from models import RadiacionV
#from models import PresionV
#from models import RadMaxV
#from models import RadMinV
#from models import VientoV
#from models import ParV
#from models import ParMaxV
#from models import PrecipitacionV
#from models import ETo
#from models import EToV
#from models import TempRocioV
##from models import CaudalEmbalseV
##from models import CaudalEstanqueV
#from models import SensacionTermicaT
#from models import TendenciaV
#from models import VientoVelMed12hV
#from models import VientoDir12hV

from datetime import datetime
import datetime
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
#import pdb; pdb.set_trace()
# Create your views here.


def index(request):
    return HttpResponse('<h1>Sparus</h1>')
    print "test..."

def pmet(request):
    print 'iniciando'
    #    hour = '12:30pm'#    height = 30.2#    id = 12#    embalse = EmbalseTest.objects.all()
    embalse = NivelEmbalseV.objects.last
    try:
      caudal_em = embalse().caudal
    except:
      caudal_em = 'NN'
    em_percent = float(embalse().nivel_m3) / float('16331.3') * 100
    estanque = NivelEstanqueV.objects.last
    caudal_es = estanque().caudal

    es_percent = float(estanque().nivel_m3) / float('2694.0') * 100
    emt = EmbalseTest.objects.order_by('-fecha')[:144]
    actual = emt[0]
########
    actual_144 = dict()

    try:
      actual_144['p_tendencia'] = TendenciaV.objects.order_by('-fecha')[0].tendencia
    except:
      actual_144['p_tendencia'] = 'NN'

    actual_144['es_alt'] = NivelEstanqueV.objects.order_by('-fecha')[0].nivel_m #float((3750 - float(NivelEstanqueV.objects.order_by('-fecha')[0].distancia_mm))/1000)
    actual_144['em_alt'] = NivelEmbalseV.objects.order_by('-fecha')[0].nivel_m #float((5000 - float(NivelEmbalseV.objects.order_by('-fecha')[0].distancia_mm))/1000)
    actual_144['tmax'] = 0
    actual_144['tmin'] = actual.temperatura
    actual_144['hmax'] = 0
    actual_144['hmin'] = actual.humedad
    actual_144['rmax'] = 0
    actual_144['parmax'] = 0
    tempmax = TempMaxV.objects.last()
    actual_144['tmax'] = tempmax.temperatura
    actual_144['tmaxh'] = tempmax.fecha
    tempmin = TempMinV.objects.last()
    actual_144['tmin'] = tempmin.temperatura
    actual_144['tminh'] = tempmin.fecha
    hummax = HumMaxV.objects.last()
    actual_144['hmax'] = hummax.humedad
    actual_144['hmaxh'] = hummax.fecha
    hummin = HumMinV.objects.last()
    actual_144['hmin'] = hummin.humedad
    actual_144['hminh'] = hummin.fecha
    radmax = RadMaxV.objects.last()
    actual_144['rmax'] = radmax.radiacion
    actual_144['rmaxh'] = radmax.fecha
    parmax = ParMaxV.objects.last()
    actual_144['parmax'] = parmax.par
    actual_144['parmaxh'] = parmax.fecha

    actual_144['lluvia'] = actual.lluvia
    actual_144['lluvia_intensidad'] = float(actual_144['lluvia']) * 12

    actual_144['i_calor'] = SensacionTermicaT.objects.order_by('-fecha')[0].calor
    actual_144['i_frio'] = SensacionTermicaT.objects.order_by('-fecha')[0].frio

    print actual_144
    presion_nm = float(actual.presion) * 1.0875
    viento_vel = round(float(VientoVelMed12hV.objects.first().viento_vel_med12h),1)
    viento_simbolo = VientoDir12hV.objects.order_by('cantidad').last().viento_simbolo
    viento_grado = VientoDir12hV.objects.order_by('cantidad').last().viento_grado + 25 - 90 + 180
    viento_raf = round(float(actual.viento_raf)*3.6,1)
    viento_dir = actual.viento_dir + 25 - 90
    viento = {'vel': viento_vel, 'simbolo': viento_simbolo, 'raf': viento_raf, 'dir': viento_dir, 'grado': viento_grado}
    precip = PrecipitacionV.objects.last
    eto = EToV.objects.last

    print 'terminando consultas'
    context = { 'embalse': embalse, 'estanque': estanque, 'actual_144': actual_144,
    'presion_nm': presion_nm,
    'viento': viento,
    'precip': precip,
    'eto': eto, 
    'caudal_em': caudal_em, 'caudal_es': caudal_es, 
    'es_percent': es_percent, 'em_percent': em_percent, 'actual':actual  }

    print 'enviando datos'
    return render(request, 'index.html', context)
#    print 'cargando index.html'


def simbolo(viento_dir):
    if viento_dir == 0:
        viento_simbolo = 'N'
    elif (viento_dir > 0 and viento_dir < 45):
        viento_simbolo = 'NNE'
    elif viento_dir == 45:
        viento_simbolo = 'NE'
    elif (viento_dir > 45 and viento_dir < 90):
        viento_simbolo = 'ENE'
    elif viento_dir == 90:
        viento_simbolo = 'E'
    elif (viento_dir > 90 and viento_dir < 135):
        viento_simbolo = 'ESE'
    elif (viento_dir >= 135 and viento_dir < 180):
        viento_simbolo = 'SSE'
    elif viento_dir == 180:
        viento_simbolo = 'S'
    elif (viento_dir > 180 and viento_dir < 225):
        viento_simbolo = 'SSW'
    elif (viento_dir >= 225 and viento_dir < 270):
        viento_simbolo = 'WSW'
    elif viento_dir == 270:
        viento_simbolo = 'W'   
    elif (viento_dir > 270 and viento_dir < 315):
        viento_simbolo = 'WNW'  
    elif (viento_dir >= 315 and viento_dir < 360):
        viento_simbolo = 'NNW'  
    else:
        viento_simbolo = 'XXX'
    return(viento_simbolo)

#def graf(x):
#      embalse = EmbalseTest.objects.all().order_by('-fecha')[:144]
#      a1 = '<div id="graphdiv-' + x + '" style="clear:both;width:500px;height:200px;"></div>'
#      a2 = '<script type="text/javascript">g = new Dygraph(document.getElementById("graphdiv-' + x + '"),"fecha,'+x+'\n"'
#      for i in embalse:
#        a3 = a3 + '"' + i.fecha + ',' + i.temperatura + '\n"'
#      a3 = a3 + ','

def day(request):
    nivel_em = NivelEmbalseV.objects.all().order_by('-fecha')[:144]
    nivel_es = NivelEstanqueV.objects.all().order_by('-fecha')[:144]
#    eto = ETo.objects.all().order_by('-fecha')[:144]
    eto = EToV.objects.all().order_by('-fecha')[:144]
    embalse = EmbalseTest.objects.all().order_by('-fecha')[:144]
    estanque = EstanqueTest.objects.all().order_by('-fecha')[:144]
    temperatura = TemperaturaV.objects.all().order_by('-fecha')[:144]
    humedad = HumedadV.objects.all().order_by('-fecha')[:144]
    rocio = RocioV.objects.all().order_by('-fecha')[:144]     
    radiacion = RadiacionV.objects.all().order_by('-fecha')[:144]
    par = ParV.objects.all().order_by('-fecha')[:144]
    presion = PresionV.objects.all().order_by('-fecha')[:144]
    viento = VientoV.objects.all().order_by('-fecha')[:144]
    lluvia = PrecipitacionV.objects.all().order_by('-fecha')[:144]    
    lluvia_ac = LluviaAcV.objects.all().order_by('-fecha')[:144]
    context = { 'nivel_em': nivel_em,'nivel_es': nivel_es,'embalse': embalse, 'estanque': estanque, 'eto': eto, 'temperatura': temperatura, 'humedad':humedad, 'rocio':rocio, 'radiacion':radiacion, 'par':par, 'presion':presion, 'viento':viento, 'lluvia':lluvia, 'lluvia_ac':lluvia_ac }
    return render(request, 'day.html', context)

def week(request):
    nivel_em = NivelEmbalseV.objects.all().order_by('-fecha')[:1008]
    nivel_es = NivelEstanqueV.objects.all().order_by('-fecha')[:1008]
    eto = EToV.objects.all().order_by('-fecha')[:1008]
    embalse = EmbalseTest.objects.all().order_by('-fecha')[:1008]
    estanque = EstanqueTest.objects.all().order_by('-fecha')[:1008]
    temperatura = TemperaturaV.objects.all().order_by('-fecha')[:1008]
    humedad = HumedadV.objects.all().order_by('-fecha')[:1008]
    rocio = RocioV.objects.all().order_by('-fecha')[:1008]
    radiacion = RadiacionV.objects.all().order_by('-fecha')[:1008]
    par = ParV.objects.all().order_by('-fecha')[:1008]
    presion = PresionV.objects.all().order_by('-fecha')[:1008]
    viento = VientoV.objects.all().order_by('-fecha')[:1008]
    lluvia = PrecipitacionV.objects.all().order_by('-fecha')[:1008]
    lluvia_ac = LluviaAcV.objects.all().order_by('-fecha')[:1008]
    context = { 'nivel_em': nivel_em,'nivel_es': nivel_es,'embalse': embalse, 'estanque': estanque, 'eto': eto, 'temperatura': temperatura, 'humedad':humedad, 'rocio':rocio,'radiacion':radiacion, 'par':par, 'presion':presion, 'viento':viento, 'lluvia':lluvia, 'lluvia_ac': lluvia_ac }
#    context = { 'nivel_em': nivel_em,'nivel_es': nivel_es,'embalse': embalse, 'estanque': estanque, 'eto': eto }
    return render(request, 'week.html', context)

def month(request):
    nivel_em = NivelEmbalseV.objects.all().order_by('-fecha')[:4320:3]
    nivel_es = NivelEstanqueV.objects.all().order_by('-fecha')[:4320:3]
    eto = EToV.objects.all().order_by('-fecha')[:4320:3]
    embalse = EmbalseTest.objects.all().order_by('-fecha')[:4320:3]
    estanque = EstanqueTest.objects.all().order_by('-fecha')[:4320:3]
    temperatura = TemperaturaV.objects.all().order_by('-fecha')[:4320:3]
    humedad = HumedadV.objects.all().order_by('-fecha')[:4320:3]
    rocio = RocioV.objects.all().order_by('-fecha')[:4320:3]
    radiacion = RadiacionV.objects.all().order_by('-fecha')[:4320:3]
    par = ParV.objects.all().order_by('-fecha')[:4320:3]
    presion = PresionV.objects.all().order_by('-fecha')[:4320:3]
    viento = VientoV.objects.all().order_by('-fecha')[:4320:3]
    lluvia = PrecipitacionV.objects.all().order_by('-fecha')[:4320:3]
    lluvia_ac = LluviaAcV.objects.all().order_by('-fecha')[:4320:3]
    context = { 'nivel_em': nivel_em,'nivel_es': nivel_es,'embalse': embalse, 'estanque': estanque, 'eto': eto, 'temperatura': temperatura, 'humedad':humedad, 'rocio':rocio,'radiacion':radiacion, 'par':par, 'presion':presion, 'viento':viento, 'lluvia':lluvia, 'lluvia_ac': lluvia_ac }
#    context = { 'nivel_em': nivel_em,'nivel_es': nivel_es,'embalse': embalse, 'estanque': estanque, 'eto': eto }
    return render(request, 'month.html', context)

def xls(request):
    return render(request, 'xls.html')#, context)

def em_csv(request):
    time0 = EmbalseTest.objects.last().fecha
    time = time0.strftime("%H%M-%d%m%Y")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="embalse'+str(time)+'.csv"'
    writer = csv.writer(response)
    writer.writerow(['FECHA','LOC','DIA','MES','ANO','HORA','MINUTO','TEMP','PROCIO','HR','PAT','PATNM','IC','VVTO','DVTO','RSOL','RFA','PP','IPP','VOL','TLLV'])
    em = ExportarEmbalseV.objects.order_by('-FECHA')[:144]
    for j in em:
        writer.writerow([j.FECHA, j.LOC, j.DIA, j.MES, j.ANO, j.HORA, j.MINUTO, j.TEMP, j.PROCIO, j.HR, j.PAT, j.PATNM, j.IC, j.VVTO, j.DVTO, j.RSOL, j.RFA, j.PP, j.IPP, j.VOL, j.TLLV])
    return response

def em7_csv(request):
    time0 = EmbalseTest.objects.last().fecha
    time = time0.strftime("%H%M-%d%m%Y")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="embalse7-'+str(time)+'.csv"'
    writer = csv.writer(response)
    writer.writerow(['FECHA','LOC','DIA','MES','ANO','HORA','MINUTO','TEMP','PROCIO','HR','PAT','PATNM','IC','VVTO','DVTO','RSOL','RFA','PP','IPP','VOL','TLLV'])
    em = ExportarEmbalseV.objects.order_by('-FECHA')[:1008]
    for j in em:
        writer.writerow([j.FECHA, j.LOC, j.DIA, j.MES, j.ANO, j.HORA, j.MINUTO, j.TEMP, j.PROCIO, j.HR, j.PAT, j.PATNM,j.IC, j.VVTO, j.DVTO, j.RSOL, j.RFA, j.PP, j.IPP, j.VOL, j.TLLV])
    return response

def em30_csv(request):
    time0 = EmbalseTest.objects.last().fecha
    time = time0.strftime("%H%M-%d%m%Y")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="embalse30-'+str(time)+'.csv"'
    writer = csv.writer(response)
    writer.writerow(['FECHA','LOC','DIA','MES','ANO','HORA','MINUTO','TEMP','PROCIO','HR','PAT','PATNM','IC','VVTO', 'DVTO','RSOL','RFA','PP','IPP','VOL','TLLV'])
    em = ExportarEmbalseV.objects.order_by('-FECHA')[:4320]
    for j in em:
        writer.writerow([j.FECHA, j.LOC, j.DIA, j.MES, j.ANO, j.HORA, j.MINUTO, j.TEMP, j.PROCIO, j.HR, j.PAT, j.PATNM,j.IC, j.VVTO, j.DVTO, j.RSOL, j.RFA, j.PP, j.IPP, j.VOL, j.TLLV])
    return response

def em90_csv(request):
    time0 = EmbalseTest.objects.last().fecha
    time = time0.strftime("%H%M-%d%m%Y")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="embalse90-'+str(time)+'.csv"'
    writer = csv.writer(response)
    writer.writerow(['FECHA','LOC','DIA','MES','ANO','HORA','MINUTO','TEMP','PROCIO','HR','PAT','PATNM','IC','VVTO', 'DVTO','RSOL','RFA','PP','IPP','VOL','TLLV'])
    em = ExportarEmbalseV.objects.order_by('-FECHA')[:12960]
    for j in em:
        writer.writerow([j.FECHA, j.LOC, j.DIA, j.MES, j.ANO, j.HORA, j.MINUTO, j.TEMP, j.PROCIO, j.HR, j.PAT, j.PATNM,j.IC, j.VVTO, j.DVTO, j.RSOL, j.RFA, j.PP, j.IPP, j.VOL, j.TLLV])
    return response

def es_csv(request):
    time0 = EmbalseTest.objects.last().fecha
    time = time0.strftime("%H%M-%d%m%Y")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="estanque'+str(time)+'.csv"' #agregar +str(tiempo)
    writer = csv.writer(response)
    writer.writerow(['FECHA','LOC','DIA','MES','ANO','HORA','MINUTO','VOL','TLLV'])
    em = ExportarEstanqueV.objects.order_by('-FECHA')[:144]
    for j in em:
        writer.writerow([j.FECHA,j.LOC,j.DIA,j.MES,j.ANO,j.HORA,j.MINUTO,j.VOL,j.TLLV])
    return response

def es7_csv(request):
    time0 = EmbalseTest.objects.last().fecha
    time = time0.strftime("%H%M-%d%m%Y")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="estanque7-'+str(time)+'.csv"' #agregar +str(tiempo)
    writer = csv.writer(response)
    writer.writerow(['FECHA','LOC','DIA','MES','ANO','HORA','MINUTO','VOL','TLLV'])
    em = ExportarEstanqueV.objects.order_by('-FECHA')[:1008]
    for j in em:
        writer.writerow([j.FECHA,j.LOC,j.DIA,j.MES,j.ANO,j.HORA,j.MINUTO,j.VOL,j.TLLV])
    return response

def es30_csv(request):
    time0 = EmbalseTest.objects.last().fecha
    time = time0.strftime("%H%M-%d%m%Y")                      
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="estanque30-'+str(time)+'.csv"' #agregar +str(tiempo)
    writer = csv.writer(response)
    writer.writerow(['FECHA','LOC','DIA','MES','ANO','HORA','MINUTO','VOL','TLLV'])
    em = ExportarEstanqueV.objects.order_by('-FECHA')[:4320]
    for j in em:
        writer.writerow([j.FECHA,j.LOC,j.DIA,j.MES,j.ANO,j.HORA,j.MINUTO,j.VOL,j.TLLV])
    return response

def es90_csv(request):
    time0 = EmbalseTest.objects.last().fecha
    time = time0.strftime("%H%M-%d%m%Y")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="estanque90-'+str(time)+'.csv"' #agregar +str(tiempo)
    writer = csv.writer(response)
    writer.writerow(['FECHA','LOC','DIA','MES','ANO','HORA','MINUTO','VOL','TLLV'])
    em = ExportarEstanqueV.objects.order_by('-FECHA')[:12960]
    for j in em:
        writer.writerow([j.FECHA,j.LOC,j.DIA,j.MES,j.ANO,j.HORA,j.MINUTO,j.VOL,j.TLLV])
    return response


def eto_csv(request):
    time0 = EmbalseTest.objects.last().fecha
    time = time0.strftime("%H%M-%d%m%Y")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="eto'+str(time)+'.csv"'
    writer = csv.writer(response)
    writer.writerow(['fecha','LOC','DIA','MES','ANO','ETOD'])
    em = ExportarEToV.objects.order_by('-fecha')[:1]
    for j in em:
        writer.writerow([j.fecha,j.LOC,j.DIA,j.MES,j.ANO,j.ETOD])
    return response

def eto7_csv(request):
    time0 = EmbalseTest.objects.last().fecha
    time = time0.strftime("%H%M-%d%m%Y")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="eto7-'+str(time)+'.csv"'
    writer = csv.writer(response)
    writer.writerow(['fecha','LOC','DIA','MES','ANO','ETOD'])
    em = ExportarEToV.objects.order_by('-fecha')[:7]
    for j in em:
        writer.writerow([j.fecha,j.LOC,j.DIA,j.MES,j.ANO,j.ETOD])
    return response

def eto30_csv(request):
    time0 = EmbalseTest.objects.last().fecha
    time = time0.strftime("%H%M-%d%m%Y")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="eto30-'+str(time)+'.csv"'
    writer = csv.writer(response)
    writer.writerow(['fecha','LOC','DIA','MES','ANO','ETOD'])
    em = ExportarEToV.objects.order_by('-fecha')[:30]
    for j in em:
        writer.writerow([j.fecha,j.LOC,j.DIA,j.MES,j.ANO,j.ETOD])
    return response

def eto90_csv(request):
    time0 = EmbalseTest.objects.last().fecha
    time = time0.strftime("%H%M-%d%m%Y")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="eto90-'+str(time)+'.csv"'
    writer = csv.writer(response)
    writer.writerow(['fecha','LOC','DIA','MES','ANO','ETOD'])
    em = ExportarEToV.objects.order_by('-fecha')[:90]
    for j in em:
        writer.writerow([j.fecha,j.LOC,j.DIA,j.MES,j.ANO,j.ETOD])
    return response

def nivel(request):
    return(1)
