from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
# Create your models here.
class Book(models.Model):
    GENRE_CHOICES = [
        ('SCRIPTURE','Scripture'),
        ('FICTION', 'Fiction'),
        ('NON-FICTION', 'Non-fiction'),
        ('MYSTERY', 'Mystery'),
        ('SCIENCE FICTION', 'Science Fiction'),
        ('ROMANCE', 'Romance'),
        ('HORROR', 'Horror'),
        ('BIOGRAPHY', 'Biography'),
        ('POETRY', 'Poetry'),
        ('OTHER','other'),
        
    ]
    image = models.ImageField(upload_to='books/')

    title=models.CharField(max_length=300)
    author=models.CharField(max_length=300)
    description=models.TextField()
    genre=models.CharField(max_length=30,choices=GENRE_CHOICES)
    isbn=models.CharField('ISBN',max_length=12,unique=True)
    publication_date=models.DateField()
    average_rating=models.DecimalField(max_digits=3,decimal_places=3,validators=[MinValueValidator(0),MaxValueValidator(5)],default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('book-detail',kwargs={'pk':self.pk})