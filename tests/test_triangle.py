import pytest
from mygeopy.triangle import hypot

def test_hypot():
    
    assert hypot(3,4) == 5
    assert hypot(9,12) == 15
    
    with pytest.raises(ValueError):
        hypot(-3,4)
    
    with pytest.raises(TypeError):
        hypot('3', 4)