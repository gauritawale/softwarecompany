from django.contrib import admin
from website import models
# Register your models here.
class FeatureAdmin(admin.ModelAdmin):
    list_display=('feature_image','feature_title','feature_details')
    
admin.site.register(models.Feature,FeatureAdmin)





# class YourModelAdmin(admin.ModelAdmin):
#     list_display = ('field1', 'field2', 'field3')

# admin.site.register(YourModel, YourModelAdmin)

