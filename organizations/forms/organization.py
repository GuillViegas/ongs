from django import forms

from core.models.organizations import Organization

class OrganizationRegister(forms.Form):
    name = forms.CharField(
        max_length=120, 
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nome da Intituição',
                'class': 'form-control'
            }
        )
    )

    site = forms.URLField(
        required=False,
        widget=forms.URLInput(
            attrs={
                'placeholder': 'Site',
                'class': 'form-control'
            }
        )
    )

    presentation = forms.CharField(
        max_length=1500,
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Apresentação',
                'class': 'form-control'
            }
        )
    )
    
    phone = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Telefone de contato',
                'class': 'form-control'
            }
        )
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email de contato',
                'class': 'form-control'
            }
        )
    )

    action_areas = forms.MultipleChoiceField(
        required=True,
        label='Áreas de atuação',
        choices=Organization.ActionArea.choices(),
        widget=forms.CheckboxSelectMultiple(
        )
    )

    logo = forms.ImageField()

class AddressForm(forms.Form): 
    cep = forms.CharField(
        label="Cep",
        max_length=9, 
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'cep',
                'class': 'form-control'
            }
        )
    )

    location = forms.CharField(
        label="Endereço",
        max_length=150,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Endereço',
                'class': 'form-control'
            }
        )
    )

    number = forms.CharField(
        label="Número",
        max_length=10,
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Número',
                'class': 'form-control'
            }
        )
    )
    
    complement = forms.CharField(
        label="Complemento",
        max_length=256,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Complemento',
                'class': 'form-control'
            }
        )
    )

    neighborhood = forms.EmailField(
        label="Bairro",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Bairro',
                'class': 'form-control'
            }
        )
    )

    city = forms.EmailField(
        label="Cidade",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Cidade',
                'class': 'form-control'
            }
        )
    )

    state = forms.EmailField(
        label="Estado",
        max_length=50,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Estado',
                'class': 'form-control'
            }
        )
    )