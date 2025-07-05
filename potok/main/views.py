from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .forms import Reg_from, Log_form

def mainpage(request):
    if request.user.is_authenticated:
        context = {'is_auth': True}
    else:
        form = Log_form()

        if request.method == 'POST':

            form = Log_form(request.POST)

            if form.is_valid():

                tg = form.cleaned_data['tg']
                user = authenticate(request, tg=tg)
                if user is not None:
                    login(request, user)
                    print(f'Юзер авторизировался')
                    return redirect('mainpage')
                else:
                    form.add_error(None, 'какие-то ошибки у малышки???)')


        context = {'is_auth': False, 'form': form}

    return render(request, 'main/mainpage.html', context)

def logout_user(r):
    logout(r)
    print(f'Юзер логаут blya')
    return redirect('mainpage')

def inf1(r):
    return render(r,'mainpage/inf1.html')

def reg(r):
    if r.method == 'POST':
        form = Reg_from(r.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('mainpage')
    else:
        form = Reg_from()

    return render(r, 'users/reg.html', {'form': form})