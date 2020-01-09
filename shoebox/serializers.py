from rest_framework.serializers import HyperlinkedModelSerializer
from shoebox.models import Manufacturer, ShoeType, ShoeColor, Shoe


class ManufacturerSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'website']

class ShoeTypeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeType
        fields = ['id', 'style']
        
class ShoeColorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ['id', 'color']
        
class ShoeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = [
            'id', 'size', 'brand', 'manufacturer', 'color','material','shoe_type','fasten_type']