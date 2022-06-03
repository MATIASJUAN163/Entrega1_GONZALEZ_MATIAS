from tkinter.tix import Meter
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Modem)
admin.site.register(Webclient)
admin.site.register(Smartmeter)