from django.db import models

class empmodel(models.Model):
    
    empid = models.IntegerField(primary_key=True)

    empname = models.CharField(max_length=100)

    email = models.CharField(max_length=100)

    salary = models.IntegerField()

    class Meta:

        db_table = "employeer"