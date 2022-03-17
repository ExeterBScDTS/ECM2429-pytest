# ECM2429-pytest
## Pytest examples


## Notes
It's possible to patch built-in functions.

'''python
@patch("__builtins__.open")
def test_myfilecode(mock_open: MagicMock):
...
'''
