from system.core.controller import *

class Favorites(Controller):
    def __init__(self, action):
        super(Favorites, self).__init__(action)
        self.load_model('Crime')
        self.load_model('Favorite')
        self.load_model('User')
        self.db = self._app.db

    def edit_page(self,id):
      favorite=self.models['Favorite'].get_favorite(id)
      return self.load_view('/favorites/edit.html',favorite=favorite[0])

    def delete_page(self,id):
      favorite=self.models['Favorite'].get_favorite(id)
      return self.load_view('/favorites/delete.html',favorite=favorite[0])

    def confirm_delete(self,id):
      favorite=self.models['Favorite'].delete_favorite(id)
      # return self.load_view('/profile.html', user=user[0])
      return redirect('/users/{}'.format(session['id']))


    def confirm_edit(self,id):
    	print id
    	data ={'id': id,'name': request.form['name'], 'location': request.form['location']}
    	favorite=self.models['Favorite'].update_favorite(data)
    	return redirect('/users/{}'.format(session['id']))    	  

