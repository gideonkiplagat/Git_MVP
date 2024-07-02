class User:
    def __init__(self, *args, **kwargs):
        """initialize user object"""
        self.access_token = ""
        self.id = 0
        self.login = ""
        self.name = ""
        self.gravatar_id = ""
        self.avatar_url = ""
        self.email = ""
        self.html_url = ""
        self.bio = ""
        self.twitter_username = ""
        self.public_repos = ""
        self.followers = ""
        self.following = ""
        self.user_etag = ""
        self.repo_etag = ""
        if kwargs:
            for attr, val in kwargs.items():
                if hasattr(self, attr):
                    setattr(self, attr, val)
                    
    def update(self, *args, **kwargs):
        """ update user attributes """
        for attr, val in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, val)
    
    def save(self):
        """ save user attributes in the storage """
        print("HIT")
        from storage.storage_engine import StorageEngine
        StorageEngine.new_user(self)
        StorageEngine.save_user()

    def save_repos(self, repos=[]):
        """ save repo objects related to a user """
        from storage.storage_engine import StorageEngine
        for repo in repos:
            StorageEngine.new_repo(repo, self.id)
        StorageEngine.save_repos()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        return new_dict
