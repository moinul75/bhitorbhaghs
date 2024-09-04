from django.db import models

# Create your models here.   
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        abstract = True 
        
class SocialMedia(TimeStampedModel):
    facebook = models.URLField(max_length=500, blank=True, null=True)
    twitter = models.URLField(max_length=500, blank=True, null=True)
    youtube = models.URLField(max_length=500, blank=True, null=True)
    linkedin = models.URLField(max_length=500, blank=True, null=True)
    instagram = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self) -> str:
        return f"Social Media Links"

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Social Media"

class Icon(TimeStampedModel):
    name = models.CharField(max_length=50,null=True)  # e.g., 'fa-map-marker-alt', 'fa-envelope-open', etc.
    class_name = models.CharField(max_length=50,null=True)  # Font Awesome class, e.g., 'fa-map-marker-alt'

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Icon"


class Contact(TimeStampedModel): 
    location = models.CharField(max_length=255, blank=True, null=True) 
    email = models.EmailField(max_length=255, null=True, blank=True, unique=True) 
    phone = models.CharField(max_length=20, null=True, blank=True)  
    map_link = models.URLField(max_length=500, blank=True, null=True) 
    icons = models.ManyToManyField(Icon, blank=True)

    def __str__(self) -> str:
        return f"{self.location} -> {self.email} -> {self.phone}" 
    
    class Meta:  
        ordering = ['-id']
        verbose_name_plural = "Contact"
    
    
class Complain(models.Model):
    gurdian_name = models.CharField(max_length=100)
    gurdian_email = models.EmailField()
    student_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return f"Complaint from {self.gurdian_name} about {self.student_name}"

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Complain" 
        
class ImportantLink(models.Model):
    link_name = models.CharField(max_length=100)
    link = models.URLField(max_length=500)

    def __str__(self) -> str:
        return f"{self.link_name}: {self.link}"

    class Meta:
        ordering = ['link_name']
        verbose_name_plural = "Important Links" 
        
    

class Slider(models.Model): 
    name = models.CharField(max_length=25,null=True,blank=True) 
    slide_img = models.ImageField(upload_to='Sliders/',null=True,blank=True) 
    
    def __str__(self):
        return self.name  
    
class Qoutes(models.Model):
    image = models.ImageField(upload_to='Quote/', null=True, blank=True)
    writer_name = models.CharField(max_length=100)
    quote = models.TextField()

    def __str__(self) -> str:
        return f"{self.writer_name}: {self.quote[:50]}..."

    class Meta:
        ordering = ['writer_name']
        verbose_name_plural = "Quotes" 
        
        
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Teachers/', blank=True, null=True)
    facebook = models.URLField(max_length=500, blank=True, null=True)
    instagram = models.URLField(max_length=500, blank=True, null=True)
    linkedin = models.URLField(max_length=500, blank=True, null=True)
    twitter = models.URLField(max_length=500, blank=True, null=True)
    youtube = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.designation}"

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Teacher"
    
    
class Gallary(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='Gallery/') 
    created_at = models.DateTimeField(auto_now_add=True,null=True) 
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Gallary"  



        
