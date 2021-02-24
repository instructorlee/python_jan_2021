from django.db import models

import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class BookManager(models.Manager):

    def validate(self, form):
        errors = {}
        if len(form['author']) < 2:
            errors['author'] = 'Author name must be at least 2 characters'

        if len(form['title']) < 2:
            errors['last_name'] = 'Title must be at least 2 characters'

        return errors


class Book(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=100)  # options: blank, null, default
    author = models.CharField(max_length=100)

    objects = BookManager()

    owner = models.ForeignKey('User', on_delete=models.CASCADE, related_name='my_books', null=True)  # in the dB, this stores the ID of the User
    # what kind of relationship is being created?

    checked_out_to = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, default=None)  # None == null
    # what kind of relationship is being created?

    likes = models.ManyToManyField('User', related_name='books')

    def __str__(self):  # usually only needed if using in admin
        return "{} by {}".format(self.title, self.author)


class UserManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['first_name']) < 2:
            errors['first_name'] = 'First Name must be at least 2 characters'

        if len(form['last_name']) < 2:
            errors['last_name'] = 'Last Name must be at least 2 characters'

        if not EMAIL_REGEX.match(form['email']):
            errors['email'] = 'Invalid Email Address'

        email_check = self.filter(email=form['email'])
        if email_check:
            errors['email'] = "Email already in use"

        if len(form['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'

        if form['password'] != form['confirm']:
            errors['password'] = 'Passwords do not match'

        return errors

    def authenticate(self, email, password):
        users = self.filter(email=email)
        if not users:
            return False

        user = users[0]
        return user if bcrypt.checkpw(password.encode(), user.password.encode()) else None

    def register(self, form):
        pw = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt()).decode()
        return self.create(
            first_name=form['first_name'],
            last_name=form['last_name'],
            email=form['email'],
            password=pw,
        )


class User(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    objects = UserManager()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


