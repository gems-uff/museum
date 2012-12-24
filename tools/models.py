from django.db import models

# Create your models here.

class Institution(models.Model):
    acronym = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.acronym

class Researcher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    affiliation = models.ManyToManyField(Institution)
    def __unicode__(self):
        return self.name

class Edition(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(choices=([(year, year) for year in range(1987, 2013)]))
    place = models.CharField(max_length=100)
    chair = models.ManyToManyField(Researcher)
    def __unicode__(self):
        return self.name + " " + unicode(self.year)