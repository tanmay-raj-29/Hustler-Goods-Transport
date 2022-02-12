from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=150, blank=False)
    state = models.CharField(max_length=150, blank=False)
    latitude = models.DecimalField(decimal_places=8, max_digits=15)
    longitude = models.DecimalField(decimal_places=8, max_digits=15)

    def __str__(self):
        return self.name + '|' + self.state




class Route(models.Model):
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='from_city')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='to_city')
    days = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return self.from_city.name + ' -> ' + self.to_city.name




class Dealer(models.Model):
    name = models.CharField(max_length=150, blank=False)
    mobile_number = models.CharField(max_length=10, blank=False)
    material_nature = models.CharField(max_length=100, blank=False)
    material_weight = models.CharField(max_length=100, blank=False)
    quantity = models.IntegerField(blank=False)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class Driver(models.Model):
    name = models.CharField(max_length=150, blank=False)
    age = models.PositiveIntegerField(blank=False)
    truck_number = models.CharField(max_length=100, blank=False)
    mobile_number = models.CharField(max_length=10, blank=False)
    capacity = models.PositiveIntegerField(blank=False)
    transporter_name = models.CharField(max_length=150, blank=False)
    experience = models.PositiveIntegerField(blank=False)
    routes = models.ManyToManyField(Route)
    def __str__(self):
        return self.name




# class Deal(models.Model):
#     driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
#     dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)
#     route = models.ForeignKey(Route, on_delete=models.CASCADE)
#     is_confirmed = models.BooleanField()

#     def __str__(self):
#         return self.driver + ' & ' + self.dealer