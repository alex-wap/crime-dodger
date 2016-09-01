from system.core.controller import *

class Favorites(Controller):
    def __init__(self, action):
        super(Favorites, self).__init__(action)
        self.load_model('Crime')
        self.load_model('Favorite')
        self.load_model('User')
        self.db = self._app.db

    def edit(self,id):
      favorite=self.models['Favorite'].get_favorite(id)
      return self.load_view('/favorites/edit.html',favorite=favorite[0])