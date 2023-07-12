from django.contrib import admin
from . import models
# Register your models here.

class IntroductionAdmin(admin.ModelAdmin):
    fields = ['introduction']
    
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
            
        return True
    
class HeadLineAdmin(admin.ModelAdmin):
    fields = ['headLine']
    
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
            
        return True    
    
class LeftSideTopBackgroundAdmin(admin.ModelAdmin): 
    fields = ['backgroundImage']
    
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
            
        return True  
    
class RightBannerImagesAdmin(admin.ModelAdmin): 
    fields = ['image']
    
class LogoAdmin(admin.ModelAdmin):
    fields = ['sanImage']
    
class ActivitiesAdmin(admin.ModelAdmin):
    fields = ['activities','smallImage1', 'smallImage2', 'largeImage', 'smallImage3', 'smallImage4']
    
class WorkShopAdmin(admin.ModelAdmin):
    fields = ['workTitle','workImage']    
    
class FAQLogoAdmin(admin.ModelAdmin):
    fields = ['fLogo']          
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
            
        return True
    
class FAQAdmin(admin.ModelAdmin):
    fields = ['question','answer']       
    
class ContactUsAdmin(admin.ModelAdmin):
    fields = ['telephone','email','address']    
    
class MenuAdmin(admin.ModelAdmin):
    fields = ['menuName','url']    
    
class SubMenuAdmin(admin.ModelAdmin):
    fields = ['menu', 'submenu','url']    
    
class SetLogoAdmin(admin.ModelAdmin):
    fields = ['setLogo']     
    
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
            
        return True

class SDhamLogoAdmin(admin.ModelAdmin):
    fields = ['dhaLogo']     
    
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
            
        return True
    
class TopHeaderTextAdmin(admin.ModelAdmin):
    fields = ['title', 'tlLogo']      
        
    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False    
        return True
    
class OurTeamAdmin(admin.ModelAdmin):
    fields = ['teamname']    
    
class JobAdmin(admin.ModelAdmin):
    fields = ['jobname', 'name','timage', 'designation', 'remark']        
    
class ShopAdmin(admin.ModelAdmin):
    fields = ['proLogo', 'productName', 'rs']
    
    
admin.site.register(models.Introduction,IntroductionAdmin)
admin.site.register(models.HeadLine,HeadLineAdmin)
admin.site.register(models.SLogo,LogoAdmin)
admin.site.register(models.Activities,ActivitiesAdmin)
admin.site.register(models.WorkShop,WorkShopAdmin)
admin.site.register(models.FAQLogo,FAQLogoAdmin)
admin.site.register(models.FAQ,FAQAdmin)
admin.site.register(models.ContactUs,ContactUsAdmin)
admin.site.register(models.Menu,MenuAdmin)
admin.site.register(models.SubMenu,SubMenuAdmin)
admin.site.register(models.SetLogo,SetLogoAdmin)
admin.site.register(models.SDhamLogo,SDhamLogoAdmin)
admin.site.register(models.TopHeaderText,TopHeaderTextAdmin)
admin.site.register(models.LeftSideTopBackground,LeftSideTopBackgroundAdmin)
admin.site.register(models.RightBannerImages,RightBannerImagesAdmin)
admin.site.register(models.OurTeam,OurTeamAdmin)
admin.site.register(models.Job,JobAdmin)
admin.site.register(models.Shop,ShopAdmin)
