# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-07-05T12:26:58+05:30
# @Email:  tamyworld@gmail.com
# @Filename: admin.py
# @Last modified by:   tushar
# @Last modified time: 2017-07-05T13:22:33+05:30



from django.contrib import admin
from .models import Notification
from fcm_django.models import FCMDevice

class NotificationodelAdmin(admin.ModelAdmin):
    """model admin for the Notification"""
    def save_model(self, request, obj, form, change):
        for device in form.cleaned_data.get("fcm_devices"):
            device.send_message(title=request.POST.get("title"),body=request.POST.get("body"))
        super(NotificationodelAdmin, self).save_model(request, obj, form, change)

# Register your models here.
admin.site.register(Notification, NotificationodelAdmin)
