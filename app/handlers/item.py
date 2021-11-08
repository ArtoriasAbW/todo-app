from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response


async def update_item(request: Request) -> Response:
    return web.json_response(status=200)


async def get_item_by_id(request: Request) -> Response:
    return web.json_response(status=200)


async def delete_item(request: Request) -> Response:
    return web.json_response(status=200)
