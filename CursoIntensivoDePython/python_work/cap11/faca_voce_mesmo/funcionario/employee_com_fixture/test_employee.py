import pytest
from employee import Employee


@pytest.fixture
def employee():
    funcionario = Employee('gledson', 'cavalheiro', 15_000)
    return funcionario


def test_give_default_rise(employee):
    """Teste com aumento no valor padrão """
    employee.give_raise()
    assert employee.salario == 20_000


def test_give_custom_rise(employee):
    """Teste com aumento no valor personalizado """
    employee.give_raise(7_000)
    assert employee.salario == 22_000


