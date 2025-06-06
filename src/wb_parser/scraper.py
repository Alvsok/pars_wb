# wb_parser/scraper.py

import math
import httpx
from .wb_constants import BASE_URL
from .utils import random_user_agent


async def _request_wb(search: str, wb_page: int, color_codes: list[int] | None) -> dict:
    params = {
        "appType": 1, "curr": "rub", "dest": -1257786,
        "query": search, "resultset": "catalog",
        "sort": "popular", "page": wb_page, "limit": 100,  # WB максимум 100
    }
    if color_codes:
        params["fcolor"] = ";".join(map(str, color_codes))
    headers = {
        "accept-language": "ru-RU,ru;q=0.9",
        "user-agent": random_user_agent(),
    }
    async with httpx.AsyncClient(timeout=20) as cl:
        r = await cl.get(BASE_URL, params=params, headers=headers)
        r.raise_for_status()
        return r.json()


def _passes_price(prod: dict, low: int, high: int) -> bool:
    real = (prod["salePriceU"] - prod.get("logisticsCost", 0)) // 100
    prod["displayPrice"] = real
    return low <= real <= high


async def get_filtered_page(
    search: str,
    client_page: int,
    per_page: int,                    # ← новый аргумент
    min_price: int | None,
    max_price: int | None,
    color_codes: list[int] | None,
) -> dict:
    """Возвращает ровно `per_page` карточек (или меньше, если товаров нет)."""
    low = 0 if min_price is None else min_price
    high = math.inf if max_price is None else max_price

    need_until = client_page * per_page
    basket: list[dict] = []
    wb_page = 1

    while len(basket) < need_until:
        raw = await _request_wb(search, wb_page, color_codes)
        prods = raw.get("data", {}).get("products", [])
        if not prods:
            break
        basket.extend([p for p in prods if _passes_price(p, low, high)])
        wb_page += 1

    start = (client_page - 1) * per_page
    page_slice = basket[start: start + per_page]

    return {
        "page": client_page,
        "per_page": per_page,
        "returned": len(page_slice),
        "products": page_slice,
        "total_filtered_so_far": len(basket),
        "wb_pages_fetched": wb_page - 1,
    }
