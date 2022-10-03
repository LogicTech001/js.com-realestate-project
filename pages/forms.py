from django import forms
from .models import Plumbing
from django.forms.widgets import NumberInput
 
class PlumbingForm(forms.ModelForm):
    
    # date = forms.DateField(
        
    #     widget=forms.DateInput(
    #         attrs={'class': 'form-control', 'placeholder': '2006-10-25':00:00:00'}),
    #     input_formats=(
    #         '%Y-%m-%d',  # '2006-10-25'
    #         '%m/%d/%Y',  # '10/25/2006'
    #         '%m/%d/%y'
    #     )
    # )  # '10/25/06')
    
    full_name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name'
            }
        )
    )
    phone = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
             attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }
            )
    )
    flat_number = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
             attrs={
                'class': 'form-control',
                'placeholder': 'Enter flat number'
            }
            )
    )
    # type_of_services = forms.MultipleChoiceField(
    #     max_length=50,
    #     widget=forms.SelectMultiple(
    #          attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Select service'
    #         }
    #         )
    # )
    message = forms.CharField(
        widget=forms.Textarea(
           attrs={
              
                'class': 'form-control',
                'placeholder': 'Enter message',
                
            }
       
    )
    )
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'date', 'class': 'form-control'}
                
    
    )
    )
    time = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'time', 'class': 'form-control'}
                
    
    )
    )
    # goal = forms.ModelChoiceField(
        
    #     model_choice = forms.ModelChoiceField(
    #     queryset = Plumbing.objects.all(),
    #     initial = 0
    #     )
    # )
    
    class Meta:
        model = Plumbing
        fields = "__all__"
        
       

# Create your forms here.
