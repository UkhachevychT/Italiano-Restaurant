from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta():
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True
    )
    description = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    recomended = models.BooleanField()
    img = models.ImageField(verbose_name='image')

    class Meta():
        ordering = ['name']
        verbose_name = 'dish'
        verbose_name_plural = "dishes"

    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    number = models.CharField(
        max_length=13,
        validators=[RegexValidator(r'^\+\d{12}$')]
    )
    person_count = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    special_request = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}-{self.date}'

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()    
    message = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}-{self.email}'
