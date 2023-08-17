from django import forms 
from .models import ipfs,team,capture,buy_energy,meter_analytics,summary_file,meta_video,forum,cloud
       

class buyForm(forms.ModelForm):
    class Meta:
        model = buy_energy
        fields = [
            'cus_name',
            'meter_id',
            'quantity',
            'energy_price',
        ]
