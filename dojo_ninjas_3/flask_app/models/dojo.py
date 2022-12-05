from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id=data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.ninjas=[]

    @classmethod
    def get_all(cls):
        query= 'SELECT * FROM dojos;'

        results= connectToMySQL('dojo_ninjas_3').query_db(query)
        dojos=[]

        for datas in results:
            dojos.append(cls(datas))
        return dojos

    @classmethod
    def save(cls,data):
        query= 'INSERT INTO dojos (name) VALUES (%(name)s)'
        result= connectToMySQL('dojo_ninjas_3').query_db(query,data)
        return result

    @classmethod
    def get_ninja_datas(cls,data):
        query='SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results= connectToMySQL('dojo_ninjas_3').query_db(query,data)
        print(results)

    #  I am having trouble with this new part here. I am not sure why this part is not working in my code. 
        dojo= cls(results[0])
        for row in results:
            nin={
                'id': row['ninjas.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
        dojo.ninjas.append(Ninja(nin))
        return dojo
