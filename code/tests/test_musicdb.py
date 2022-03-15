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
    print(connect.mock_calls)
    assert True