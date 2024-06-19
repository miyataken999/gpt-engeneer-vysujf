from django.db import models

class Coupon(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    expiration_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name