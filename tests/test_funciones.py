from prueba_repo01.funciones import sumar 

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0

def test_restar():
    from prueba_repo01.funciones import restar
    assert restar(5, 3) == 2
    assert restar(0, 0) == 0
    assert restar(-1, -1) == 0