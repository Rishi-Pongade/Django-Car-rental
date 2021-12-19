from django.db import models

# Create your models here.
class cars(models.Model):
    name=models.CharField(max_length=225)
    price=models.CharField(max_length=225)
    image=models.CharField(max_length=225)

    def __str__(self) -> str:
        return self.name