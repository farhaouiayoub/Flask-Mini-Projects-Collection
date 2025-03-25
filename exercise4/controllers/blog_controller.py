from flask import Blueprint, render_template, request, redirect, url_for
from models.post_model import Post
from models.database import db

blog_blueprint = Blueprint('blog', __name__)

@blog_blueprint.route('/')
def index():
    posts = Post.query.order_by(Post.date.desc()).all()
    return render_template('index.html', posts=posts)

@blog_blueprint.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        
        return redirect(url_for('blog.index'))
    
    return render_template('add_post.html')

@blog_blueprint.route('/post/<int:id>')
def view_post(id):
    post = Post.query.get_or_404(id)
    return render_template('view_post.html', post=post)
