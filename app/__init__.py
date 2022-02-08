from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

#app = Flask(__name__,instance_relative_config=True)
app = Flask(__name__)

bootstrap = Bootstrap(app)

def create_app(config_name):
    


    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    #bootstrap.init_app(app)

# Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

# setting config
    from .requests import configure_request
    configure_request(app)

    # Will add the views and forms

return app
