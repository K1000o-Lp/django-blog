from django.db import models

class Person(models.Model):
  person_id = models.AutoField(primary_key=True)
  name_lastname = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  password = models.CharField(max_length=200)

class Post:
  post_id = models.AutoField(primary_key=True)
  person_fk = models.ForeignKey(Person, on_delete=models.RESTRICT)
  title = models.CharField(max_length=20)
  description = models.TextField()
  image = models.ImageField(null=True, upload_to=None)