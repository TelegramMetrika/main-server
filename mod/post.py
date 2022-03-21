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
            data='{"id": "' + data.bot_id + '", "name": "' + data.name + '", "username": "' + data.username + '"}',
            token=token,
            users='{}'
        )
        session.add(m)
        session.commit()

        return True

    def _get_metrika(id):
        try:
            session = create_session()
            m = session.query(Metrika).\
                        filter(Metrika.id == id).\
                        one()

            return Metrika(
                id=m.id,
                data=m.data,
                token=m.token,
                users=m.users
            )
        except:
            return None

    def _check_token(id, token):
        try:
            session = create_session()
            m = session.query(Metrika).\
                        filter(Metrika.id == id).\
                        one()

            return m.token == token
        except:
            return False

    def _add_data(id, data):
        try:
            session = create_session()
            m = session.query(Metrika).\
                        filter(Metrika.id == id).\
                        one()

            # ...

            return True
        except:
            return False