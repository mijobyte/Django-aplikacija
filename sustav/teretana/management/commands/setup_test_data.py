import random
from django.utils import timezone
from django.db import transaction
from django.core.management.base import BaseCommand

from teretana.models import *
from teretana.factory import *

NUM_OZNAKAS = 20
NUM_PLANS = 10
NUM_TRENERS = 20
#NUM_PRETPLATNIKS = 100
#NUM_PRETPLATAS = 100

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Oznaka, Plan, Trener, Pretplatnik, Pretplata]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_OZNAKAS):
            oznaka = OznakaFactory()

        for _ in range(NUM_PLANS):
            plan = PlanFactory()

        for _ in range(NUM_TRENERS):
            trener = TrenerFactory()
        """
        for _ in range(NUM_PRETPLATNIKS):
            pretplatnik = PretplataFactory()

        for _ in range(NUM_PRETPLATAS):
            pretplata = PretplataFactory()
            """