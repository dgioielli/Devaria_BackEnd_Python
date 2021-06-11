from sqlalchemy import Column, Integer, String, inspect

import config
from database.databese import Base, engine


class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100))
    senha = Column(String(100))


if not inspect(engine).has_table('usuario', schema=config.MYSQL_DATABASE):
    Usuario.__table__.create(engine)