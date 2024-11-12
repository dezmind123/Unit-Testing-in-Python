# test_inputs.py
import unittest
from unittest.mock import patch
from main import get_symbol, get_chart_type, get_time_series, get_start_date, get_end_date

class TestInputs(unittest.TestCase):
    
    # Test for valid symbol
    def test_valid(self):
        with patch("builtins.input", return_value="AAPL"):
            self.assertEqual(get_symbol(), "AAPL")
    
    # Test for invalid symbol
    def test_invalid(self):
        with patch("builtins.input", return_value="aapl"):
            with self.assertRaises(ValueError):
                get_symbol()

        with patch("builtins.input", return_value="aapl2"):
            with self.assertRaises(ValueError):
                get_symbol()

        with patch("builtins.input", return_value="A"):
            self.assertEqual(get_symbol(), "A")

    # Test for valid chart type
    def test_chart_valid(self):
        with patch("builtins.input", return_value="1"):
            self.assertEqual(get_chart_type(), "1")
        
    # Test for invalid chart type
    def test_chart_invalid(self):
        with patch("builtins.input", return_value="3"):
            with self.assertRaises(ValueError):
                get_chart_type()

    # Test for valid time series
    def test_time_valid(self):
        with patch("builtins.input", return_value="3"):
            self.assertEqual(get_time_series(), "3")

    # Test for invalid time series
    def test_time_invalid(self):
        with patch("builtins.input", return_value="5"):
            with self.assertRaises(ValueError):
                get_time_series()

    # Test for valid start date
    def test_start_valid(self):
        with patch("builtins.input", return_value="10-15-2024"):
            self.assertEqual(get_start_date(), "10-15-2024")

    # Test for invalid start date
    def test_start_invalid(self):
        with patch("builtins.input", return_value="10-15-2024"):
            with self.assertRaises(ValueError):
                get_start_date()

    # Test for valid end date
    def test_end_valid(self):
        with patch("builtins.input", return_value="11-15-2024"):
            self.assertEqual(get_end_date(), "11-15-2024")

    # Test for invalid end date
    def test_end_date_invalid(self):
        with patch("builtins.input", return_value="11-15-2024"):
            with self.assertRaises(ValueError):
                get_end_date()



