# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User



class buy_energy(models.Model):
    cus_name=models.CharField(max_length=20,default=None)
    meter_id=models.IntegerField(default="",blank=True,null=True)
    quantity=models.IntegerField(default="",blank=True,null=True)
    energy_price=models.IntegerField(default="",blank=True,null=True)

    def __str__(self):
        return self.cus_name
    

