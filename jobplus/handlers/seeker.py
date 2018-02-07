from flask import Blueprint, render_template, flash
from jobplus.forms import SeekerForm

seeker = Blueprint('seeker', __name__, url_prefix='/seekers')

@seeker.route('/profile', methods=['GET', 'POST'])
def profile():
    form = SeekerForm()
    if form.validate_on_submit():
        form.create_seeker()
        flash('已保存', 'success')
    return render_template('seeker_main.html', form=form)

@seeker.route('/resume')
def resume():
    return render_template('job/resume.html')

@seeker.route('/deliver')
def deliver():
    return render_template('job/deliver.html')

