from src_pullreq.src_pullreq import add
import pytest

def test_add():
     r=add(2,3)
     assert r == 6
