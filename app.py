from flask import Flask

UPLOAD_FOLDER = 'E:/img_class/uploads'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
