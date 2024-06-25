# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "postgresql://user:password@localhost/healthcare_db"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Substitua pelos seus valores reais
DATABASE_URL = "postgresql://patrikz:root123@localhost/ufsc_sql_injection"

# Criação do engine
engine = create_engine(DATABASE_URL)

# Sessão local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base declarativa
Base = declarative_base()

# Dependência da sessão do banco de dados para FastAPI ou uso similar
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelo de exemplo
from sqlalchemy import Column, Integer, String

class ExampleModel(Base):
    __tablename__ = 'example_model'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

# Criar todas as tabelas
Base.metadata.create_all(bind=engine)
