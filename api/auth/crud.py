from api.utils.dbUtil import database
from api.auth import schemas


def save_user(user: schemas.UserCreate):
    query = "INSERT INTO my_users VALUES (nextval('user_id_seq'), :email, :password, :fullname, now() at time zone 'UTC', '0')"
    return database.execute(query, values={"email": user.email, "password": user.password, "fullname": user.fullname})


def update_user(email: str):
    query = "UPDATE my_users SET status='1' WHERE email=:email"
    return database.execute(query, values={"email": email})

def find_existed_user(email: str):
    query = "select * from my_users where email=:email"
    return database.fetch_one(query, values={"email": email})
