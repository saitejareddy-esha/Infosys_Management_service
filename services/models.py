from django.db import models

# Create your models here.

class Dataset(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DataElement(models.Model):
    DATA_TYPES = [
        ('string', 'String'),
        ('integer', 'Integer'),
        ('date', 'Date'),
        ('boolean', 'Boolean'),
    ]

    dataset = models.ForeignKey(
        Dataset,
        related_name='elements',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    data_type = models.CharField(max_length=20, choices=DATA_TYPES)
    is_required = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('dataset', 'name')

    def __str__(self):
        return f"{self.dataset.name}.{self.name}"
