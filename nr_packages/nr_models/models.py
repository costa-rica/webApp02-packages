from sqlalchemy import create_engine, inspect
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from datetime import datetime
from nr_config import ConfigDev, ConfigProd
from flask_login import UserMixin, LoginManager


config = ConfigDev()

Base = declarative_base()
engine = create_engine(config.SQL_URI, echo = True, connect_args={"check_same_thread": False})
Session = sessionmaker(bind = engine)
sess = Session()

login_manager= LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(any_name_for_id_obj):# any_name_for_id_obj can be any name because its an arg that is the user id.
    # This is probably created somewhere inside flask_login when the user gets logged in. But i've not been able to track it.
    print('* in load_user *')
    print(any_name_for_id_obj)
    return sess.query(Users).filter_by(id = any_name_for_id_obj).first()
    

class Users(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    email = Column(Text, unique = True, nullable = False)
    password = Column(Text, nullable = False)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f'Users(id: {self.id}, email: {self.email})'
