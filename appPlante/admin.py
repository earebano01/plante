from django.contrib import admin
from .models import Plante, Salle, Node, Measure

@admin.register(Plante)
class PlanteAdmin(admin.ModelAdmin):
    list_display = ['type_plante', 'id_node']

@admin.register(Salle)
class SalleAdmin(admin.ModelAdmin):
    list_display = ['nom_salle']

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ['num_node', 'id_salle']

@admin.register(Measure)
class MeasureAdmin(admin.ModelAdmin):
    list_display = ['temp', 'humidity', 'light', 'moist', 'datetime',  'num_node']
