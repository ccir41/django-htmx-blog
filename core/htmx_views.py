from django.shortcuts import render


def render_navbar(request):
    user = request.user
    return render(request, 'navbar.html', {'user': user})