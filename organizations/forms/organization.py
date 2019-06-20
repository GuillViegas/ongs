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

    action_area = forms.MultipleChoiceField(
        required=True,
        label='Áreas de atuação',
        choices=Organization.ActionArea.choices(),
        widget=forms.CheckboxSelectMultiple(
        )
    )

    logo = forms.ImageField()
