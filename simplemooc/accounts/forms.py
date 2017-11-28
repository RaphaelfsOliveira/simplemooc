from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from core.utils import generate_hash_key
from core.mail import send_mail_template
from .models import PasswordReset

User = get_user_model()

#forms
class PasswordResetForm(forms.Form):

    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__exact=email):
            return email
        raise forms.ValidationError('Não existe usuário com este e-mail')

    def save(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(user=user, key=key)
        reset.save()
        template = 'accounts/password_reset_mail.html'
        subject = 'Criar nova senha no sistema'
        context = {
            'reset': reset,
        }
        send_mail_template(subject, template, context, [user.email])


class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password1 != password2:
            raise forms.ValidationError('As duas senhas não são identicas',
                                        code='password_mismatch')
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email']


class EditAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
