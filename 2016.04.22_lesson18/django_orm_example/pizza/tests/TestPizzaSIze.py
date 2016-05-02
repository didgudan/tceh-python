from django.test import TestCase
from pizza.models import PizzaIngredient

class TestPizzaIngredient(TestCase):
    def test_for_creation_ingredient(self):
        new_ingridient = PizzaIngredient(name = "test PizzaIngredient")
        new_ingridient.save()
        self.assertNotEqual(
            PizzaIngredient.objects.get(name="test PizzaIngredient".pk),
            None,
        )
