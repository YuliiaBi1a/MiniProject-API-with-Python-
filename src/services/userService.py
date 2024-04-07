from src.database.db_phpMySql import get_connection
from src.models.userModel import User

class UserService():
    
    @classmethod
    def get_user(cls):
        try:
            connection  = get_connection()
            print(connection)
            with connection.cursor() as cursor:
                #cursor.execute('SELECT * FROM user')
                cursor.callproc('select_user')
                result = cursor.fetchall()
                print(result)
                
            connection.close()
            return "Data base is close"
        
        except Exception as ex:
            print(ex)
    
    @classmethod
    def post_user(cls, user_table:User):
        try:
            connection  = get_connection()
            #print(connection)
            #id_user = user_table.id_user
            name_user = user_table.name_user
            password_user = user_table.password_user
            id_user_type = user_table.user_type
            dni_person =  user_table.person
            
            
            with connection.cursor() as cursor:
                #cursor.execute("INSERT INTO user(id_user, name_user, password_user, id_user_typeFK, dni_personFK) VALUES ({0}, '{1}', '{2}', {3}, {4})"
                               #.format(id_user,name_user,password_user,id_user_type,dni_person))
                cursor.callproc('insert_user', (name_user,password_user,id_user_type,dni_person))               
                connection.commit()
                print('User added successfully')
                
            connection.close()
            return "Data base is close"
        
        except Exception as ex:
            print(ex)    
            
                
    @classmethod
    def patch_user(cls, user_table:User):
        try:
            connection  = get_connection()
            
            id_user = user_table.id_user
            name_user = user_table.name_user
            password_user = user_table.password_user
            id_user_type = user_table.user_type
            dni_person =  user_table.person
            
            
            with connection.cursor() as cursor:
                cursor.callproc('update_user', (id_user,name_user,password_user,id_user_type,dni_person))               
                connection.commit()
                print('User updated successfully')
                
            connection.close()
            return "Data base is close"
        
        except Exception as ex:
            print(ex)    
            
    @classmethod
    def delete_user(cls, id_user): 
        try:
            connection  = get_connection()
            print(connection)
            
            with connection.cursor() as cursor:

                cursor.callproc('delete_user', (id_user,)) # Aqui uso otro metodo callproc para trabajar con procedimientos
                connection.commit()
                
            connection.close()
            return "Data base is close"
            
        except Exception as ex:
            print(ex)