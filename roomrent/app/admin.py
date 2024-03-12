# from django.contrib import admin

# from . models import room_rent


# class room_rentAdmin(admin.ModelAdmin):
#     list_display = ['owner','room_prize','total_rooms','room_for']

#     def formfield_for_dbfield(self, db_field, **kwargs):
#         if db_field.name == 'room_images':
#             kwargs['widget'] = admin.widgets.AdminFileWidget(multiple=True)  # Set multiple=True for multiple file uploads
#         return super().formfield_for_dbfield(db_field, **kwargs)


# admin.site.register(room_rent,room_rentAdmin)


from django.contrib import admin
from django import forms
from .models import room_rent , room_money



class room_rentAdmin(admin.ModelAdmin):
    list_display = ['owner','room_prize','total_rooms','room_for']

class room_moneyAdmin(admin.ModelAdmin):
    list_display = ['name','amount','payment_id','paid']



admin.site.register(room_rent, room_rentAdmin)
admin.site.register(room_money, room_moneyAdmin)

