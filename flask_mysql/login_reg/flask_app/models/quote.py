from flask_app.config.mysqlconnection import connectToMySQL

db_name='quote_dash'


class Quote:
     def __init__(self, data):
        self.id=data['id']
        self.author=data['author']
        self.content=data['content']
        self.created_at=data['created_at']
        self.updated_at=data['update_at']

        self.poster_first_name=data['first_name']
        self.poster_last_name=data['last_name']
        self.poster_id=data['users.id']

    @classmethod
    def get_all_with_users(cls):
        query='''
        SELECT * from quotes 
        join users on users.id = quotes.user_id
        '''
        results=connectToMySQL(db_name).query_db(query)
        
        quotes=[]
        for row in results:
            quotes.append(cls(row))
        return quotes
        

    @classmethod
    def save():
        pass
