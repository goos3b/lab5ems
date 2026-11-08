"""
Меню выбора материала.
"""
from __future__ import annotations

from constants import STEEL_DENSITY, ALUMINUM_DENSITY, COPPER_DENSITY


def choose_material() -> tuple[str, float]:
    """
    Предложить выбрать материал. Возвращает (название, плотность).
    """
    print("Выберите материал:")
    print("1 — Сталь")
    print("2 — Алюминий")
    print("3 — Медь")

    while True:
        choice = input("Номер материала (1..3): ").strip()
        if choice == "1":
            return "Сталь", STEEL_DENSITY
        elif choice == "2":
            return "Алюминий", ALUMINUM_DENSITY
        elif choice == "3":
            return "Медь", COPPER_DENSITY
        else:
            print("Ошибка: введите 1, 2 или 3.")
