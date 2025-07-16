from django import forms
from app.models import Book
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['image','title','author','description','genre','isbn','publication_date']
        widgets={
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Book Title',
            }),
            'author':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Author Name',}),
            'description':forms.Textarea(attrs={
                'class':'form-control',
                'rows':3,
                'placeholder':'Enter Book Description',
                }),
            'genre':forms.Select(attrs={
                'class':'form-control',
                }),
            'isbn':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter ISBN Number',
            }),
            'publication_date':forms.DateInput(attrs={
                'class':'form-control',
                    'type':'date',
                    }),
                
                
            
        }