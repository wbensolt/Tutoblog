from django.db import models

class Categorie (models.Model):
    nom = models.CharField(max_length=100)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom

class Article (models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.SET_NULL)
    date_publication = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titre
# Create your models here.
