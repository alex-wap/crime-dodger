from system.core.router import routes

routes['default_controller'] = 'Welcome'
routes['/about'] = 'Welcome#about'
routes['/login'] = 'Users#login'
routes['/logout'] = 'Users#logout'
routes['/users/<id>'] = 'Users#profile'
routes['/favorites/<id>/edit'] = 'Favorites#edit'
routes['/favorites/<id>'] = 'Favorites#delete'
routes['/favorites/<id>/destroy'] = 'Favorites#destroy'

routes['POST']['/favorites/<id>/show'] = 'Favorites#show'


routes['POST']['/favorites/<id>/add'] = 'Favorites#add'
routes['POST']['/users/create'] = 'Users#create'
routes['POST']['/users/login'] = 'Users#check_login'
 
routes['/place/<id>'] = 'Crimes#place'
