# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-07-05T12:26:58+05:30
# @Email:  tamyworld@gmail.com
# @Filename: models.py
# @Last modified by:   tushar
# @Last modified time: 2017-07-05T12:51:48+05:30



from django.db import models
from fcm_django.models import FCMDevice


# Create your models here.
class Notification(models.Model):
    """
    Notification to be send to the user
    """
    title=models.CharField(max_length=200)
    body=models.TextField(max_length=1000)
    fcm_devices=models.ManyToManyField(FCMDevice)
    def __str__(self):
        """
        string representation
        """
        return self.title

    def save(self, *args, **kwargs):
        """
        send the notification upon save
        """
        super(Notification, self).save(*args, **kwargs)
        for device in self.fcm_devices.all():
            device.send_message(title=self.title,body=self.body)
