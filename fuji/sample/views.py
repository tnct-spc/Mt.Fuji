from django.shortcuts import render


def register(request):
    '''サンプル用のサインアップページ'''
    return render(request, 'sample/register/index.html', {})    

def login(request):
    '''サンプル用のログインページ'''
    return render(request, 'sample/login/index.html', {})    

def nfc_register(request):
    '''NFCタグ登録ページ'''
    return render(request, 'sample/nfc_register/index.html', {})

def nfc_check(request):
    '''NFCタグ確認ページ'''
    return render(request, 'sample/nfc_check/index.html', {})
