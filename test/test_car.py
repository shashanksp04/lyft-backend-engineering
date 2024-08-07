import unittest
from datetime import datetime

from carfactory import Carfactory


class TestCalliope(unittest.TestCase):

    # Checking for the CapuletEngine when current mileage - last_serviced > 30000
    def test_engine_should_be_serviced(self):
        tire_wear = [0.5,0.6,0.7,0.4]
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_calliope(today, last_service_date, current_mileage, last_service_mileage,tire_wear)
        self.assertTrue(car.needs_service())

    # Checking for the CapuletEngine when current mileage - last_serviced < 30000
    def test_engine_should_not_be_serviced(self):
        tire_wear = [0.5,0.6,0.7,0.4]
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 2999
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_calliope(today, last_service_date, current_mileage, last_service_mileage,tire_wear = [0.5,0.6,0.7,0.4])
        self.assertFalse(car.needs_service())
    
    # Checking for the SplinderBattery when current date - last_service_date > 3 years
    def test_battery_should_be_serviced(self):
        tire_wear = [0.5,0.6,0.7,0.4]
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_calliope(today,last_service_date, current_mileage, last_service_mileage,tire_wear)
        self.assertTrue(car.needs_service())

    # Checking for the SplinderBattery when current date - last_service_date < 3 years
    def test_battery_should_not_be_serviced(self):
        tire_wear = [0.5,0.6,0.7,0.4]
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_calliope(today, last_service_date, current_mileage, last_service_mileage,tire_wear)
        self.assertFalse(car.needs_service())

    # checking for the Carrigan tires when one value is greater than or equal to 0.9
    def test_tire_should_be_serviced(self):
        tire_wear = [0.5,0.6,0.9,0.4]
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_calliope(today, last_service_date, current_mileage, last_service_mileage,tire_wear)
        self.assertFalse(car.needs_service())
    
    # checking for the Carrigan tires when no value is greater than or equal to 0.9
    def test_tire_should_not_be_serviced(self):
        tire_wear = [0.5,0.6,0.7,0.4]
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_calliope(today, last_service_date, current_mileage, last_service_mileage,tire_wear)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):

    # Checking for the WilloughbyEngine when current mileage - last_serviced > 60000
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())
    
    # Checking for the WilloughbyEngine when current mileage - last_serviced < 60000
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 5999
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())
    
    # Checking for the SplinderBattery when current date - last_service_date > 3 years
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_mileage = 0
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_glissade(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    # Checking for the SplinderBattery when current date - last_service_date < 3 years
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year)
        current_mileage = 0
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_glissade(today,last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    # Checking for the octoprime when the sum of all four values is greater than 3.0
    def test_tire_should_be_serviced(self):
        tire_wear = [0.5,0.8,0.9,0.9]
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_glissade(today, last_service_date, current_mileage, last_service_mileage,tire_wear)
        self.assertTrue(car.needs_service())

    # Checking for the octoprime when the sum of all four values is not greater than 3.0
    def test_tire_should_not_be_serviced(self):
        tire_wear = [0.4,0.3,0.5,0.7]
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year)
        current_mileage = 0
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_glissade(today,last_service_date, current_mileage, last_service_mileage,tire_wear)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):

    # Checking for the SternmanEngine when warning light is on
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True
        object = Carfactory()
        car = object.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    # Checking for the SternmanEngine when warning light is off
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().time()
        last_service_date = datetime.today().date()
        warning_light_is_on = False
        object = Carfactory()
        car = object.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())

    # Checking for the SplinderBattery when current date - last_service_date > 3 years
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        warning_light_is_on = False
        object = Carfactory()
        car = object.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())

    # Checking for the SplinderBattery when current date - last_service_date < 3 years
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        object = Carfactory()
        car = object.create_palindrome(today, last_service_date, warning_light_is_on)
        self.assertFalse(car.needs_service())
    
    # checking for the Carrigan tires when one value is greater than or equal to 0.9
    def test_tire_should_be_serviced(self):
        tire_wear = [0.5,0.6,0.9,0.4]
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        object = Carfactory()
        car = object.create_palindroem(today, last_service_date, warning_light_is_on,tire_wear)
        self.assertFalse(car.needs_service())
    
    # checking for the Carrigan tires when no value is greater than or equal to 0.9
    def test_tire_should_not_be_serviced(self):
        tire_wear = [0.5,0.6,0.7,0.4]
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        warning_light_is_on = False
        object = Carfactory()
        car = object.create_palindrome(today, last_service_date, warning_light_is_on,tire_wear)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):

    # Checking for the WilloughbyEngine when current mileage - last_serviced > 60000
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    # Checking for the WilloughbyEngine when current mileage - last_serviced < 60000
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 5999
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())
    
    # Checking for the NubinBattery when current date - last_service_date > 4 years
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 6)
        current_mileage = 0
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    # Checking for the NubinBattery when current date - last_service_date < 4 years
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_rorschach(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    # Checking for the octoprime when the sum of all four values is greater than 3.0
    def test_tire_should_be_serviced(self):
        tire_wear = [0.5,0.8,0.9,0.9]
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_rorschach(today, last_service_date, current_mileage, last_service_mileage,tire_wear)
        self.assertTrue(car.needs_service())

    # Checking for the octoprime when the sum of all four values is not greater than 3.0
    def test_tire_should_not_be_serviced(self):
        tire_wear = [0.4,0.3,0.5,0.7]
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year)
        current_mileage = 0
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_rorschach(today,last_service_date, current_mileage, last_service_mileage,tire_wear)
        self.assertFalse(car.needs_service())

class TestThovex(unittest.TestCase):
    
    # Checking for the CapuletEngine when current mileage - last_serviced > 30000
    def test_engine_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    # Checking for the CapuletEngine when current mileage - last_serviced < 30000
    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 2999
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    # Checking for the NubinBattery when current date - last_service_date > 4 years
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 7)
        current_mileage = 0
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_thovex(today,last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    # Checking for the NubinBattery when current date - last_service_date < 4 years
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_mileage = 0
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_thovex(today, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())
    
    # checking for the Carrigan tires when one value is greater than or equal to 0.9
    def test_tire_should_be_serviced(self):
        tire_wear = [0.5,0.6,0.9,0.4]
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_thovex(today, last_service_date, current_mileage, last_service_mileage,tire_wear)
        self.assertFalse(car.needs_service())
    
    # checking for the Carrigan tires when no value is greater than or equal to 0.9
    def test_tire_should_not_be_serviced(self):
        tire_wear = [0.5,0.6,0.7,0.4]
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 0
        object = Carfactory()
        car = object.create_thovex(today, last_service_date, current_mileage, last_service_mileage,tire_wear)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
