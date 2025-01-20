from django.urls import path
from .views import ListeArticlesView, CreerArticleView, CreerCategorieView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    #path('', views.liste_articles, name='liste_articles'),
    path('', ListeArticlesView.as_view(), name='liste_articles'),
    path('nouveau/', CreerArticleView.as_view(), name='creer_article'),
    path('nouveauCateg/', CreerCategorieView.as_view(), name='creer_categorie'),
    path('blogupdate/<int:pk>/edit/', ArticleUpdateView.as_view(), name='article-update'),
    path('blogdelete/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]