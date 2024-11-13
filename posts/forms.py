from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, label='Введите логин')
    password = forms.CharField(min_length=4, max_length=20, label='Введите пароль')


# class RegistrationForm(forms.Form):
#     username = forms.CharField(max_length=20, label='Введите логин')
#     password = forms.CharField(min_length=4, max_length=10, label='Введите пароль')
#     repeat_password = forms.CharField(min_length=4, max_length=10, label='Повторите пароль')


class CreatePost(forms.Form):
    title = forms.CharField(max_length=100, label='Введите заголовок')
    body = forms.CharField(widget=forms.Textarea, label='Напишите пост')
