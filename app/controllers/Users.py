"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('Crime')
        self.load_model('User')
        self.db = self._app.db

    def login(self):
        return self.load_view('registration.html')

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
        flash('You have successfully signed in!')
        return redirect('/')

    def logout(self):
        session.clear()
        return redirect('/')