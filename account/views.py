from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


@login_required#данный декоратор проверяет аутентификацию текущего пользователя
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)#создается экземпляр формы с переданными данными
        if form.is_valid(): #валидация формы
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])#если данные валидны, пользователь аутентифицируется по БД
            if user is not None:
                if user.is_active:#проверяется статус пользователя - активна
                    login(request, user)#пользователь входит в систему
                    return HttpResponse('Authenticated successfully')#аутентифкация прошла успешно
                else:
                    return HttpResponse('Disabled account')#учетная запись не активна
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
