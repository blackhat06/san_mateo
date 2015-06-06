from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class HomelessPeople(models.Model):
    Study = (
        ('1', 'Uneducated'),
        ('2', 'high school'),
        ('3', 'college'),
        ('4', 'Undergraduate'),
        ('5', 'graduate'),
        ('6', 'none of above')
    )
    Sex = (
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Prefer not to answer')
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=Sex, max_length=30)
    address = models.TextField()
    contact_number = models.IntegerField(null=True, blank=True)
    higher_studies = models.CharField(choices=Study, max_length=20)

    def __unicode__(self):
        return smart_unicode(self.first_name)


class Donators(models.Model):

    Sex = (
        ('1', 'Male'),
        ('2', 'Female'),
        ('3', 'Prefer not to answer')
    )

    Category = (
        ('1', 'Individual Person'),
        ('2', 'Individual Group'),
        ('3', 'Organization')
    )

    Mode = (
        ('1', 'delivery'),
        ('2', 'pick-up'),
    )

    name = models.CharField(max_length=50)
    address = models.TextField()
    contact_number = models.IntegerField(null=True, blank=True)
    date = models.DateField()
    email = models.EmailField()
    category = models.CharField(choices=Category, max_length=50)
    description_of_donation = models.TextField()
    mode_of_donation = models.CharField(choices=Mode, max_length=20)


    def __unicode__(self):
        return smart_unicode(self.first_name)



