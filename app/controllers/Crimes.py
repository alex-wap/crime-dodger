"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Crimes(Controller):
    def __init__(self, action):
        super(Crimes, self).__init__(action)
        self.load_model('Crime')
        self.load_model('Favorite')
        self.load_model('User')
        self.db = self._app.db

    def index(self):
        """
        A loaded model is accessible through the models attribute
        self.models['WelcomeModel'].get_users()

        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask

        # return self.load_view('index.html', messages=messages, user=user)
        """
        crimes=self.models['Crime'].get_crimes()
        return self.load_view('crimes/index.html',crimes=crimes)

    # def createMapData(self):
    #     crimes=self.models['Crime'].get_crimes()
    #     return jsonify(crimes)

    def jquery(self):
        return self.load_view('crimes/jquery_test.html')

    def marker(self):
        crimes=self.models['Crime'].get_crimes()
        return self.load_view('crimes/simple_marker.html',crimes=crimes)

    def marker2(self):
        crimes=self.models['Crime'].get_crimes()
        return self.load_view('crimes/marker2.html',crimes=crimes)

    def directions(self):
        crimes=self.models['Crime'].get_crimes()
        return self.load_view('crimes/directions.html',crimes=crimes)

    def directions2(self):
        crimes=self.models['Crime'].get_crimes()
        return self.load_view('crimes/directions2.html',crimes=crimes)
