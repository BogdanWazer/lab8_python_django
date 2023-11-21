from django.shortcuts import render
from .models import Provider, Material, Supply

def index(request):
    providers = Provider.objects.all()
    materials = Material.objects.all()
    supplies = Supply.objects.all()

    tables = {
        'Providers': [[provider.name, provider.contact_person, provider.phone, provider.account] for provider in providers],
        'Materials': [[material.name, material.price] for material in materials],
        'Supplies': [[supply.date, supply.provider, supply.material, supply.days, supply.amount] for supply in supplies]
    }

    return render(request, r'/Users/wazermac/Desktop/lab8_python_django/project_lab8/lab8_app/templates/lab8_app/index.html', {'tables': tables})
