from django.shortcuts import render,redirect
from app.forms import BookForm
from app.models import Book
from django.contrib import messages

# Create your views here.
def book_create(req):
    if req.method == 'POST':
        form = BookForm(req.POST, req.FILES)  # 🟢 Include req.FILES here
        if form.is_valid():
            form.save()
            messages.success(req, "Book created Successfully")
            return redirect('book-list')
    else:
        form = BookForm()
    return render(req, 'app/book_form.html', {'form': form})

   
def book_list(req):
    books=Book.objects.all().order_by('-created_at')
    return render(req,'app/book_list.html',{'books':books})
def book_detail(req,pk):
    book=Book.objects.get(pk=pk)
    return render(req,'app/book_detail.html',{'book':book})
def book_update(req, pk):
    book = Book.objects.get(pk=pk)
    if req.method == 'POST':
        form = BookForm(req.POST, req.FILES, instance=book)  # 🟢 Include req.FILES here
        if form.is_valid():
            form.save()
            messages.success(req, "Book updated Successfully")
            return redirect('book-update', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(req, 'app/book_form.html', {'form': form})

def book_delete(req,pk):
    book=Book.objects.get(pk=pk)
    
    book.delete()
    messages.success(req,"Book deleted Successfully")
    return redirect('book-list')

       