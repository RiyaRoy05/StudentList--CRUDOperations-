from django.contrib import admin
from web.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone','date_of_birth','email','image']
admin.site.register(Student,StudentAdmin)
