"""
Расчёты: скорость резания V, скорректированная V_adj, класс диаметра.
"""

from typing import Annotated

from connstans import PI, D_SMALL_LIMIT, D_LARGE_LIMIT


def cutting_speed(
    d: Annotated[float, "Диаметр заготовки, мм"],
    n: Annotated[float, "Частота вращения, об/мин"],
) -> float:
    """
    Рассчитать скорость резания V = π · D · n / 1000, м/мин.

    Args:
        d: диаметр заготовки, мм.
        n: частота вращения, об/мин.

    Returns:
        Скорость резания, м/мин.
    """
    return PI * d * n / 1000.0


def adjusted_speed(
    v: Annotated[float, "Скорость резания, м/мин"],
    k: Annotated[float, "Коэффициент режима"],
) -> float:
    """
    Скорректированная скорость V_adj = V · k.

    Args:
        v: скорость резания, м/мин.
        k: коэффициент режима.

    Returns:
        Скорректированная скорость, м/мин.
    """
    return v * k


def diameter_class(
    d: Annotated[float, "Диаметр, мм"],
) -> str:
    """
    Классифицировать диаметр через if-elif-else.

    D < 10 — малый диаметр;
    10 ≤ D ≤ 100 — нормальный диаметр;
    D > 100 — крупный диаметр.

    Args:
        d: диаметр, мм.

    Returns:
        Строка с названием класса диаметра.
    """
    if d < D_SMALL_LIMIT:
        return "малый диаметр"
    elif d <= D_LARGE_LIMIT:
        return "нормальный диаметр"
    else:
        return "крупный диаметр"