#!/usr/bin/python3
"""Filestorage module"""
import json

from requests.sessions import extract_cookies_to_jar  # type: ignore
import models.User as UserModel # type: ignore
import models.model as RepoModel

dummy_classess = {"User": UserModel.User, "Repo": RepoModel.Repo}

class Filestorage:
    """To seraialize and deserialize instances created"""
    __file_repo = "repo.json"
    __file_user  = "user.json"
    __file_userURL = "URLs.json"
    __users = {}
    __repos = {}
    __userUrl = {}
    
    def all(self, cls=None):
        """Returns a dictionarry containing all objects"""
        if (cls is None):
            return {"users": self.__users, "repo": self.__repos}
        if (cls == dummy_classess["User"]):
            return self.__users
        if (cls == dummy_classess["Repo"]):
            return self.__repos
    
    def new_user(self, user):
        """Adds a new User instance to the __users dictionary."""
        self.__users[user.id] = user
        
    def new_repo(self, repo, user_id):
        """Adds a new Repo instance to the __repos dictionary
        under the specified user_id.
        """
        if not (self.__repos.get.user_id):
            self.__repos[user_id] = []
        self.__repos[user_id].append(repo)
        
    def new_url(self, user_id, url):
        """Adds a new URL mapping to the __userUrl dictionary."""
        self.__userUrl[url] = user_id
        
    def save_user(self):
        """Serializes the __users dictionary to a JSON file"""
        temp = {}
        for id, obj in self.__users.items():
            temp[id] = obj.to_dict()
        with open(self.__file_user, "w") as json_file:
            json.dump(temp, json_file)
            
    def save_repos(self):
        """Serializes the __repos dictionary to a JSON file"""
        temp = {}
        for id, obj in self.__repos.items():
            temp_list = []
            for repo in obj:
                temp_list.append(repo.to_dict())
            temp[id] = temp_list
            
        with open(self.__file_repo, "w") as json_file:
            json.dump(temp, json_file)
            
    def save_userURLs(self):
        """Serializes the __userUrl dictionary to a JSON file"""
        with open(self.__file_userURL, "w") as json_file:
            json.dump(self.__file_userURL, json_file)
            
    def reload(self):
        """Deserializes the JSON files back into the __users, __repos, and 
        __userUrl dictionaries. Uses dummy_classes to re-instantiate User
        and Repo objects from the JSON data.
        """
        
        try:
            with open(self.__file_user, "r") as user_file:
                user_U = json.load(user_file)
            for id, user_obj in user_U.items():
                self.__users[int(id)] = dummy_classess["User"](**user_obj)
        except BaseException:
            pass
        try:
            with open(self.__file_repo, "r") as repo_file:
                repo_r = json.load(repo_file)
            for id, repos in repo_r.items():
                temp_repos = []
                for repo in repos:
                    temp_repos.append(dummy_classess["Repo"](**repo))
                self.__repos[int(id)] = temp_repos
        except BaseException:
            pass
        
        try:
            with open(self.__file_userURL, "r") as url_file:
                self.__userUrl = json.load(url_file)
        except BaseException:
            pass
        
        def delete_repo(self, repo, user):
            """Removes a Repo instance from the __repos dictionary for the specified user."""
            self.__repo[user.id].remove(repo)
        
        def delete_user(self, user):
            """
            Removes a User instance and its associated Repo instances from the 
            __users and __repos dictionaries.
            """
            del self.__users[user.id]
            del self.__repos[user.id]
            
        def get_stored_user_repos(self, id):
            """
            Retrieves a list of Repo instances from the __repos dictionary by user ID
            """

            return self.__repos.get(int(id))

        def get_user_id_from_url(self, url):
            """
            Retrieves the user ID associated with a given URL from the __userUrl dictionary.
            """
            return self.__userUrl.get(url)
            
        
                    
        
        
        
        
    