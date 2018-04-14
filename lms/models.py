from django.db import models

# Create your models here.


class Books(models.Model):
    book_name=models.CharField(max_length=100)
    author_name=models.CharField(max_length=100)
    no_of_books=models.IntegerField()
    book_detail=models.TextField(default='text')
    book_image=models.FileField()

    def Claimbook(self):
        if self.no_of_books>1:
            self.no_of_books=self.no_of_books-1
            self.no_of_books.save()
        else:
            print("not enough books to Claim")


    def Addbook(self):
        self.no_of_books=self.no_of_books+1
        self.no_of_books.save()


    def __str__(self):
        return self.book_name






