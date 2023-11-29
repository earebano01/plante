from rest_framework.viewsets import ModelViewSet
from .models import Plante, Salle, Node, Measure
from .serializers import PlanteSerializer, SalleSerializer, NodeSerializer, MeasureSerializer
from django.core.serializers import serialize
import json
from django.http import JsonResponse
from django.shortcuts import render

"""def BASE(request):
    nombre_salles = Salle.objects.count()
    nombre_nodes = Node.objects.count()
    nombre_plantes = Plante.objects.count()

    nodes_data = []
    for node in Node.objects.all():
        measures = Measure.objects.filter(num_node=node.num_node).order_by('-datetime')[:30]
        measures_json = serialize('json', measures)
        nodes_data.append({
            'num_node': node.num_node,
            'measures': measures_json
        })

    return render(request, 'base.html', {
        'nombre_salles': nombre_salles,
        'nombre_nodes': nombre_nodes,
        'nombre_plantes': nombre_plantes,
        'nodes_data_json': json.dumps(nodes_data)  # Vérifiez que ceci est une chaîne JSON valide
    })
"""

def BASE(request):
    nombre_salles = Salle.objects.count()
    nombre_nodes = Node.objects.count()
    nombre_plantes = Plante.objects.count()

    nodes_data = []
    for node in Node.objects.all():
        measures = Measure.objects.filter(num_node=node.num_node).order_by('-datetime')[:30]
        measures_json = json.loads(serialize('json', measures))
        node_data = {
            'num_node': node.num_node,
            'measures': measures_json
        }
        nodes_data.append(node_data)

    nodes_data_json = json.dumps(nodes_data)  # Serialize the list of nodes with their measures

    return render(request, 'base.html', {
        'nombre_salles': nombre_salles,
        'nombre_nodes': nombre_nodes,
        'nombre_plantes': nombre_plantes,
        'nodes_data_json': nodes_data_json  # Pass the JSON string to the template
    })


    



class PlanteViewset(ModelViewSet):
    serializer_class = PlanteSerializer

    def get_queryset(self):
        return Plante.objects.all()

class SalleViewset(ModelViewSet):
    serializer_class = SalleSerializer

    def get_queryset(self):
        return Salle.objects.all()

class NodeViewset(ModelViewSet):
    serializer_class = NodeSerializer

    def get_queryset(self):
        return Node.objects.all()

class MeasureViewset(ModelViewSet):
    serializer_class = MeasureSerializer

    def get_queryset(self):
        return Measure.objects.all()
    




    


