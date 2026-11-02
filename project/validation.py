"""
Валидация пользовательского ввода.
- Проверка границ через if-elif-else.
- Циклический ввод до корректного значения.
"""

from __future__ import annotations

from connstans import D_MIN, D_MAX, N_MIN, N_MAX
from logger import log_error


def validate_range(value: float, low: float, high: float) -> tuple[bool, str]:
    """
    Проверка попадания value в [low, high] через if-elif-else.
    :return: (True, "") или (False, сообщение)
    """
    if value < low:
        return False, f"Ошибка: значение меньше нижней границы ({low})."
    elif value > high:
        return False, f"Ошибка: значение больше верхней границы ({high})."
    else:
        return True, ""


def input_number(prompt: str, low: float, high: float) -> float:
    """
    Циклически запрашивать число, пока не будет корректного.
    Проверяет тип (float) через try/except ValueError и границы.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError as e:
            msg = str(e.args[0]) if e.args else str(e)
            msg = f"Ошибка: введено не число ('{raw}'). {msg}"
            print(msg)
            log_error(msg)
            continue

        ok, msg = validate_range(value, low, high)
        if ok:
            return value
        print(msg + " Повторите ввод.")
        log_error(msg)


def input_diameter() -> float:
    """Циклический ввод диаметра заготовки D (мм), допустимо 1..500."""
    return input_number(
        "Введите диаметр заготовки D, мм (1..500): ",
        D_MIN, D_MAX,
    )


def input_frequency() -> float:
    """Циклический ввод частоты вращения n  () /мин), допустимо 50..3000."""
    return input_number(
        "Введите частоту вращения n, об/мин (50..3000): ",
        N_MIN, N_MAX,
    )