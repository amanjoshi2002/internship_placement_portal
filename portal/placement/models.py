from django.db import models

class Internship(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    slots = models.IntegerField()
    link = models.URLField()
    logo = models.ImageField(upload_to='internship_logos/', blank=True, null=True)
    last_date_to_apply = models.DateField()

    def __str__(self):
        return self.name

class Placement(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    slots = models.IntegerField()
    link = models.URLField()
    logo = models.ImageField(upload_to='placement_logos/', blank=True, null=True)
    last_date_to_apply = models.DateField()

    def __str__(self):
        return self.name

class Placed(models.Model):
    profile_photo = models.ImageField(upload_to='placed_profile_photos/', blank=True, null=True)
    department = models.CharField(max_length=20 ,blank=True, null=True)
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.name
