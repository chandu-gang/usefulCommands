

import sys
import pytest
from somfunc import *

def test_pytest():
	result = somefunc(10,10)
	assert result == 20
	