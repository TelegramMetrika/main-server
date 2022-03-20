from mod.db import create_session
from mod.model import Metrika

from datetime import datetime
from secrets import token_urlsafe
import random

class DB():
    def _create_metrika(data):
        token = token_urlsafe(32)
        session = create_session()
        m = Metrika(
            id=data.id,
            name=data.name,
            token=token,
            users='{}'
        )
        session.add(m)
        session.commit()

        return True

    def _get_metrika(id):
        session = create_session()
        m = session.query(Metrika).\
    				filter(Metrika.id == id).\
    				one()

        return Metrika(
            id=m.id,
            name=m.name,
            token=m.token,
            users=m.users
        )

    def _check_token(id, token):
        session = create_session()
        m = session.query(Metrika).\
    				filter(Metrika.id == id).\
    				one()

        return m.token == token

    def _add_data(id, data):
        session = create_session()
        m = session.query(Metrika).\
    				filter(Metrika.id == id).\
    				one()

        res = ''

        return True