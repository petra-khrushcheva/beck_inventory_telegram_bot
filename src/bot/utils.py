def get_test_result(score) -> str:
    if 0 <= score <= 9:
        return f"{score} баллов. Отсутствие депрессивных симптомов."
    if 10 <= score <= 18:
        return f"{score} баллов. Субдепрессия, умеренная депрессия."
    if 19 <= score <= 29:
        return f"{score} баллов. Выраженная депрессия средней тяжести."
    if 30 <= score <= 63:
        return f"{score} баллов. Тяжелая депрессия."
    return (
        "Кажется при работе теста произошла ошибка. Пожалуйста, "
        "напишите об этом разработчикам: @FakeTelegramUsername"
    )
