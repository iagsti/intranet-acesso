from django.test import TestCase
from django.db import models

from ..models import AccessModel


class CoreModelAccessTest(TestCase):
    def setUp(self):
        self.model = AccessModel()

    def test_is_model_instance(self):
        self.assertIsInstance(self.model, models.Model)

    def test_has_attributes(self):
        attributes = ('uuid', 'enabled', 'weekdays', 'period_to',
                      'period_from', 'time_to', 'time_from',
                      'institution', 'name', 'job', 'email',
                      'phone', 'doc_type', 'doc_number',
                      'answerable', 'observation', 'status',
                      'created_at', 'updated_at', 'created_by')

        for expected in attributes:
            with self.subTest():
                message = '{} not found.'.format(expected)
                self.assertTrue(hasattr(self.model, expected), msg=message)
