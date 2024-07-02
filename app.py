from flask import Flask, request, render_template, redirect
from storage.storage_engine import StorageEngine
from models.User import User
from models.model import Repo

app = Flask(__name__)

# Initialize storage engine
storage = StorageEngine()
storage.reload()

@app.route('/')
def home():
    users = storage.all(User)
    repos = storage.all(Repo)
    return render_template('index.html', users=users, repos=repos)

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

if __name__ == '__main__':
    app.run(debug=True)