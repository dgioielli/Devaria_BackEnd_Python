from sqlalchemy import Column, Integer, String, inspect
from sqlalchemy.orm import relationship

import config
import database.databese
from database.databese import Base, engine


class Usuario(Base):
    __tablename__ = 'usuario'
    metadata = database.databese.metadata

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    email = Column(String(100))
    senha = Column(String(100))
    #tarefas = relationship("Tarefa")


if not inspect(engine).has_table('usuario', schema=config.MYSQL_DATABASE):
    Usuario.__table__.create(engine)