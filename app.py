# from siteinfo import app
from flask import Flask

app = Flask(__name__, instance_relative_config=False)
app.config.from_object('config.Config')
app.config['SECRET_KEY'] = 'mysecretkey'
from core.views import core
app.register_blueprint(core)


if __name__ == "__main__":
    app.run(debug = True)
