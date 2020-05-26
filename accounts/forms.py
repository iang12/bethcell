from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from core.choices import LIDER_CHOICES,SEXO_CHOICES
from members.models import Lider

class CustomUserCreationForm(UserCreationForm):
    tipo_lider =  forms.CharField(widget=forms.Select(choices=LIDER_CHOICES,
        attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}))
    lider      =  forms.ModelChoiceField(required = False,queryset=Lider.objects.all(),
        widget=forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition',
            'data-size':7,'data-live-search':'true'}))
    sexo       =  forms.ChoiceField(choices=SEXO_CHOICES,widget=forms.Select(
        attrs={'class':'selectpicker','data-style':'select-with-transition','data-size':7}))
    
    class Meta:
        model  = get_user_model()
        fields = (
            'username', 'first_name', 'last_name', 'password1', 
            'password2', 'email','is_cell_leader',
            'is_generation_leader','is_teacher'
        )
        widgets = { 
            'username':forms.TextInput(attrs={'class':'form-control','required':'true'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','required':'true'}),   
            'last_name':forms.TextInput(attrs={'class':'form-control','required':'true'}),   
            'email':forms.EmailInput(attrs={'class':'form-control','required':'true'}),    
            'password1':forms.PasswordInput(attrs={'class':'form-control','required':'true'}),    
            'password2':forms.PasswordInput(attrs={'class':'form-control','required':'true'}),    
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control',})  

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model  = get_user_model()
        fields = ('username', 'email','is_cell_leader','is_generation_leader','is_teacher')
