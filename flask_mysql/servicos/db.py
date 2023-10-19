from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///funcionarios.db", echo=True)
Base = declarative_base()


class Setor(Base):
    __tablename__ = "setor"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    sobrenome = Column(String)
    data_admissao = Column(String)
    status = Column(String)
    funcionarios = relationship("Funcionario", back_populates="setor")


class Cargo(Base):
    __tablename__ = "cargo"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    setor_id = Column(Integer, ForeignKey("setor.id"))
    funcionarios = relationship("Funcionario", back_populates="cargo")


class Funcionario(Base):
    __tablename__ = "funcionario"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    setor_id = Column(Integer, ForeignKey("setor.id"))
    cargo_id = Column(Integer, ForeignKey("cargo.id"))
    setor = relationship("Setor", back_populates="funcionarios")
    cargo = relationship("Cargo", back_populates="funcionarios")


Base.metadata.create_all(engine)
