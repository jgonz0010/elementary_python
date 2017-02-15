from django.db import models

# Create your models here.
class Suspect(models.Model):
    name = models.CharField(max_length = 50)
    hair = models.CharField(max_length = 50, blank = True)
    attire = models.CharField(max_length = 50, blank = True)
    room = models.IntegerField(default=0, blank = True)
    is_murderer = models.BooleanField(default=False)

    def __str__(self):
        return (
        "\nSuspect Name: " + self.name +
        "\nSuspect Hair: " + self.hair +
        "\nSuspect Attire: " + self.attire +
        "\nSuspect Room: " + str(self.room) +
        "\nIs Murderer: " + str(self.is_murderer));
