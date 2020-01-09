from django.core.management.base import BaseCommand
from shoebox.models import ShoeType, ShoeColor

class Command(BaseCommand):
    help ='What is the shoe type and color'

    def shoe_color(self):
        for pick_color in ShoeColor.color:
            ShoeColor.objects.create(color = pick_color[0])
    
    
    def shoe_type(self):
        for type in ShoeType.shoe_type:
            ShoeType.objects.create(style = type[0])

    def add(self, *arg, **kwargs):
        self.shoe_color()
        self.shoe_type()
        