from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('Crime')
        self.load_model('Favorite')
        self.load_model('User')
        self.db = self._app.db

    def login(self):
        return self.load_view('registration.html')
    def splash(self):
        return self.load_view('splash.html')
    def create(self):
        create_status = self.models['User'].create_user(request.form)
        if create_status['status'] == True:
            session['id'] = create_status['user']['id']
            session['name'] = create_status['user']['name']
            return redirect('/')
        else:
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            return redirect('/login')
    def check_login(self):
        user = self.models['User'].login_user(request.form)
        if not user:
            flash("Your login information is incorrect. Please try again.")
            return redirect('/login')
        session['id'] = user['id']
        session['name'] = user['name']
        return redirect('/')

    def logout(self):
        session.clear()
        return redirect('/')

    def profile(self,id):
        user=self.models['User'].get_user(id)
        favorites=self.models['Favorite'].get_favorites(id)
        return self.load_view('profile.html',user=user[0],favorites=favorites)

    def add(self,id):
        valid = self.models['Favorite'].create_favorite(id,request.form)
        if valid == False:
            flash('Name and Location cannot be blank!')
        return redirect('/users/{}'.format(id))

    def userfavorite(self,id):
        user=self.models['User'].get_user(id)
        favorites=self.models['Favorite'].get_favorites(id)
        return self.load_view('profile.html',user=user[0],favorites=favorites)

    def delete(self,id):
        return self.load_view('delete.html', user=user[0], favorites=favorites)
