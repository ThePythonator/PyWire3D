from PyWire3D.Utilities.Vector import add

def test_vector_add():
    assert add([1,2,3], [2,4,5], [-2,-3,1]) == [1,3,9]