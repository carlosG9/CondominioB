from django import forms

from .models import visits


class AdministratorForm(forms.ModelForm):

    class Meta:
        model = visits

        fields = [
            'rut',
            'name',
            'last_name',
            'tower',
            'department'
        ]

        labels = {
            'rut': 'Rut',
            'name': 'Nombre',
            'last_name': 'Apellido',
            'tower': 'Torre',
            'department': 'Departamento'
        }

        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control',
                                          'required': True, 'placeholder': 'Rut'},
                                   ),
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Nombre'}),
            'last_name':  forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Apellido'}),
            'tower':  forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Torre'}),
            'department':  forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Departamento'}),
        }
