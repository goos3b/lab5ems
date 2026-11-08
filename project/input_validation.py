"""
Валидация пользовательского ввода.
- Проверка границ через if-elif-else.
- Циклический ввод до корректного значения.
- Проверка типа через try/except ValueError.
- Защита от NaN и бесконечности.
- Ошибки логируются через logger.
"""
from __future__ import annotations

import math

from constants import (
    L_MIN, L_MAX,
    W_MIN, W_MAX,
    T_MIN, T_MAX,
    Q_MIN, Q_MAX,
)
from logger import log_error


def validate_range(value: float, low: float, high: float) -> tuple[bool, str]:
    """
    Проверка попадания value в [low, high] через if-elif-else.
    :return: (True, "") или (False, сообщение об ошибке)
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
    Проверяет тип (float) через try/except ValueError,
    отсекает NaN и бесконечность, затем проверяет границы.
    """
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            msg = f"Ошибка: введено не число ('{raw}')."
            print(msg)
            log_error(msg)
            continue

        if not math.isfinite(value):
            msg = f"Ошибка: введено недопустимое число ('{raw}')."
            print(msg)
            log_error(msg)
            continue

        ok, msg = validate_range(value, low, high)
        if ok:
            return value
        print(msg + " Повторите ввод.")
        log_error(msg)


def input_quantity() -> int:
    """
    Циклический ввод количества листов Q (шт), допустимо Q_MIN..Q_MAX.
    Количество должно быть целым числом. Порядок проверок:
    число -> конечность -> целое -> границы.
    """
    while True:
        raw = input(f"Введите количество листов Q, шт ({Q_MIN}..{Q_MAX}): ").strip()
        try:
            value = float(raw)
        except ValueError:
            msg = f"Ошибка: введено не число ('{raw}')."
            print(msg)
            log_error(msg)
            continue

        if not math.isfinite(value):
            msg = f"Ошибка: введено недопустимое число ('{raw}')."
            print(msg)
            log_error(msg)
            continue

        if not value.is_integer():
            msg = f"Ошибка: количество должно быть целым числом (введено: {raw})."
            print(msg)
            log_error(msg)
            continue

        int_value = int(value)
        ok, msg = validate_range(int_value, Q_MIN, Q_MAX)
        if ok:
            return int_value
        print(msg + " Повторите ввод.")
        log_error(msg)


def input_length() -> float:
    """Циклический ввод длины листа L (м), допустимо L_MIN..L_MAX."""
    return input_number(
        f"Введите длину листа L, м ({L_MIN}..{L_MAX}): ",
        L_MIN, L_MAX,
    )


def input_width() -> float:
    """Циклический ввод ширины листа W (м), допустимо W_MIN..W_MAX."""
    return input_number(
        f"Введите ширину листа W, м ({W_MIN}..{W_MAX}): ",
        W_MIN, W_MAX,
    )


def input_thickness() -> float:
    """Циклический ввод толщины листа t (мм), допустимо T_MIN..T_MAX."""
    return input_number(
        f"Введите толщину листа t, мм ({T_MIN}..{T_MAX}): ",
        T_MIN, T_MAX,
    )
