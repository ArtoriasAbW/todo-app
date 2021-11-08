from aiohttp import web
from handlers import auth, item, list


def get_routes():
    return [

        web.post('/auth/sign-up', auth.sign_up),
        web.post('/auth/sign-in', auth.sign_in),

        web.get('/lists', list.get_all_lists),
        web.get('/lists/{id}', list.get_list_by_id),
        web.post('/lists', list.create_list),
        web.put('/lists/{id}', list.update_list),
        web.delete('/lists/{id}', list.update_list),
        web.get('/lists/{id}/items', list.get_all_items),
        web.post('/lists/{id}/items', list.create_item),

        web.put('/items/{id}', item.update_item),
        web.get('/items/{id}', item.get_item_by_id),
        web.delete('/items/{id}', item.delete_item),
    ]
