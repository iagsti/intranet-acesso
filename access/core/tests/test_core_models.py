from django.test import TestCase
from django.db import models

from ..models import AccessModel


class CoreModelAccessTest(TestCase):
    def setUp(self):
        self.model = AccessModel()

    def test_is_model_instance(self):
        self.assertIsInstance(self.model, models.Model)
