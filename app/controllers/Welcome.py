from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')
        self.load_model('Crime')
        self.db = self._app.db

    def index(self):
        crimes=self.models['Crime'].get_crimes()
        return self.load_view('index.html',crimes=crimes)

    def about(self):
        return self.load_view('about.html')