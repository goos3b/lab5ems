"""
Константы проекта: плотности материалов, границы ввода, пороги классификации.
"""
import math

# --- Плотности материалов (Вариант 2), кг/м³ ---
STEEL_DENSITY: float = 7850.0      # сталь
ALUMINUM_DENSITY: float = 2780.0   # алюминий
COPPER_DENSITY: float = 8900.0     # медь

# --- Допустимые диапазоны входных данных ---
L_MIN: float = 0.1    # длина листа, м
L_MAX: float = 5.0
W_MIN: float = 0.1    # ширина листа, м
W_MAX: float = 3.0
T_MIN: float = 0.1    # толщина листа, мм
T_MAX: float = 20.0
Q_MIN: int = 1        # количество листов, шт
Q_MAX: int = 1000

# --- Пороговые значения для классификации толщины ---
T_THIN_LIMIT: float = 0.5     # t < 0.5 — тонкий лист
T_THICK_LIMIT: float = 5.0    # t > 5.0 — толстый лист

# --- Число пи ---
PI: float = math.pi

# --- Файл журнала ошибок ---
LOG_FILE: str = "input_errors.log"
