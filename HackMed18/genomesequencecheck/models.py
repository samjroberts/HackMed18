from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Bacteria(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return "Bacteria: {}".format(self.name)

@python_2_unicode_compatible
class GenomeIndicator(models.Model):
    operon = models.CharField(max_length=50)
    sequence = models.TextField(max_length=1000, blank=True)
    bacteria = models.ForeignKey(Bacteria, related_name="genomes", on_delete=models.CASCADE)

    def __str__(self):
        return "Sequence: {}".format(self.sequence)
