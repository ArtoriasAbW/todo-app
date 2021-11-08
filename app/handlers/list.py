from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response


async def get_all_lists(request: Request) -> Response:
    return web.json_response(status=200)


async def get_list_by_id(request: Request) -> Response:
    return web.json_response(status=200)


async def update_list(request: Request) -> Response:
    return web.json_response(status=200)


async def create_list(request: Request) -> Response:
    return web.json_response(status=200)


async def get_all_items(request: Request) -> Response:
    return web.json_response(status=200)


async def create_item(request: Request) -> Response:
    return web.json_response(status=200)
