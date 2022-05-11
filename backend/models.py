from django.db import models

class NavSlide(models.Model):
    class Meta:
        verbose_name = 'Navbar slide'
        verbose_name_plural = 'Navbar slides'
    
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    image = models.ImageField()

    def __str__(self):
        return self.name