from missions import get_all_missions, search_missions_by_direction

def print_missions(missions_list):
    for i, mission in enumerate(missions_list, 1):
        print(f"{i}. {mission['name']}")
        print(f"   Год запуска: {mission['year']}")
        print(f"   Направление: {mission['direction']}\n")


def main():
    # 1. Выводим полный список миссий
    print("=== Каталог космических миссий ===")
    all_missions = get_all_missions()
    print_missions(all_missions)

    # 2. Спрашиваем направление
    search_query = input("Введите направление для поиска: ")

    # 3. Выводим результаты поиска
    found_missions = search_missions_by_direction(search_query)

    if found_missions:
        print(f"\n--- Найдены миссии по направлению '{search_query}' ---")
        print_missions(found_missions)
    else:
        # 4. Сообщение, если ничего не найдено
        print(f"\nМиссии по направлению '{search_query}' не найдены.")


if __name__ == "__main__":
    main()