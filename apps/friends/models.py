from __future__ import unicode_literals
from django.db import models
import bcrypt

class UserManager(models.Manager):
    def validateRegistration(self, form_data):
        errors = []

        if len(form_data['first_name']) == 0:
            errors.append("First name is required")

        if len(form_data['last_name']) == 0:
            errors.append("Last name is required")

        if len(form_data['email']) == 0:
            errors.append("Email is required")

        if len(form_data['password']) == 0:
            errors.append("Password is required")

        if form_data['password'] != form_data['confirm_password']:
            errors.append("Passwords do not match")

        return errors

    def createUser(self, form_data):
        password = str(form_data['password'])
        hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())

        user = User.objects.create(
            first_name = form_data['first_name'],
            last_name = form_data['last_name'],
            email = form_data['email'],
            password = hashed_pw
        )

        return user

    def validateLogin(self, form_data):
        errors = []

        if len(form_data['email']) == 0:
            errors.append("Email is required")

        if len(form_data['password']) == 0:
            errors.append("Password is required")

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    friends = models.ManyToManyField("self")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
