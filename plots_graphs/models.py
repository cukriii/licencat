from django.db import models

# Create your models here.
"""
class Kategoria(models.Model):
    id_kategorii = models.PositiveIntegerField()
    nazwa = models.CharField(max_length=50)

class Klient(models.Model):
    id_klienta = models.PositiveIntegerField()
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)

class Produkt(models.Model):
    id_produktu = models.PositiveIntegerField()
    nazwa = models.CharField(max_length=50, default="a")
    id_kategorii = models.PositiveIntegerField(default='1')
    cena = models.FloatField(default='0')

class Produkty_Zamowienia(models.Model):
    id_zamowienia = models.PositiveIntegerField()
    id_produktu = models.PositiveIntegerField()
    ilosc = models.PositiveIntegerField()

class Sprzedawca(models.Model):
    id_sprzedawcy = models.PositiveIntegerField()
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)

class Zamowienie(models.Model):
    id_zamowienia = models.PositiveIntegerField()
    id_klienta = models.PositiveIntegerField()
    id_sprzedawcy = models.PositiveIntegerField()
    data = models.DateField()
"""