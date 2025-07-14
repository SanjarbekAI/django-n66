from django.db import models


class Products(models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"ID: {self.id}) {self.name} | {self.quantity}"

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
