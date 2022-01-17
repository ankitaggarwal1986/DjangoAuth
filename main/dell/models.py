from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    #def __str__(self):
        #return self.first_name
    
    def detail(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        return f'{self.first_name} {self.last_name}'
    
class Tracking(models.Model):
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    active_hours=models.IntegerField()
    idle_hours = models.IntegerField()

    #def __int__(self):
        #return self.emp_id
    
    def office_hours(self,active_hours, idle_hours):
        self.active_hours=active_hours
        self.idle_hours=idle_hours
        return (self.active_hours+self.active_hours)
