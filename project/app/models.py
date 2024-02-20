from django.db import models

class Adhar(models.Model):
    Adhar=models.IntegerField()
    def __str__(self):
        return str(self.Adhar)
    
class Allot(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Adhar = models.OneToOneField(Adhar,on_delete=models.CASCADE)    
