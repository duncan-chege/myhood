from django.test import TestCase
from .models import *

class NeighbourhoodTest(TestCase):
    def test_string_representation(self):
        hood1 = Neighbourhood(hood_name='Jiji')
        self.assertEqual(str(hood1), hood1.hood_name)

    def setUp(self):
        self.new_hood = Neighbourhood(id=1, hood_name="Jiji",hood_location="Umoja",occupants=80)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_hood, Neighbourhood))
    
    

   