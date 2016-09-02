from system.core.router import routes

routes['default_controller'] = 'Welcome'
routes['/login'] = 'Users#login'
routes['/logout'] = 'Users#logout'
routes['/users/<id>'] = 'Users#profile'
routes['/update_favorites/<id>'] = 'Favorites#edit'
routes['/delete_favorites/<id>'] = 'Favorites#delete'
routes['/confirm_delete/<id>'] = 'Favorites#confirm_delete'

routes['POST']['/confirm_edit/<id>'] = 'Favorites#confirm_edit'


routes['POST']['/users/<id>/add'] = 'Users#add'
routes['POST']['/users/create'] = 'Users#create'
routes['POST']['/users/login'] = 'Users#check_login'
routes['/delete_page/<id>'] = 'Favorites#delete_page'
routes['/edit_page/<id>'] = 'Favorites#edit_page'
 
routes['/place/<id>'] = 'Crimes#place'
