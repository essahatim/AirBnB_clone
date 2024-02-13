#!/usr/bin/python3
"""
Modules:
- `base_model`: Defines the base class for all data models.
- `engine`: Contains modules related to storage and data persistence.
"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
