from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)  
    phone = models.CharField(max_length=15) 
    date_of_birth = models.DateField()  
    email = models.EmailField(unique=True)  
    image=models.ImageField(upload_to='student_image',null=True,blank=True)

    class Meta:
        verbose_name_plural="web.Student"
        ordering=['id']

    def __str__(self):
        return self.name
