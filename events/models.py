from django.db import models

COLOR_CHOICES = (
     ('#FFFFFF', 'White'),
     ('#C0C0C0', 'Silver'),
     ('#808080', 'Gray'),
     ('#000000', 'Black'),
     ('#FF0000', 'Red'),
     ('#800000', 'Maroon'),
     ('#FFFF00', 'Yellow'),
     ('#808000', 'Olive'),
     ('#00FF00', 'Lime'),
     ('#008000', 'Green'),
     ('#00FFFF', 'Aqua'),
     ('#008080', 'Teal'),
     ('#3a87ad', 'Blue'),
     ('#000080', 'Navy'),
     ('#FF00FF', 'Fuchsia'),
     ('#800080', 'Purple')
 )

class Event(models.Model):
    title = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    color = models.CharField(max_length=7, choices=COLOR_CHOICES, default='#3a87ad')
    description = models.TextField(blank=True, default='')

    def test(self):
        return 'ok'

    def __str__(self):
        return str(self.title)