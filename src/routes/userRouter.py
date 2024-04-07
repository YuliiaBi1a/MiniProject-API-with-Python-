from flask import Blueprint,  request
from src.services.userService import UserService
from src.models.userModel import User

main = Blueprint('miniproject_blueprint', __name__)

@main.route('/', methods = ['GET','POST','PATCH','DELETE'])
def manage_user():
    
    if request.method == "GET":
        get_user = UserService.get_user()
        print(get_user)
    
    elif request.method == "POST":
        name_user = request.json['name_user']
        password_user = request.json['password_user']
        id_user_type = request.json['id_user_type']
        dni_person = request.json['dni_person']   
        
        user_table = User(0,name_user,
                                password_user, 
                                id_user_type,
                                dni_person)
        
        post_user = UserService.post_user(user_table)
        print(post_user)
        
        
    elif request.method == "PATCH": 
        id_user = request.json['id_user']
        name_user = request.json['name_user']
        password_user = request.json['password_user']
        id_user_type = request.json['id_user_type']
        dni_person = request.json['dni_person']
       
        user_table = User(id_user,
                        name_user,
                        password_user, 
                        id_user_type,
                        dni_person)

        patch_user = UserService.patch_user(user_table)
        print(patch_user) 
    
    elif request.method == "DELETE":
        id_user = request.json['id_user']
        delete_user = UserService.delete_user(id_user)
        print(delete_user)  
           
    print('Esto se imprime en consola')
    return 'Esto se ve en la pagina'