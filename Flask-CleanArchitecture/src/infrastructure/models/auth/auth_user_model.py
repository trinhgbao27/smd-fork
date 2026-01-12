from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from infrastructure.databases.supabase import get_supabase_client
class AuthUserModel(get_supabase_client):
    __tablename__ = 'auth_users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(512), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime) 

    def __repr__(self):
        return f"<AuthUserModel(username='{self.username}', email='{self.email}')>"