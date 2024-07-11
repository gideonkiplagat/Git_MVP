from flask import Flask, request, render_template, redirect
from storage.storage_engine import StorageEngine
from models.User import User
from models.model import Repo

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')

# Initialize storage engine
storage = StorageEngine()
storage.reload()

@app.route('/')
def home():
    users = storage.all(User)
    repos = storage.all(Repo)
    return render_template('landing.html', users=users, repos=repos)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.form
    new_user = User(id=int(data['id']), name=data['name'], email=data['email'])
    new_user.save()
    return redirect('/')

@app.route('/add_repo', methods=['POST'])
def add_repo():
    data = request.form
    new_repo = Repo(id=int(data['id']), name=data['name'], user_id=int(data['user_id']))
    new_repo.save()
    return redirect('/')

@app.route('/tutorials')
def tutorials_page():
    tutorials = [
        {"id": 1, "title": "Git Basics", "content": "Learn the basics of Git..."},
        {"id": 2, "title": "Branching Strategies", "content": "Understand different branching strategies..."},
        {"id": 3, "title": "Merging and Rebasing", "content": "Learn how to merge and rebase..."},
    ]
    return render_template('./templates/tutorials.html', tutorials=tutorials)

@app.route('/tutorial/<int:id>')
def tutorial(id):
    tutorials = [
        {"id": 1, "title": "Git Basics", "content": "Learn the basics of Git..."},
        {"id": 2, "title": "Branching Strategies", "content": "Understand different branching strategies..."},
        {"id": 3, "title": "Merging and Rebasing", "content": "Learn how to merge and rebase..."},
    ]
    tutorial = next((t for t in tutorials if t['id'] == id), None)
    if tutorial:
        return render_template('./templates/tutorials.html', tutorial=tutorial)
    else:
        return "Tutorial not found", 404

@app.route('/visualizations')
def visualizations():
    return render_template('./templates/visualizations.html')

@app.route('/collaboration')
def collaboration():
    users = storage.all(User)
    repos = storage.all(Repo)
    return render_template('./templates/collaboration.html', users=users, repos=repos)

if __name__ == '__main__':
    app.run(debug=True)
