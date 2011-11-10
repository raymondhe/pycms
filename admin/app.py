import web
from admin import view, user, group, model, field, relation, template, category, entity

urls = (
        '', 'reindex',
        '/', view.index,
        '/login', view.login,
        '/logout', view.logout,
        '/submenu', view.submenu,
        '/curpos', view.curpos,

        '/user/index', user.index,
        '/user/add', user.add,
        '/user/(\d+)/edit', user.edit,
        '/user/(\d+)/editpwd', user.editpwd,
        '/user/(\d+)/delete', user.delete,

        '/group/index', group.index,
        '/group/add', group.add,
        '/group/(\d+)/edit', group.edit,
        '/group/(\d+)/delete', group.delete,

        '/model/index', model.index,
        '/model/add', model.add,
        '/model/(\d+)/edit', model.edit,
        '/model/(\d+)/delete', model.delete,
        '/model/(\d+)/create_table', model.create_table,
        '/model/(\d+)/drop_table', model.drop_table,

        '/field/index', field.index,
        '/field/add', field.add,
        '/field/(\d+)/edit', field.edit,
        '/field/(\d+)/delete', field.delete,

        '/relation/index', relation.index,
        '/relation/add', relation.add,
        '/relation/(\d+)/edit', relation.edit,
        '/relation/(\d+)/delete', relation.delete,

        '/template/index', template.index,
        '/template/add', template.add,
        '/template/(\d+)/edit', template.edit,
        '/template/(\d+)/delete', template.delete,

        '/category/index', category.index,
        '/category/add', category.add,
        '/category/(\d+)/edit', category.edit,
        '/category/(\d+)/delete', category.delete,
        '/category_tree', category.tree,

        '/entity/admin', entity.admin,
        '/(.+)/index', entity.index,
        '/(.+)/add', entity.add,
        '/(.+)/(\d+)/edit', entity.edit,
        '/(.+)/(\d+)/delete', entity.delete,
)


class reindex:
    def GET(self): raise web.seeother('/')

app_admin = web.application(urls, locals())
