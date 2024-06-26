"""Repo details"""

import storage_engine
class model():
    """model object"""
    def __init__(self, *args, **kwargs):
        """Initialize the model"""
        self.id = 0
        self.name = ""
        self.owner_id = 0
        self.repo_owner_name = ""
        self.repo_owner_url = ""
        self.forks_count = 0
        self.stargazers_count = 0
        self.subscribers_count = 0
        self.license = {}
        self.description = ""
        self.latest_release = ""
        self.topics = []
        self.size = 0
        self.langs = {}
        self.html_url = ""
        self.user_id = 0
        if kwargs:
            for attr, val in kwargs.items():
                if hasattr(self, attr):
                    setattr(self, attr, val)
    
    def update(self, *args, **kwargs):
        """update the attributes"""
        for attr, val in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, val)
    
    def save(self):
        """ 
        save repo attributes in the storage
        """
        storage_engine.Storage_Json.new_repo(self, self.user_id)
        storage_engine.Storage_Json.save_repos()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        # new_dict["__class__"] = self.__class__.__name__
        return new_dict
    

    