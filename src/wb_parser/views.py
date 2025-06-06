# wb_parser/views.py
from django.http import JsonResponse, HttpRequest
from .wb_constants import PER_PAGE
from .scraper import get_filtered_page
from .utils import parse_color_list


async def parser_view(request: HttpRequest):
    search = request.GET.get("search")
    if not search:
        return JsonResponse({"error": "`search` is required"}, status=400)

    # ── номер страницы ───────────────────────────────────────────────
    try:
        client_page = max(1, int(request.GET.get("page", "1")))
    except ValueError:
        return JsonResponse({"error": "`page` must be positive int"}, status=400)

    # ── сколько товаров на страницу ─────────────────────────────────
    try:
        per_page = int(request.GET.get("per_page", "100"))
        if per_page < 1 or per_page > 100:
            raise ValueError
    except ValueError:
        return JsonResponse({"error": "`per_page` must be 1…100"}, status=400)

    color_codes = parse_color_list(request.GET.get("color"))

    try:
        min_r = int(request.GET["min"]) if "min" in request.GET else None
        max_r = int(request.GET["max"]) if "max" in request.GET else None
    except ValueError:
        return JsonResponse({"error": "`min`/`max` must be int"}, status=400)

    data = await get_filtered_page(
        search=search,
        client_page=client_page,
        per_page=PER_PAGE,
        min_price=min_r,
        max_price=max_r,
        color_codes=color_codes,
    )
    return JsonResponse(data, json_dumps_params={"ensure_ascii": False})
