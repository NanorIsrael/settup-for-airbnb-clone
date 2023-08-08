#!/usr/bin/python3
""" initializing module that initializes storage """


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
