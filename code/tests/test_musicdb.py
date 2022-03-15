import pytest
from unittest.mock import patch, MagicMock
import musicdb


#@patch("sqlite3.connect")
#def test_MusicDB(connect: MagicMock):
#    db = musicdb.MusicDB("file://BAD")
#    assert isinstance(db, musicdb.MusicDB)

@patch("sqlite3.connect")
def test_MusicDB_get_album_names(connect: MagicMock):
    db = musicdb.MusicDB("file://BAD")
    db.get_album_names()
    # Checking if a method of a method... etc. has been called is possible,
    # but it requires some knowledge of what methods have been called.
    ## You can get a list by uncommenting the next two lines.
    # print(connect.mock_calls)
    # assert False
    ## The line to test for is
    ## 'call().__enter__().cursor().execute('SELECT DISTINCT album FROM tunes'
    ## Where thing() appears this translates to a mock of return_value.thing 

    cursor_mock: MagicMock = connect.return_value.__enter__.return_value.cursor.return_value
    cursor_mock.execute.assert_called_with("SELECT DISTINCT album FROM tunes")
