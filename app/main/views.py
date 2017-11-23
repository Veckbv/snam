import os
from flask import render_template, redirect, current_app, url_for, request
from werkzeug.utils import secure_filename
from . import main
from .forms import ImageForm
from ..models import Image
from .. import db

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/upload',methods=['GET','POST'])
def upload():
    form = ImageForm()
    if form.validate_on_submit():
        uploaded_files = request.files.getlist("image")
        for f in uploaded_files:
            filename = secure_filename(f.filename)
            f.save(os.path.join(current_app.root_path, 'static/images', filename))
            path = Image(path=os.path.join('images', filename))
            db.session.add(path)
            db.session.commit()
    return render_template('upload.html', form=form)

@main.route('/uploaded', methods=['GET', 'POST'])
def uploaded():
    page = request.args.get('page', 1, type=int)
    pagination = Image.query.paginate(page, per_page=1, error_out=False)
    images = pagination.items
    return render_template('uploaded.html', images=images, pagination=pagination)