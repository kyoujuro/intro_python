import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

engine = sqlalchemy.create_engine('sqlite:///:memory:')
Base = sqlalchemy.ext.declarative.declarative_base()
class Color(Base):
    __tablename__ = 'colors'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))
Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()
color = Color(name='Green')
session.commit()
colors = session.query(Color).all()
for color in colors:
    print(color.id, color.name)
