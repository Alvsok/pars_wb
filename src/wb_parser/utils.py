import random
from .wb_constants import COLOR_MAP


def parse_color_list(raw: str | None) -> list[int]:
    if not raw:
        return []
    names = [c.strip().lower() for c in raw.split(",")]
    return [COLOR_MAP[n] for n in names if n in COLOR_MAP]


_UA_POOL: list[str] = [
    # ─── Chrome Windows ────────────────────────────────────────────────
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/114.0.5735.199 Safari/537.36",

    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/115.0.5790.110 Safari/537.36",

    # ─── Chrome Linux ──────────────────────────────────────────────────
    "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/113.0.5672.126 Safari/537.36",

    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/117.0.5938.92 Safari/537.36",

    # ─── Safari macOS ─────────────────────────────────────────────────
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) "
    "Version/16.4 Safari/605.1.15",

    # ─── Safari iPhone ────────────────────────────────────────────────
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) "
    "Version/17.0 Mobile/15E148 Safari/604.1",

    # ─── Firefox Windows ──────────────────────────────────────────────
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) "
    "Gecko/20100101 Firefox/118.0",

    # ─── Firefox Linux ────────────────────────────────────────────────
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:117.0) "
    "Gecko/20100101 Firefox/117.0",
]


def random_user_agent() -> str:
    return random.choice(_UA_POOL)
