from ideas import show_ideas, add_idea

ideas_list = [
    {
        "name": "Трекер привычек",
        "topic": "Консольное приложение",
        "difficulty": "Средняя"
    },
    {
        "name": "Космическая викторина",
        "topic": "Игра",
        "difficulty": "Лёгкая"
    },
    {
        "name": "Планировщик задач",
        "topic": "Организация времени",
        "difficulty": "Средняя"
    }
]

show_ideas(ideas_list)

answer = input("Добавить новую идею? (да/нет): ").strip().lower()

if answer == "да":
    name = input("Название: ")
    topic = input("Тема: ")
    difficulty = input("Сложность: ")

    add_idea(ideas_list, name, topic, difficulty)

    show_ideas(ideas_list)