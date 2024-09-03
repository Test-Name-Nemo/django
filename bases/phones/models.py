from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=150)
    image = models.URLField()
    price = models.DecimalField(decimal_places=2)
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=50)
    slug = models.CharField(max_length=150)
    
    def __str__(self):
        return f"Название: {self.name}, Цена: {self.price}, Фото: {self.image}"
