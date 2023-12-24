
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms



class Expenses(models.Model):
    Expense_choices = [
        ('personal', 'Personal'),
        ('family', 'Family'),
        ('work', 'Work'),
        ('miscellaneous', 'Miscellaneous'),
    ]

    Category_choices=[
        ('fees','Fees'),
        ('transport','Transport'),
        ('communication','Communication'),
        
    ]



    title = models.CharField(max_length=200,choices=Expense_choices,default='action')
    amount= models.DecimalField(null=False, blank=False,max_digits=10,decimal_places=2,validators=[MinValueValidator(0.00),MaxValueValidator(float('inf'))])
    description = models.TextField(null=True, blank=True)
    date_added = models.DateField(auto_now=timezone.now(),null=True)
    date_completed= models.DateField(null=True)
    category= models.CharField(null=True, blank=True, max_length=50, choices = Category_choices)

    def __str__(self):
        return self.title
    

  

class Form(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['date_completed']
        widgets = {
            'date_completed': forms.TextInput(attrs={'type': 'date'})
        }

