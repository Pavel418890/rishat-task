from django.db import models


class Item(models.Model):
    name = models.CharField(
        verbose_name="Item name",
        db_index=True,
        max_length=100,
    )
    price = models.DecimalField(
        verbose_name="Item price", max_digits=7, decimal_places=2
    )
    description = models.TextField(
        verbose_name="Item description",
        null=True,
    )

    class Meta:
        db_table = "items"
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name
