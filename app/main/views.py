from flask import render_template,request,redirect,url_for,abort
from ..models import User,Pitches,Comments
from .. import db,photos
import markdown2  
from .forms import UpdateProfile,CommentForm,PitchForm
# from app import auth
from . import main
from flask_login import login_required,current_user
#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
 
    title='Pitch site'
    return render_template('index.html',title=title)
    
@main.route('/pitch/newpitch', methods=['POST', 'GET'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        newPitch = form.pitch_info.data
        new_pitch = Pitches(pitch_title=title,pitch_category=category,pitch_itself=newPitch,user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('.index'))
    title = 'Add pitch'
    return render_template('pitches.html', title=title, pitchesform=form)

@main.route('/categories/<category>')
def categories(category):
    '''
    view function to display interview pitches
    '''
    pitches=Pitches.get_pitches (category)
    title = category + "pitches"
 
    return render_template('categories.html',title=title,pitches=pitches)

# @main.route('/comment/<int:id>', methods=['POST', 'GET'])
# @login_required
# def post_comment(id):
#     pitche = Pitches.getPitchId(id)
#     comments = Comments.get_comments(id)
#     if request.args.get("like"):
#         pitch = Pitches.query.filter_by(user_id=current_user.id)
#         pitch.likes += 1
#         print(pitch.likes)
#         db.session.add(pitch.likes)
#         db.session.commit()
#         return str(pitch.likes)
#     elif request.args.get("dislike"):
#         pitche.dislikes += 1
#         db.session.add()
#         db.session.commit()
#         return redirect(".comment")
#     form = CommentForm()
#     if form.validate_on_submit():
#         comment = form.comment.data
#         new_comment = Comments(comment_itself=comment,
#                                user_id=current_user.id,
#                                pitches_id=pitche.id)
#         new_comment.save_comment()
#         return redirect(url_for('main.post_comment', id=pitche.id))
#     return render_template('comment.html',
#                            commentform=form,
#                            comments=comments,
#                            pitch=pitche)
# @main.route('/pitch/upvote/<int:id>&<int:vote>')
# @login_required
# def vote(id, vote):
#     counter = 0
#     pitchethrill = Pitches.getPitchId(id)
#     # vote = .get_vote(id)
#     counter += 1
#     print(counter)
#     new_vote = Pitches(likes=counter)
#     new_vote.save_vote()
#     return str(new_vote)
@main.route('/comments/<id>')
@login_required
def comment(id):
    '''
    function to return the comments
    '''
    comm =Comments.get_comment(id)
    print(comm)
    title = 'comments'
    return render_template('comments.html',comment = comm,title = title)

@main.route('/new_comment/<int:pitches_id>', methods = ['GET', 'POST'])
@login_required
def new_comment(pitches_id):
    pitches = Pitches.query.filter_by(id = pitches_id).first()
    form = CommentForm()

    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comments(comment=comment,user_id=current_user.id, pitches_id=pitches_id)

        new_comment.save_comment()

        return redirect(url_for('main.index'))
    title='New Pitch'
    return render_template('new_comment.html',title=title,comment_form = form,pitches_id=pitches_id)
@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    return render_template("profile/profile.html", user = user)
@main.route('/user/<uname>/update',methods = ['GET','POST'])
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile',uname = user.username))
    return render_template('profile/update.html',form = form)
@main.route('/user/<uname>/update/pic',methods = ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname = uname))