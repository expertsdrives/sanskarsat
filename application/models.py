from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField

# Create your models here.
class Introduction(models.Model):
    introduction = RichTextField()
    
    def __str__(self):
        return  str(self.introduction)
    
class HeadLine(models.Model):
    headLine = models.CharField(max_length=256)
    
    def __str__(self):
        return  str(self.headLine)    
    
class LeftSideTopBackground(models.Model):
    backgroundImage = models.ImageField(upload_to = "images")
    
    def __str__(self):
        return  str(self.backgroundImage)    
    
class RightBannerImages(models.Model):
    image = models.ImageField(upload_to = "images")
    
    def __str__(self):
        return  str(self.image)  
    
class SLogo(models.Model):
    sanImage = models.ImageField(upload_to = "images")
    
    def __str__(self):
        return str(self.sanImage)
    
class Activities(models.Model):
    activities = models.CharField(max_length=256)
    smallImage1 = models.ImageField(upload_to = "images", default="")
    smallImage2 = models.ImageField(upload_to = "images", default="")
    largeImage = models.ImageField(upload_to = "images", default="")
    smallImage3 = models.ImageField(upload_to = "images", default="")
    smallImage4 = models.ImageField(upload_to = "images", default="")
    
    def __str__(self):
        return str(self.activities)
    
class WorkShop(models.Model):
    workTitle = models.CharField(max_length=256)
    workImage = models.ImageField(upload_to = "images")
    
    def __str__(self):
        return str(self.workTitle)    
    
class FAQLogo(models.Model):
    fLogo = models.ImageField(upload_to = "images")
    
    def __str__(self):
        return str(self.fLogo) 
    
class FAQ(models.Model):
    question = models.TextField(max_length=256)
    answer = models.TextField(max_length=256)
    
    def __str__(self):
        return self.question
    
class ContactUs(models.Model):
    telephone = models.CharField(max_length=15)
    email = models.EmailField(max_length=256)
    address = models.TextField(max_length=256)
    
    def __str__(self):
        return str(self.telephone) 
    
class Menu(models.Model):
    menuName = models.CharField(max_length=256)
    url = models.CharField(max_length=256)    
    
    def __str__(self):
        return str(self.menuName)
    
class SubMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT, default="")
    submenu = models.CharField(max_length=256, default='', blank=True)
    subMenuUrl = models.CharField(max_length=256,name='url')      
    
    def __str__(self):
        return str(self.submenu)
    
class SetLogo(models.Model):
    setLogo = models.ImageField(upload_to = "images")
    
    def __str__(self):
        return str(self.setLogo)
    
class SDhamLogo(models.Model):
    dhaLogo = models.ImageField(upload_to = "images")
    
    def __str__(self):
        return str(self.dhaLogo)    
    
class TopHeaderText(models.Model):
    title = models.CharField(max_length=256)
    tlLogo = models.ImageField(upload_to = "images", default='')
    
    def __str__(self):
        return str(self.title)        
    
           
class OurTeam(models.Model):
    teamname = models.CharField(max_length=256, default="")  
    
    def __str__(self):
        return str(self.teamname)
    
class Job(models.Model):
    jobname = models.ForeignKey(OurTeam, on_delete=models.PROTECT, default="")
    name = models.CharField(max_length=256, default="")
    timage = models.ImageField(upload_to = "images", default='')
    designation = models.CharField(max_length=256)
    remark = models.CharField(max_length=256, default='')
                               
    def __str__(self):
        return str(self.name)
    
class Shop(models.Model):
    proLogo = models.ImageField(upload_to = "images", default='')
    productName = models.CharField(max_length=256)
    rs = models.CharField(max_length=256)
    
    def __str__(self):
        return str(self.productName)            