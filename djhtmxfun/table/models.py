from django.db import models


class TableData(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    distance = models.IntegerField()

    class Meta:
        ordering = ("name", "quantity", "distance")

    def __str__(self):
        return f"{self.date} {self.name} {self.quantity} {self.distance}"
