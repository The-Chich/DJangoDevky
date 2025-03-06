from django.shortcuts import render  # Importujeme funkci render

# Funkce pro vykreslení seznamu příspěvků na hlavní stránce blogu
def post_list(request):
    return render(request, 'blog/post_list.html', {})
