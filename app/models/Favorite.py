from system.core.model import Model

class Favorite(Model):
    def __init__(self):
        super(Favorite, self).__init__()

    def get_favorites(self,id):
        query = "SELECT * from favorites WHERE user_id = :id"
        data = {"id" : id}
        return self.db.query_db(query,data)

    def get_favorite(self,id):
        query = "SELECT * from favorites WHERE id = :id"
        data = {"id" : id}
        return self.db.query_db(query,data)

    def create_favorite(self,id,form):
        data = {
            'user_id' : id,
            'name' : form['name'],
            'location' : form['location']
        }
        if not data['name']:
            return False
        if not data['location']:
            return False
        query = "INSERT INTO favorites (name, user_id, location, created_at,updated_at) VALUES (:name, :user_id, :location, NOW(),NOW())"
        self.db.query_db(query, data)
        return True

    def update_favorite(self,data):
        sql = "UPDATE favorites SET name=:name, location=:location, updated_at=NOW() WHERE id = :id"
        self.db.query_db(sql, data)
        return True
    
    def delete_favorite(self,id):
        query = "DELETE FROM favorites WHERE id = :id"
        data = {'id':id}
        return self.db.query_db(query, data)

