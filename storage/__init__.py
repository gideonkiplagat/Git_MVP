from .storage_engine import StorageEngine
"""Create an instance of storage object and load the existing data"""

storage_json = StorageEngine()
storage_json.reload()
