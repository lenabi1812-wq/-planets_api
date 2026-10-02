def show_ideas(ideas):
    print("\n=== Каталог идей для Python-проектов ===")
    for index, idea in enumerate(ideas, 1):
        print(f"\n{index}. {idea['name']}")
        print(f"Тема: {idea['topic']}")
        print(f"Сложность: {idea['difficulty']}")
    print("-" * 40)

def add_idea(ideas, name, topic, difficulty):
    new_idea = {
        "name": name,
        "topic": topic,
        "difficulty": difficulty
    }
    ideas.append(new_idea)
    print("Идея добавлена!")