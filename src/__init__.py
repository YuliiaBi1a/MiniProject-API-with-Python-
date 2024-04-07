from flask import Flask
from .routes import userRouter


app = Flask( __name__ )

def init_app(config):
    app.config.from_object(config)
    
    app.register_blueprint(userRouter.main, url_prefix='/user')
    #app.register_blueprint(user_typeRouter.main, url_prefix='/user_type')
    #app.register_blueprint(personRouter.main, url_prefix='/person')
    return app