import pytest

from src.decorators import log


# Тестируемую функцию
@log(filename=None)  # Логи будут выводиться в консоль
def add(x, y):
    return x + y


@log(filename=None)
def divide(x, y):
    return x / y


def test_add(capsys):
    result = add(2, 3)

    # Перехватываем вывод
    captured = capsys.readouterr()

    # Проверяем что результат правильный
    assert result == 5
    # Проверяем, что в консоль записались правильные строки
    assert "Starting add with args: (2, 3)" in captured.out
    assert "add ok. Result: 5" in captured.out


def test_divide(capsys):
    result = divide(10, 2)

    captured = capsys.readouterr()

    assert result == 5
    assert "Starting divide with args: (10, 2)" in captured.out
    assert "divide ok. Result: 5.0" in captured.out


def test_divide_by_zero(capsys):
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()

    assert "Starting divide with args: (1, 0)" in captured.out
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in captured.err


# Тест для лога в файл
def test_logging_to_file(tmpdir):
    log_file = tmpdir.join("test_log.txt")

    @log(filename=str(log_file))
    def multiply(x, y):
        return x * y

    result = multiply(3, 4)
    assert result == 12

    with open(log_file) as f:
        log_contents = f.read()
        assert "Starting multiply with args: (3, 4)" in log_contents
        assert "multiply ok. Result: 12" in log_contents

# Для запуска тестов откройте терминал и выполните:
# pytest test_decorators.py
