"""
Точка входа: ввод данных, расчёт массы, вывод результата.
Запускать ТОЛЬКО этот файл: python main.py
"""
from constants import STEEL_DENSITY
from logger import clear
from operations import calculate_mass, get_material_name, thickness_class
from input_validation import (
    input_length,
    input_width,
    input_thickness,
    input_quantity,
)
from menu import choose_material


def main() -> None:
    clear()  # очищаем журнал ошибок перед новым запуском

    print("--- Расчёт массы партии листов ---")
    print()

    # 1. Выбор материала (название + плотность)
    material_name, rho = choose_material()

    # 2. Ввод размеров и количества
    l = input_length()
    w = input_width()
    t = input_thickness()
    q = input_quantity()

    # 3. Расчёты
    mass = calculate_mass(l, w, t, rho, q)
    t_class = thickness_class(t)
    material_by_rho = get_material_name(rho)

    # 4. Вывод результата
    print()
    print("--- Результат ---")
    print(f"Материал:          {material_name}, плотность {rho} кг/м³")
    print(f"Размеры листа:     {l} м × {w} м × {t} мм")
    print(f"Количество:        {q} шт")
    print(f"Класс толщины:     {t_class}")
    print(f"Масса партии:      {mass:.2f} кг")


if __name__ == "__main__":
    main()
