from src.main import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(1,3) == 4
    
def test_sub():
    assert sub(5,1) == 4
    assert sub(9,6) == 3