from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class Inventaire(models.Model): 
    SN = models.CharField(max_length=100, unique=True)
    Application = models.CharField(max_length=100)
    IP = models.CharField(max_length=100)
    Site = models.CharField(max_length=100)
    Position = models.CharField(max_length=100 )
    Marque = models.CharField(max_length=100)
    Disk = models.CharField(max_length=100)
    CPU = models.CharField(max_length=100)
    RAM = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    Support = models.CharField(max_length=100)
    Type = models.CharField(max_length=1000)

@receiver(pre_save, sender=Inventaire)
def prevent_sn_change(sender, instance, **kwargs):
    if instance.pk:  # Vérifie si l'objet existe déjà (n'est pas en cours de création)
        original_instance = Inventaire.objects.get(pk=instance.pk)
        if original_instance.SN != instance.SN:
            # Si l'attribut fixed_field est différent de sa valeur d'origine, annule la modification
            instance.SN = original_instance.SN 

class Incident(models.Model): 
    SN = models.CharField(max_length=100)
    Date = models.DateField(auto_now_add=True)
    Description = models.CharField(max_length=1000)
    Application = models.CharField(max_length=1000)
    Type = models.CharField(max_length=1000)

@receiver(pre_save, sender=Incident)
def prevent_sn_change(sender, instance, **kwargs):
    if instance.pk:  # Vérifie si l'objet existe déjà (n'est pas en cours de création)
        original_instance = Incident.objects.get(pk=instance.pk)
        if original_instance.SN != instance.SN:
            # Si l'attribut fixed_field est différent de sa valeur d'origine, annule la modification
            instance.SN = original_instance.SN
        if original_instance.Date != instance.Date:
            # Si l'attribut fixed_field est différent de sa valeur d'origine, annule la modification
            instance.Date = original_instance.Date
        if original_instance.Description != instance.Description:
            # Si l'attribut fixed_field est différent de sa valeur d'origine, annule la modification
            instance.Description = original_instance.Description
        if original_instance.Application != instance.Application:
            # Si l'attribut fixed_field est différent de sa valeur d'origine, annule la modification
            instance.Application = original_instance.Application
        if original_instance.Type != instance.Type:
            # Si l'attribut fixed_field est différent de sa valeur d'origine, annule la modification
            instance.Type = original_instance.Type