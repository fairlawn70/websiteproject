from flask import Flask

from views import views

app = Flask(__name__)
app.secret_key = "How We Doin?"
app.register_blueprint(views, url_preifx ="/")
if __name__ == '__main__':
    app.run(debug = True, port = 70, host = '0.0.0.0')
