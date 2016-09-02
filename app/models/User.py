from system.core.model import Model
import re
import bcrypt

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self,id):
        query = "SELECT * from users where id = :id LIMIT 1"
        data = {'id': id}
        return self.db.query_db(query, data)

    def create_user(self, form):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        data = {'name':form['name'],
                'email':form['email'],
                'password':form['password'],
                'confirm':form['confirm']
                }
        if not data['name']:
            errors.append('Name cannot be blank')
        elif len(data['name']) < 2:
            errors.append('Name must be at least 2 characters long')
        elif not data['name'].isalpha():
            errors.append('Name must be letters only')
        if not data['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(data['email']):
            errors.append('Email format must be valid!')
        if not data['password']:
            errors.append('Password cannot be blank')
        elif len(data['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif data['password'] != data['confirm']:
            errors.append('Password and confirmation must match!')
        # If we hit errors, return them, else return True.
        if errors:
            return {"status": False, "errors": errors}
        else:
            # check if email already in db
            user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
            user_data = {'email': data['email']}
            user = self.db.get_one(user_query, user_data)
            if user:
                errors.append('Email is already in the system!')
                return {"status": False, "errors": errors}
            # insert user
            password = data['password']
            hashed_pw = self.bcrypt.generate_password_hash(password)
            data['pw_hash'] = hashed_pw
            query = query = "INSERT INTO users (pw_hash,name,email,created_at,updated_at) VALUES (:pw_hash,:name,:email,NOW(),NOW())"
            self.db.query_db(query,data)
            # Then retrieve the last inserted user.
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return { "status": True, "user": users[0] }

    def login_user(self, data):
        password = data['password']
        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        user_data = {'email': data['email']}
        # same as query_db() but returns one result
        user = self.db.get_one(user_query, user_data)
        print user
        if user:
           # check_password_hash() compares encrypted password in DB to one provided by user logging in
            if self.bcrypt.check_password_hash(user.pw_hash, password):
                return user
        # Whether we did not find the email, or if the password did not match, either way return False
        return False