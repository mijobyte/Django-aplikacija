import factory
import datetime
import factory.fuzzy
from factory.django import DjangoModelFactory
from teretana.models import *
from django.utils import timezone
from django.core.files.base import ContentFile
from django.contrib.auth.models import User 



class OznakaFactory(DjangoModelFactory):
    class Meta:
        model = Oznaka

    naziv = factory.Faker("first_name")


class PlanFactory(DjangoModelFactory):
    class Meta:
        model = Plan
        exclude = ('oznake')

    naziv = factory.Faker("first_name")
    cijena = factory.Faker("pyint", min_value = 0, max_value= 1000)
    oznake = factory.SubFactory(OznakaFactory)


class TrenerFactory(DjangoModelFactory):
    class Meta:
        model = Trener

    ime = factory.Faker("first_name")
    image = factory.LazyAttribute(
            lambda _: ContentFile(
                factory.django.ImageField()._make_data(
                    {'width': 1024, 'height': 768}
                ), 'example.jpg'
            )
        )
    """    
class PretplatnikFactory(DjangoModelFactory):
    class Meta: 
        model = Pretplatnik

    korisnik = factory.Iterator(User.objects.all())
    trener = factory.SubFactory(TrenerFactory)
    plan = factory.SubFactory(PlanFactory)
    datum_r = factory.Faker("date_time")
    spol = factory.fuzzy.FuzzyChoice(['Female', 'Male'])
    adresa = factory.Faker("sentence", nb_words = 3)
"""

