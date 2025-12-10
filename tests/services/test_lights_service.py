import unittest
from unittest.mock import Mock

from app.services.lights_service import LightsService

class TestLightServiceToggle(unittest.TestCase):

    def setUp(self):
        self.mock_repo = Mock()
        self.service = LightsService(self.mock_repo)
    
    def test_toggle_off_to_on_bool(self):
        # Arrange
        self.mock_repo.get.return_value = {
            "id": 1, 
            "name": "Living Room", 
            "is_on": False, 
            "brightness": 0
        }

        # Act
        light = self.service.toggle_light(1)

        # Assert
        self.assertTrue(light["is_on"])

        self.mock_repo.get.assert_called_once_with(1)
        self.mock_repo.update.assert_called_once()

    def test_toggle_off_to_on_brightness(self):
        # Arrange
        self.mock_repo.get.return_value = {
            "id": 1, 
            "name": "Living Room", 
            "is_on": False, 
            "brightness": 0
        }

        # Act
        light = self.service.toggle_light(1)

        # Assert
        self.assertEqual(light["brightness"], 50)

        self.mock_repo.get.assert_called_once_with(1)
        self.mock_repo.update.assert_called_once()

    def test_toggle_on_to_off(self):
        # Arrange
        self.mock_repo.get.return_value = {
            "id": 3, 
            "name": "Kitchen", 
            "is_on": True, 
            "brightness": 75
        }
        
        # Act
        light = self.service.toggle_light(3)
        
        # Assert
        self.assertFalse(light["is_on"])
        self.assertEqual(light["brightness"], 0)
