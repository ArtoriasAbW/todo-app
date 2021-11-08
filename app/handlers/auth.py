from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response


async def sign_up(request: Request) -> Response:
    return web.json_response(status=200)


async def sign_in(request: Request) -> Response:
    return web.json_response(status=200)
