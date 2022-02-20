from email.policy import default
import string
from extensions import db
from datetime import datetime
from random import *


class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long = db.Column(db.String(512))
    short = db.Column(db.String(4))
    views = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, long) -> None:
        super().__init__()
        self.long = long
        self.short = self.GenerateShortUrl()

    def GenerateShortUrl(self) -> str:
        shortUrl = string.digits + string.ascii_letters
        result = "".join(choices(shortUrl, k=4))

        link = self.query.filter_by(short=result).first()

        if link:
            return self.GenerateShortUrl()

        return result
