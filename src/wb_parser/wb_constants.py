import random

BASE_URL = "https://search.wb.ru/exactmatch/ru/common/v4/search"

COLOR_MAP = {
    "белый": 16777215,
    "бежевый": 15794160,
    "голубой": 65407,
    "желтый": 16776960,
    "жёлтый": 16776960,
    "зеленый": 65280,
    "зелёный": 65280,
    "коричневый": 2763429,
    "красный": 16711680,
    "оранжевый": 16753920,
    "розовый": 16711935,
    "серый": 10526880,
    "синий": 255,
    "фиолетовый": 8388736,
    "черный": 0,
    "чёрный": 0,
}

USER_AGENT = (
    f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    f"AppleWebKit/537.36 (KHTML, like Gecko) "
    f"Chrome/12{random.randint(0,99)}.0.0.0 Safari/537.36"
)


PER_PAGE = 20
