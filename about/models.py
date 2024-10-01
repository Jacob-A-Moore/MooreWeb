from django.db import models

# Create your models here.
class Bio(models.Model):
    biogoraphy = models.CharField(max_length=150)
    image = models.ImageField(upload_to="bios/", blank=True, null=True)

    def __str__(self):
        return self.biogoraphy

class Education(models.Model):
    
    college_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    length_of_study = models.CharField(max_length=30)
    reflection = models.TextField()

    def __str__(self):
        return f"Majored in {self.degree} at {self.college_name} during {self.length_of_study}"


class Experience(models.Model):
    
    employer = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    responsibilities = models.TextField()

    def __str__(self):
        return f"Employer:{self.employer}\nTitle: {self.job_title}\nLocation:{self.location}\nDate Employed:{self.start_date} - {self.end_date}"

class Skill(models.Model):

    name = models.CharField(max_length=100)
    ##skill_origin = models.CharField(max_length=200)

    def __str__(self):
        return f"Skill: {self.name}"

    

class Hobby(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    
class Interest(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    
    
    
