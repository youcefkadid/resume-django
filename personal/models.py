from django.db import models

# Create your models here.


class about(models.Model):

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    adress=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.EmailField()
    details=models.TextField(max_length=600)
    def __str__(self):

        return 'about page : ' + self.first_name +''+self.last_name
    

class Aboutp(models.Model):

    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    adress=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.EmailField()
    details=models.TextField(max_length=600)
    def __str__(self):

        return 'about page : ' + self.first_name +''+self.last_name    


class Experience(models.Model):

    job_title=models.CharField(max_length=100)
    company_name=models.CharField(max_length=100)
    start_date=models.DateField(blank=True,null=True) 
    end_date=models.DateField( blank=True,null=True)
    details=models.TextField(max_length=600 , blank=True,null=True)
    def __str__(self):

        return 'experience  : ' + self.job_title



class Education(models.Model):

    school_name=models.CharField(max_length=100)
    major=models.CharField(max_length=100)
    skills=models.CharField(blank=True,null=True,max_length=200) 
    gpa=models.CharField(blank=True,null=True,max_length=200)
    start_date=models.DateField(blank=True,null=True) 
    end_date=models.DateField( blank=True,null=True)
    def __str__(self):

        return ' school  : ' + self.school_name
    

class Skills(models.Model):

    workflow=models.CharField(max_length=100)
   
    def __str__(self):

        return ' workflow  : ' + self.workflow
    


class Skills(models.Model):

    workflow=models.CharField(max_length=100)
   
    def __str__(self):

        return ' workflow  : ' + self.workflow    
    



class Portfolio(models.Model):

    project_name=models.CharField(max_length=100,blank=True,null=True)
    image=models.ImageField(null=True,blank=True) 
    description=models.TextField(max_length=300,blank=True,null=True)


    @property
    def imageURL(self):
        try:
            url=self.image.url

        except:
            url= '/img/default.png' 
        return url   

    def __str__(self):

        return ' workflow  : ' + self.project_name
    




    




    
    
