from employee import Employee


def test_give_default_rise():
    """Teste com aumento no valor padrão """
    employee = Employee('gledson', 'cavalheiro', 15_000)
    employee.give_raise()
    assert employee.salario == 20_000

def test_give_custom_rise():
    """Teste com aumento no valor personalizado """
    employee = Employee('gledson', 'cavalheiro', 15_000)
    employee.give_raise(7_000)
    assert employee.salario == 22_000


