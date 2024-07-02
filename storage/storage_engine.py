import json
from models.User import User
from models.model import Repo

class StorageEngine:
    """To serialize and deserialize instances created"""
    __file_repo = "repo.json"
    __file_user  = "user.json"
    __file_userURL = "URLs.json"
    __users = {}
    __repos = {}
    __userUrl = {}
    
    @classmethod
    def all(cls, obj_type=None):
        """Returns a dictionary containing all objects"""
        if obj_type is None:
            return {"users": cls.__users, "repos": cls.__repos}
        if obj_type == User:
            return cls.__users
        if obj_type == Repo:
            return cls.__repos
    
    @classmethod
    def new_user(cls, user):
        """Adds a new User instance to the __users dictionary."""
        cls.__users[user.id] = user
        
    @classmethod
    def new_repo(cls, repo, user_id):
        """Adds a new Repo instance to the __repos dictionary under the specified user_id."""
        if user_id not in cls.__repos:
            cls.__repos[user_id] = []
        cls.__repos[user_id].append(repo)
        
    @classmethod
    def new_url(cls, user_id, url):
        """Adds a new URL mapping to the __userUrl dictionary."""
        cls.__userUrl[url] = user_id
        
    @classmethod
    def save_user(cls):
        """Serializes the __users dictionary to a JSON file"""
        with open(cls.__file_user, "w") as json_file:
            json.dump({id: user.to_dict() for id, user in cls.__users.items()}, json_file)
            
    @classmethod
    def save_repos(cls):
        """Serializes the __repos dictionary to a JSON file"""
        with open(cls.__file_repo, "w") as json_file:
            json.dump({id: [repo.to_dict() for repo in repos] for id, repos in cls.__repos.items()}, json_file)
            
    @classmethod
    def save_userURLs(cls):
        """Serializes the __userUrl dictionary to a JSON file"""
        with open(cls.__file_userURL, "w") as json_file:
            json.dump(cls.__userUrl, json_file)
            
    @classmethod
    def reload(cls):
        """Deserializes the JSON files back into the __users, __repos, and __userUrl dictionaries."""
        try:
            with open(cls.__file_user, "r") as user_file:
                users_data = json.load(user_file)
            cls.__users = {int(id): User(**user_data) for id, user_data in users_data.items()}
        except FileNotFoundError:
            pass
        
        try:
            with open(cls.__file_repo, "r") as repo_file:
                repos_data = json.load(repo_file)
            cls.__repos = {int(id): [Repo(**repo_data) for repo_data in repo_list] for id, repo_list in repos_data.items()}
        except FileNotFoundError:
            pass
        
        try:
            with open(cls.__file_userURL, "r") as url_file:
                cls.__userUrl = json.load(url_file)
        except FileNotFoundError:
            pass
        
    @classmethod
    def delete_repo(cls, repo, user_id):
        """Removes a Repo instance from the __repos dictionary for the specified user."""
        if user_id in cls.__repos:
            cls.__repos[user_id].remove(repo)
        
    @classmethod
    def delete_user(cls, user):
        """Removes a User instance and its associated Repo instances from the __users and __repos dictionaries."""
        cls.__users.pop(user.id, None)
        cls.__repos.pop(user.id, None)
            
    @classmethod
    def get_stored_user_repos(cls, user_id):
        """Retrieves a list of Repo instances from the __repos dictionary by user ID"""
        return cls.__repos.get(user_id, [])

    @classmethod
    def get_user_id_from_url(cls, url):
        """Retrieves the user ID associated with a given URL from the __userUrl dictionary."""
        return cls.__userUrl.get(url)
