# from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer
# from .models import Plante, Salle

# class PlanteSerializer(ModelSerializer):
#     class Meta:
#         model = Plante
#         fields = ['id', 'nom', 'temperature', 'humidite', 'datetime']


# class SalleSerializer(serializers.ModelSerializer):
#     plante = serializers.SerializerMethodField()

#     class Meta:
#         model = Salle
#         fields = ['id', 'nom', 'plante']
    
#     def get_plante(self, instance):
#         queryset = Plante.objects.filter(salle=instance)
#         serializer = PlanteSerializer(queryset, many=True)
#         return serializer.data
    
from rest_framework import serializers
from .models import Plante, Salle, Node, Measure

class PlanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plante
        fields = ['id', 'type_plante', 'id_node']

class SalleSerializer(serializers.ModelSerializer):
    node = serializers.SerializerMethodField()

    class Meta:
        model = Salle
        fields = ['id', 'nom_salle', 'node']
    
    def get_node(self, instance):
        queryset = Node.objects.filter(id_salle=instance)
        serializer = NodeSerializer(queryset, many=True)
        return serializer.data

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ['id', 'num_node', 'id_salle']

class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = ['id', 'temp', 'humidity', 'light', 'moist', 'datetime',  'num_node']
