# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

# Register your models here.
from .models import team
admin.site.register(team)

# from .models import UploadFile
# admin.site.register(UploadFile)

from .models import buy_energy
admin.site.register(buy_energy)


from .models import meter_analytics
admin.site.register(meter_analytics)
