# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE 


DATABASE ="recipes_db"
    # model the class after the friend table from our database 
class table_name:
    def __init__(self , data):
        # ADD attributes for every column in our database table 
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # C
    @classmethod 
    def create(cls, data:dict) -> int:
        #add all column names and add all values
        query = "INSERT INTO table_name (column_name) VALUES (%(value_name)s);"
        return connectToMySql(DATABASE).query_db(query, data)

    # R
    @classmethod 
    def get_one(cls, data:dict) -> list:
        query = "SELECT * FROM table_name WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False 
        
    @classmethod 
    def get_one_by_email(cls, data:dict) -> list:
        
        query = "SELECT * FROM table_name WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False 

    @classmethod 
    def get_all(cls) -> list:
        query = "SELECT * FROM table_name;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_table_name = []
            for table_name_single in results:
                all_table_name.append(cls(table_name_single))
            return all_table_name
        return False

    # U
    @classmethod 
    def update_one(cls, data:dict) -> None:
        query = "UPDATE table_name SET column_name = %(column_name)s WHERE id = %(id)s;"
        return connectToMySQL(DATEBASE).query_db(query, data)

    # D 
    @classmethod 
    def delete_one(cls , data:dict) -> None:
        # ADD COLUMNS = values for every column that you wish to change in to db
        query= "DELETE FROM table_name WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validator(data:dict) -> bool:
        is_valid = True

        #some code logic here

        return is_valid 
