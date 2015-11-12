from django.test import TestCase
from service import common_service_modul
import unittest

# Create your tests here.

class Test_common_service_modul(unittest.TestCase):

  def test_compare_with_random(self):
      res = common_service_modul.getLucky(5)
      print(res)

      res = common_service_modul.getLucky(10)
      print(res)

