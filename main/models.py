# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class EmbalseTest(models.Model):
    fecha_reg = models.DateTimeField()
   # fecha = models.DateTimeField(blank=True, null=True)
    fecha = models.CharField(max_length=255)
    temperatura = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    humedad = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    puntorocio = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    viento_vel = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    viento_dir = models.IntegerField(blank=True, null=True)
    viento_raf = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    radiacion = models.IntegerField(blank=True, null=True)
    par = models.IntegerField(blank=True, null=True)
    lluvia = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    presion = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    analogo = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    bateria = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    esweb = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'embalse_test'


class EstanqueTest(models.Model):
    fecha_reg = models.DateTimeField()
    fecha = models.DateTimeField(blank=True, null=True)
    analogo = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    bateria = models.DecimalField(max_digits=4, decimal_places=3, blank=True, null=True)
    esweb = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estanque_test'

###### tablas por dia:

class NivelEmbalseV(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    nivel_m3 = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    nivel_m = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    distancia_mm = models.IntegerField()
    caudal =  models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'nivel_embalse_v'

class NivelEstanqueV(models.Model):    
    fecha = models.DateTimeField(primary_key=True)      
    nivel_m3 = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    nivel_m = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    distancia_mm = models.IntegerField()
    caudal =  models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'nivel_estanque_v'

class TemperaturaV(models.Model):
    fecha = models.DateTimeField(primary_key=True)        
    temperatura = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'temperatura_v'
#
class TempMaxV(models.Model):  
    fecha = models.DateTimeField(primary_key=True)
    temperatura = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)    
    class Meta:
        managed = False
        db_table = 'temp_max_v' 
#
class TempMinV(models.Model):  
    fecha = models.DateTimeField(primary_key=True)
    temperatura = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)    
    class Meta:
        managed = False
        db_table = 'temp_min_v' 

class PresionV(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    presion_nm = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    presion = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presion_v'

class HumedadV(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    humedad = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'humedad_v'


class RocioV(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    puntorocio = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'temprocio_v'

#
#
class HumMaxV(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    humedad = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'hum_max_v'

class HumMinV(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    humedad = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)   
    class Meta:
        managed = False
        db_table = 'hum_min_v'


class RadiacionV(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    radiacion = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'radiacion_v'
#
class RadMaxV(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    radiacion = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'rad_max_v'

class RadMinV(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    radiacion = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'rad_min_v'

class VientoV(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    viento_vel_km = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    viento_simbolo = models.CharField(max_length=255)
    viento_raf_km = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    viento_dir = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'viento_v'

class VientoVelMed12hV(models.Model):
    viento_vel_med12h = models.DecimalField(primary_key=True,max_digits=10, decimal_places=5)#, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'viento_vel_med12h_v'

class VientoDir12hV(models.Model):
    viento_simbolo = models.CharField(primary_key=True,max_length=255)
    viento_grado = models.IntegerField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'viento_dir_12h_v'
        
class ParV(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    par = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'par_v'

class ParMaxV(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    par = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'par_max_v'

class PrecipitacionV(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    lluvia = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    intensidad = models.DecimalField(max_digits=8, decimal_places=1, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'precipitacion_v'

class ETo(models.Model):
    fecha = models.DateTimeField(blank=True, null=True)
    ETo = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ETo'
class EToV(models.Model):
    fecha = models.DateTimeField(primary_key=True)#blank=True, null=True)
    ETo = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ETo_v'

class TempRocioV(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    puntorocio = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    class Meta:               
        managed = False
        db_table = 'temprocio_v'
 
#class CaudalEmbalseV(models.Model):
#    fecha = models.DateTimeField(primary_key=True)
#    caudal_m3min = models.DecimalField(max_digits=8, decimal_places=1, blank=True, null=True)
#    class Meta:        
#        managed = False       
#        db_table = 'caudal_embalse_v'
#
#class CaudalEstanqueV(models.Model):          
#    fecha = models.DateTimeField(primary_key=True)
#    caudal_m3min = models.DecimalField(max_digits=8, decimal_places=1, blank=True, null=True)
#    class Meta:        
#        managed = False         
#        db_table = 'caudal_estanque_v'

class SensacionTermicaT(models.Model):          
    fecha = models.DateTimeField(primary_key=True)
    calor = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    frio = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    class Meta:        
        managed = False           
        db_table = 'sensaciontermica_t'

class TendenciaV(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    tendencia= models.CharField(max_length=24)
    class Meta:
        managed = False 
        db_table = 'tendencia_v'
###exportar bbdd

class ExportarEmbalseV(models.Model):
    FECHA = models.DateTimeField(primary_key=True)
    LOC   = models.CharField(max_length=4)
    DIA   = models.CharField(max_length=2)
    MES   = models.CharField(max_length=2)
    ANO   = models.CharField(max_length=4)
    HORA  = models.CharField(max_length=2)
    MINUTO= models.CharField(max_length=2)
    TEMP  = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    PROCIO= models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    HR    = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True) 
    PAT   = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) 
    PATNM = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True) 
    IC    = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True) 
    VVTO  = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True) 
    DVTO  = models.IntegerField(blank=True, null=True) 
    RSOL  = models.IntegerField(blank=True, null=True) 
    RFA   = models.IntegerField(blank=True, null=True)
    PP    = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True) 
    IPP   = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True) 
    VOL   = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True) 
    TLLV  = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True) 
    class Meta:
        managed = False
        db_table = 'exportar_embalse_v'

class ExportarEstanqueV(models.Model):
    FECHA = models.DateTimeField(primary_key=True)
    LOC   = models.CharField(max_length=4)
    DIA   = models.CharField(max_length=2)
    MES   = models.CharField(max_length=2)
    ANO   = models.CharField(max_length=4)
    HORA  = models.CharField(max_length=2)
    MINUTO= models.CharField(max_length=2)
    VOL   = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    TLLV  = models.DecimalField(max_digits=6, decimal_places=4, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'exportar_estanque_v'

class ExportarEToV(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    LOC   = models.CharField(max_length=4)
    DIA   = models.CharField(max_length=2)
    MES   = models.CharField(max_length=2)
    ANO   = models.CharField(max_length=4)
    ETOD  = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'exportar_ETo_v'

class LluviaAcV(models.Model):
    fecha = models.DateTimeField(primary_key=True)
    lluvia_ac = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'lluvia_ac_v'
