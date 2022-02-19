from flask import Flask
from blueprints.pages import pages_blueprint


app = Flask(__name__)
app.register_blueprint(pages_blueprint)


if __name__ == "__main__":
    app.run(debug=True)
