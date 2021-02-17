from shutil import rmtree
from utils import increm


def test_increm_numbered():
    assert increm("abc1.txt") == "abc2.txt"
    assert increm("34abc12def1234.txt") == "34abc12def1235.txt"
    assert increm("34abc12def-1.txt") == "34abc12def-2.txt"
    assert increm(increm("abc1.txt")) == "abc3.txt"

def test_increm_not_numbered():
    assert increm("abc.txt") == "abc2.txt"
    assert increm("34cou12cou.txt") == "34cou12cou2.txt"

def test_path():
