from flask import Flask

from extensions import db
from router import main


def CreateApp(ConfigFile='settings.py'):
    app = Flask(__name__)

    # Set Config File
    app.config.from_pyfile(ConfigFile)

    db.init_app(app)
    app.register_blueprint(main)
    return app


App = CreateApp()
if __name__ == '__main__':
    App.run(debug=True)
