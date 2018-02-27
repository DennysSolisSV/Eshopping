from django.db import models


class Template(models.Model):
    top_bar = models.TextField()
    top_text = models.TextField()
    color_background = models.TextField()
    color_text = models.TextField()
    logo = models.ImageField(upload_to='images/template')
    icono = models.ImageField(upload_to='images/template')
    social = models.TextField()
    time_stamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.social

