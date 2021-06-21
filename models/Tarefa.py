from sqlalchemy import Column, Integer, String, inspect, Date, ForeignKey
from sqlalchemy_serializer import SerializerMixin

import config
import database
from database.databese import Base, engine


class Tarefa(Base, SerializerMixin):
    __tablename__ = "tarefa"
    metadata = database.databese.metadata

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100))
    dataPrevisaoConclusao = Column(Date)
    dataConclusao = Column(Date)
    idUsuario = Column(Integer, ForeignKey("usuario.id"))


if not inspect(engine).has_table('tarefa', schema=config.MYSQL_DATABASE):
    Tarefa.__table__.create(engine)
