from aiohttp import web
from routes import get_routes
from settings import get_config


def setup_app():
    app = web.Application()
    app.router.add_routes(get_routes())
    return app


def main():
    config = get_config()
    app = setup_app()
    web.run_app(app, host=config['HOST'], port=config['PORT'])


if __name__ == '__main__':
    main()
