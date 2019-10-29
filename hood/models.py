from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class NeighbourHood(models.Model):
    name = models.CharField(max_length = 30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    occupants = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.name

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()


class UserProfile(models.Model):
    name = models.CharField(max_length = 50)
    neighbourhood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, null=True)
    bio = models.TextField(null=True)
    email = models.EmailField(max_length = 60, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
