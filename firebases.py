import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

db_url = 'x'
# 서비스 계정의 비공개 키 파일이름
cred = credentials.Certificate("x")
default_app = firebase_admin.initialize_app(cred, {'databaseURL':db_url})
Data = db.reference()