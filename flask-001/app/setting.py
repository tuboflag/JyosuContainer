from flask import Flask
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

# postgresqlのDBの設定
#DATABASE = "postgresql://root:linux202009@192.168.4.109:5432/flask_tutorial"
#DATABASE = "postgresql://postgres:@127.0.0.1:5432/flask_tutorial"
#DATABASE = "postgresql://postgres:@postgres:5432/flask_tutorial"
#DATABASE = f"postgresql+psycopg2://root:linux202009@flask_postgresql:5432/flask_tutorial"
DATABASE = "postgresql+psycopg2://root:linux202009@flask_postgresql/flask_tutorial"

ENGINE = create_engine(
    DATABASE,
    encoding="utf-8",
    # TrueにするとSQLが実行される度に出力される
    echo=True
)

# Sessionの作成
session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するなど。
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

# modelで使用する
Base = declarative_base()
Base.query = session.query_property()