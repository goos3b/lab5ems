
from validation import input_diameter, input_frequency
from menu import show_menu, select_mode, mode_name
from operations import cutting_speed, adjusted_speed, diameter_class


def main() -> None:
    """Главный сценарий."""
    print("=== Расчёт скорости резания при токарной обработке ===")

    while True:
        show_menu()
        k = select_mode()
        if k is None:
            print("Работа завершена.")
            break

        d = input_diameter()
        n = input_frequency()

        v = cutting_speed(d, n)
        v_adj = adjusted_speed(v, k)
        cls = diameter_class(d)

        print("\n Результаты ")
        print(f"Режим:        {mode_name(k)} (k = {k})")
        print(f"V (скорость резания):      {v:.2f} м/мин")
        print(f"V_adj (скорректированная): {v_adj:.2f} м/мин")
        print(f"Класс диаметра: {cls}")
        print("\n")


if __name__ == "__main__":
    main()
