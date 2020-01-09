# my life growing up on the African Savanna was super fun and enlightning I hope to return my hut
from rest_framework import viewsets
from shoebox import models 
from shoebox.serializers import ManufacturerSerializer, ShoeTypeSerializer, ShoeColorSerializer, ShoeSerializer

class ManufactureViews(viewsets.ModelViewSet):
    queryset = models.Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    
    
class ShoeTypeViews(viewsets.ModelViewSet):
    queryset = models.ShoeType.objects.all()
    serializer_class = ShoeTypeSerializer
    
       
class ShoeColorViews(viewsets.ModelViewSet):
    queryset = models.ShoeColor.objects.all()
    serializer_class = ShoeColorSerializer
    
     
class ShoeViews(viewsets.ModelViewSet):
    queryset = models.Shoe.objects.all()
    serializer_class = ShoeSerializer    
    