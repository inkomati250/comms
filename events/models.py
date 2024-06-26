from django.db import models

#app views


class Events(models.Model):
    DAY_CHOICES = [
        ('Montag', 'Montag'),
        ('Dienstag', 'Dienstag'),
        ('Mittwoch', 'Mittwoch'),
        ('Donnerstag', 'Donnerstag'),
        ('Freitag', 'Freitag'),
        ('Samstag', 'Samstag'),
        ('Sonntag', 'Sonntag'),
    ]

    datum = models.DateField()
    day = models.CharField(max_length=50, choices=DAY_CHOICES)
    time = models.TimeField()
    street_name = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10, default='')
    postal_code = models.CharField(max_length=6, default='')
    city = models.CharField(max_length=100, null=True, default="")

    filmname = models.CharField(max_length=100)
    trailer = models.URLField()

    def __str__(self):
        return self.filmname
        #get formated adress
    @property
    def formatted_address(self):
        return f"{self.street_name} {self.house_number}, {self.postal_code} {self.city}"

class EventImage(models.Model):
    event = models.ForeignKey(Events, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images')

    def __str__(self):
        return f"{self.event.filmname}"

class Impressum(models.Model):
    impressum = models.TextField(verbose_name='Impressum', default='')
    contact_info = models.TextField(verbose_name='Kontaktinformationen', default='')
    geschaeftsfuehrung = models.TextField(verbose_name='geschaeftsfuehrung', default='')
    datenschutz = models.TextField(verbose_name='Datenschutz', default='')

    def __str__(self):
        return self.impressum if self.impressum else "No Impressum"

class InformationImage(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='information_images')

    def __str__(self):
        return self.name




