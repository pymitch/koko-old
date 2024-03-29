from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=50)
    sentence = models.CharField(max_length=300)
    def __str__(self):
        return self.word
    def parts(self):
        return self.sentence.split(self.word)
    def blank_space(self):
        return "_" * len(self.word)
        
        
class Input(models.Model):
    text = models.CharField(max_length=50)
    def __str__(self):
        return self.text

## trying to add a 'embedded' model for word list for each user
class UserWords(models.Model):
    #u = request.user
    user = models.ForeignKey(User)
    class user_word():
        text = models.CharField(max_length=50)
