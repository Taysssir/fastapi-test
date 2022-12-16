from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData, Sequence

metadata = MetaData()

users = Table(
    'my_users', metadata,
    Column('id', Integer, Sequence('user_id_seq'), primary_key=True),
    Column('email', String(100)),
    Column('password', String(100)),
    Column('fullname', String(50)),
    Column('created_on', DateTime),
    Column('status', String(1)),
)

otps = Table(
    'my_otps', metadata,
    Column('id', Integer, Sequence('otp_id_seq'), primary_key=True),
    Column('recipient_id', String(100)),
    Column('session_id', String(100)),
    Column('otp_code', String(4)),
    Column('status', String(1)),
    Column('created_on', DateTime),
)