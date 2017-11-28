import os
from flask import render_template, redirect, current_app, url_for, request, flash
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user
from . import main
from .forms import ImageForm, EditProfileForm ,EditProfileAdminForm
from ..models import User, Role, Image
from .. import db
from ..decorators import admin_required

@main.route('/')
def index():
    return render_template('index.html')



@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)



@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Профиль был обновлен.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)

@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        db.session.commit()
        flash('Профиль был обновлен.')
        return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile.html', form=form, user=user)

@main.route('/upload',methods=['GET','POST'])
@login_required
def upload():
    form = ImageForm()
    if form.validate_on_submit():
        uploaded_files = request.files.getlist("upload")
        path_to_folder = os.path.join(current_app.root_path, 'static/images', form.name.data)
        if not os.path.exists(path_to_folder):
            os.mkdir(path_to_folder)
            for f in uploaded_files:
                filename = secure_filename(f.filename)
                f.save(os.path.join(path_to_folder, filename))
                path = Image(name=form.name.data, path=os.path.join('images', form.name.data, filename))
                db.session.add(path)
                db.session.commit()
    return render_template('upload.html', form=form)

@main.route('/uploaded/', methods=['GET'])
def uploaded():
    page = request.args.get('page', 1, type=int)
    pagination = Image.query.filter_by(name='Лига справедливости').paginate(page, per_page=1, error_out=False)
    images = pagination.items
    return render_template('uploaded.html', images=images, pagination=pagination)


@main.route('/uploaded/<name>', methods=['GET'])
def comics(name):
    page = request.args.get('page', 1, type=int)
    pagination = Image.query.filter_by(name=name).paginate(page, per_page=1, error_out=False)
    images = pagination.items
    return render_template('uploaded.html', images=images, pagination=pagination, name=name)
