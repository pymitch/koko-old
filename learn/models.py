from django.db import models

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=50)
    sentence = models.CharField(max_length=300)
    def __str__(self):
        return self.word
    def parts(self):
        parts = self.sentence.split(self.word)
    def blank_space(self):
        blank_space = "_" * len(self.word)
        
        
class Input(models.Model):
    text = models.CharField(max_length=50)
    def __str__(self):
        return self.text
