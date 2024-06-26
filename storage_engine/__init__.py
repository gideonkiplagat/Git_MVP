from . import storage
"""create an instance of storage object and load the existing data"""

storage_json = storage.Filestorage()
storage_json.reload()