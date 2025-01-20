from django import forms
from .models import Article, Categorie


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu','categorie']


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom']

class ArticleFilterForm(forms.Form):
    name = forms.CharField(
        required=False,
        label="Nom de l'article",
        widget=forms.TextInput(attrs={'placeholder': 'Rechercher un article'})
    )
    category = forms.ChoiceField(
        required=False,
        label="Catégorie",
        choices=[],  # Les choix seront remplis dynamiquement dans la vue
    )
    date = forms.DateField(
        required=False,
        label="Date de l'article",
        widget=forms.DateInput(attrs={'type': 'date'})
    )

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'categorie']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control'}),
            'categorie': forms.Select(attrs={'class': 'form-control'}),
        }