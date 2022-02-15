from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, Workout
from . import db
import json
import pandas as pd 
import plotly
import plotly.express as px



views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/week1', methods=['GET','POST'])
@login_required
def week1():
    return render_template("week.html", user=current_user)

@views.route('/week2', methods=['GET','POST'])
@login_required
def week2():
    return render_template("week.html", user=current_user)

@views.route('/week3', methods=['GET','POST'])
@login_required
def week3():
    return render_template("week.html", user=current_user)

@views.route('/week4', methods=['GET','POST'])
@login_required
def week4():
    return render_template("week.html", user=current_user)

@views.route('/week5', methods=['GET','POST'])
@login_required
def week5():
    return render_template("week.html", user=current_user)

@views.route('/data1', methods=['GET','POST'])
@login_required
def data1():
    if request.method == 'POST':
        for n in range(1, 7):
            check = request.form.get('weight'+str(n))
            if check:
                weight = request.form.get('weight'+ str(n))
                rpe = request.form.get('rpe'+str(n))
                set = n
                new_w = Workout(Weight=weight, RPE=rpe, set_num= set, user_id=current_user.id)
                db.session.add(new_w)    
                db.session.commit()


        checkdata = Workout.query.all()
        flash('Data added!', category='success')




    return render_template("data1.html", checkdata=checkdata, user=current_user)




@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

