from django.test import TestCase
from teretana.models import *


class Testmodels(TestCase):

    def setUp(self):
        self.plan1 = Plan.objects.create(
            naziv = "some-plan",
            cijena = "TestPrice",
            oznake = "TestTags",
        )

    def test_plan(self):
        self.assertEquals(self.plan1.name, "some-plan")