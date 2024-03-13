from pydantic import BaseModel
from datetime import datetime
from typing import List, ClassVar
import pickle
import os


class Entry(BaseModel):

    STORAGE_PATH: ClassVar = 'var'

    title: str
    content: str
    timestamp: datetime

    def __str__(self):
        return f'{self.timestamp:%d.%m.%Y %H:%m}\t{self.title}\n\n{self.content}'

    def save(self):

        file_name = f'{self.timestamp:%Y-%m-%d}_{self.title.replace(" ", "_")}.entry'

        with open(os.path.join(self.STORAGE_PATH, file_name), 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def get_entry_list(cls):
        return [x for x in os.listdir(cls.STORAGE_PATH) if x.endswith('.entry')]

    @classmethod
    def get_entry(cls, entry_name):
        with open(os.path.join(cls.STORAGE_PATH, entry_name), 'rb') as f:
            entry = pickle.load(f)
        return entry
