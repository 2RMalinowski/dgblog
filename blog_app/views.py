from django.shortcuts import render


def post_list(request):
    return render(request, 'blog_app/post_list.html', {})
