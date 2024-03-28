async def get_test_result(score) -> str:
    if 0 <= score <= 9:
        return f"{score} баллов. Отсутствие депрессивных симптомов."
    elif 10 <= score <= 18:
        return f"{score} баллов. Субдепрессия, умеренная депрессия."
    elif 19 <= score <= 29:
        return f"{score} баллов. Выраженная депрессия средней тяжести."
    elif 30 <= score <= 63:
        return f"{score} баллов. Тяжелая депрессия."
    else:
        return (
            "Кажется при работе теста произошла ошибка. Пожалуйста, "
            "напишите об этом разработчикам: @FakeTelegramUsername"
            )
