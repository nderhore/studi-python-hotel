from sqlalchemy.orm import Session

from src.core.security.User import User


async def find_user_by_username(username: str, db: Session):
    return db.query(User).filter(User.username == username).first()
