from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class ShoeType(models.Model):
    sneaker = 'sneaker'
    boot = 'boot'
    sandal = 'sandal'
    dress = 'dress'
    other = 'other'
    
    shoe_type = [
        (sneaker, 'sneaker'),
        (boot, 'boot'),
        (sandal, 'sandal'),
        (dress, 'dress'),
        (other, 'other')   
    ]
    style = models.CharField(
        max_length=50, choices=shoe_type, default=other)

    def __str__(self):
        return f'{self.style}'


class ShoeColor(models.Model):
    Red = 'Red'
    Orange = 'Orange'
    Yellow = 'Yellow'
    Green = 'Green'
    Blue = 'Blue'
    Indigo = 'Indigo'
    Violet = 'Violet'
    White = 'White'
    Black = 'Black'

    shoe_color = [
        (Red , 'Red'),
        (Orange , 'Orange'),
        (Yellow , 'Yellow'),
        (Green , 'Green'),
        (Blue , 'Blue'),
        (Indigo , 'Indigo'),
        (Violet , 'Violet'),
        (White , 'White'),
        (Black , 'Black')
    ]
    color = models.CharField(
        max_length=50, choices=shoe_color, default=Green)

    def __str__(self):
        return f'{self.color}'

class Shoe(models.Model):
    size = models.IntegerField(default=0)
    brand = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=50)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.brand}'