from django.contrib import admin
from .models import MyUser, BikeCompanyModel,ServiceRequestForm, BikeModel, OurServices, BlogModel
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(MyUser, UserAdmin)

UserAdmin.fieldsets += ("Custom Fields sets", {
    'fields':('riderName', 'riderEmail', 'riderPassword', 'phone_number',)
}),


@admin.register(BikeCompanyModel)
class BikeCompanyAdmin(admin.ModelAdmin):
    list_display = ["companyName"]

@admin.register(ServiceRequestForm)
class ServiceRequestForm_Admin(admin.ModelAdmin):
    list_display = ['rider_name', 'bike_company', 'bike_model', 'bike_color', 'pickup', 'delivery', 'kmcovered', 'contact', 'problem', 'serviceDate', 'serviceTime', 'deliveryTime', 'completed']   

@admin.register(BikeModel)
class BikeModel_Admin(admin.ModelAdmin):
    list_display = ["company", "model", "bike_number", "bike_color", "picture", "rider"]

@admin.register(OurServices)
class OurServices(admin.ModelAdmin):
    list_display = ['serviceTitle', 'serviceContent', 'servicePhoto']

@admin.register(BlogModel)
class BlogModel_Admin(admin.ModelAdmin):
    list_display = ['blogTitle', 'blogImage', 'blogContent', 'blogLink']
