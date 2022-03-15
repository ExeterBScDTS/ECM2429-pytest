import pytest
from unittest.mock import patch, MagicMock
import what3words

@patch('requests.get')
def test_w3w_to_coords(mock_get: MagicMock):

    coords = what3words.w3w_to_coords("just.a.test")
    mock_get.assert_called_once()


@patch('requests.get')
def test_w3w_from_coords(mock_get: MagicMock):

    words = what3words.w3w_from_coords('50.737508,-3.532954')
    mock_get.assert_not_called()


