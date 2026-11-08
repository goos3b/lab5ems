"""
Расчёты: масса партии листов, название материала, класс толщины.
"""
from __future__ import annotations

from typing import Annotated

from constants import (
    STEEL_DENSITY,
    ALUMINUM_DENSITY,
    COPPER_DENSITY,
    T_THIN_LIMIT,
    T_THICK_LIMIT,
)


def calculate_mass(
    l: Annotated[float, "Длина листа, м"],
    w: Annotated[float, "Ширина листа, м"],
    t: Annotated[float, "Толщина листа, мм"],
    rho: Annotated[float, "Плотность материала, кг/м³"],
    q: Annotated[int, "Количество листов, шт"],
) -> float:
    """
    Рассчитать массу партии листов:
    m = L · W · (t / 1000) · ρ · Q, кг.
    """
    return l * w * (t / 1000.0) * rho * q


def get_material_name(rho: Annotated[float, "Плотность материала, кг/м³"]) -> str:
    """
    Определить название материала по плотности через if-elif-else.
    """
    if rho == STEEL_DENSITY:
        return "Сталь"
    elif rho == ALUMINUM_DENSITY:
        return "Алюминий"
    elif rho == COPPER_DENSITY:
        return "Медь"
    else:
        return "Неизвестный материал"


def thickness_class(t: Annotated[float, "Толщина листа, мм"]) -> str:
    """
    Классифицировать толщину листа через if-elif-else.

    t < 0.5 — тонкий лист;
    0.5 ≤ t ≤ 5.0 — нормальная толщина;
    t > 5.0 — толстый лист.
    """
    if t < T_THIN_LIMIT:
        return "тонкий лист"
    elif t <= T_THICK_LIMIT:
        return "нормальная толщина"
    else:
        return "толстый лист"
