import functools
import os
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug import secure_filename

from flaskr.db import get_db

bp = Blueprint('upload', __name__, url_prefix='/upload')

UPLOAD_FOLDER = 'static/image'
basedir = os.path.abspath(os.path.dirname(__file__))

@bp.route('/success', methods=('GET', 'POST'))
def uploadr():
    if request.files['file']:
        file_dir = os.path.join(basedir, UPLOAD_FOLDER)
        file = request.files['file']
        user = request.files['user']
        file.save(os.path.join(file_dir, file.filename))
        user.save(os.path.join(file_dir, user.filename))
        return render_template('uploadsuccess.html', fname=file.filename)
    else :
        return render_template('uploadfail.html')

@bp.route('/', methods=('GET', 'POST'))
def upload():
    return render_template('upload.html')
    

