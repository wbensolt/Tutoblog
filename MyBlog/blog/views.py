from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.shortcuts import render

from .forms import ArticleForm, CategorieForm, ArticleFilterForm, ArticleUpdateForm
from .models import Article, Categorie

"""def liste_articles(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request=request, template_name='blog/liste_articles.html', context=context)
# Create your views here.
"""
class ListeArticlesView(ListView):
    model = Article
    template_name = 'blog/liste_articles.html'
    context_object_name = 'articles'

    def get_queryset(self):
        """
        Filtrer les articles en fonction des paramètres GET.
        """
        queryset = Article.objects.all()
        name = self.request.GET.get('name')
        category = self.request.GET.get('category')
        date = self.request.GET.get('date')

        if name:
            queryset = queryset.filter(titre__icontains=name)
        if category:
            queryset = queryset.filter(categorie__id=category)
        if date:
            queryset = queryset.filter(date_publication=date)

        return queryset

    def get_context_data(self, **kwargs):
        """
        Ajouter le formulaire de filtrage au contexte.
        """
        context = super().get_context_data(**kwargs)
        form = ArticleFilterForm(self.request.GET or None)

        # Remplir les choix pour le champ category
        form.fields['category'].choices = [('', 'Toutes les catégories')] + [
            (cat.id, cat.nom) for cat in Categorie.objects.all()
        ]

        context['filter_form'] = form
        return context

class CreerArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/creer_article.html'
    success_url = reverse_lazy('liste_articles')

class CreerCategorieView(CreateView):
    model = Categorie
    form_class = CategorieForm
    template_name = 'blog/creer_categorie.html'
    success_url = reverse_lazy('liste_articles')

"""class ListeArticlesSearchView(ListView):
    template_name = 'blog/liste_articles.html'
    context_object_name = 'articles'

    def get_queryset(self):
        query = self.request.GET.get('name')
        if query :
            return Article.objects.filter(titre__icontains=query)
        return Article.objects.all()"""

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = 'blog/article_update.html'

    def get_success_url(self):
        return reverse_lazy('liste_articles')  # Redirige vers la liste des articles après modification


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'blog/article_delete_confirm.html'
    context_object_name = 'article'

    def get_success_url(self):
        return reverse_lazy('liste_articles')  # Red