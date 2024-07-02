from storage.storage_engine import StorageEngine
from models.User import User
from models.model import Repo

# Create an instance of StorageEngine and load existing data
storage_engine = StorageEngine()
storage_engine.reload()

# Example: Create a new user and save
new_user = User(id=1, name="John Doe", email="john.doe@example.com")
new_user.save()

# Example: Create a new repo and save
new_repo = Repo(id=1, name="Sample Repo", user_id=1)
new_repo.save()

# Display all users and repos
print(storage_engine.all(User))
print(storage_engine.all(Repo))
