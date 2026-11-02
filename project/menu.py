"""
Меню выбора режима обработки через match-case.
"""

from __future__ import annotations

from connstans import K_COARSE, K_SEMI, K_FINISH


def show_menu() -> None:
    """Вывести меню режимов."""
    print("\n Выберите режим обработки:")
    print("  1 — черновая обработка (k = 1.0)")
    print("  2 — получистовая      (k = 0.85)")
    print("  3 — чистовая          (k = 0.7)")
    print("  0 — выход")


def select_mode() -> float | None:
    """
    Циклически запрашивать режим и возвращать коэффициент k.

    Использует match-case для маршрутизации.
    Возвращает None, если выбран выход (0).
    """
    while True:
        choice = input("Введите номер режима (от 0 до 3): ").strip()
        match choice:
            case "1":
                return K_COARSE
            case "2":
                return K_SEMI
            case "3":
                return K_FINISH
            case "0":
                return None
            case _:
                print("Ошибка: неверный пункт меню. Повторите ввод.")


def mode_name(k: float) -> str:
    """Вернуть название режима по коэффициенту k."""
    match k:
        case 1.0:
            return "черновая"
        case 0.85:
            return "получистовая"
        case 0.7:
            return "чистовая"
        case _:
            return "неизвестный"