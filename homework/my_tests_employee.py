import unittest
from homework.tests_simple_employee import Employee
from unittest import mock
from unittest.mock import patch
from homework import tests_simple_employee


class TestEmployee(unittest.TestCase):

    def setUp(self) -> None:
        self.employee = Employee("Volodymyr", "Bekar", 20)
        self.employee.raise_amt = 1.05

    def test_email(self):
        self.assertEqual(self.employee.email, "Volodymyr.Bekar@email.com")

    def test_fullname(self):
        self.assertEqual(self.employee.fullname, "Volodymyr Bekar")

    def test_apply_raise(self):
        self.employee.apply_raise()
        self.assertEqual(self.employee.pay, 21)

    # @mock.patch("homework.tests_simple_employee.monthly_schedule", return_value=True)
    def test_monthly_schedule_ok(self):
        with patch('tests_simple_employee.requests.get') as mock:
            mock.return_value.ok = False
            mock.return_value.text = "Done"

            schedule = self.employee.monthly_schedule("January")
            self.assertEqual(schedule, "Bad Response!")

        # month_shed = tests_simple_employee.monthly_schedule("January")
        # self.assertNotEqual(schedule, "Bad Response!")


if __name__ == "__main__":
    unittest.main(verbosity=2)
