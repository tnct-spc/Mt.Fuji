from django.shortcuts import render


def register(request):
    '''サンプル用のサインアップページ'''
    return render(request, 'sample/register/index.html', {})    

def login(request):
    '''サンプル用のログインページ'''
    return render(request, 'sample/login/index.html', {})    
