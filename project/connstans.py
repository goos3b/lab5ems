import math

# --- Коэффициенты режима обработки (Вариант 1) ---
K_COARSE: float = 1.0    # черновая обработка
K_SEMI: float = 0.85     # получистовая
K_FINISH: float = 0.7    # чистовая

# --- Допустимые диапазоны входных данных ---
D_MIN: float = 1.0
D_MAX: float = 500.0
N_MIN: float = 50.0
N_MAX: float = 3000.0

# --- Пороговые значения для классификации диаметра ---
D_SMALL_LIMIT: float = 10.0     # D < 10 — малый
D_LARGE_LIMIT: float = 100.0    # D > 100 — крупный

# --- Число пи ---
PI: float = math.pi

# --- Файл журнала ошибок ---
LOG_FILE: str = "input_errors.log"