from .engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
classes_list = ["BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"]
