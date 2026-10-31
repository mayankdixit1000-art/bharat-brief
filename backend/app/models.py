
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    description = Column(Text, nullable=True)
    content = Column(Text, nullable=True)
    url = Column(String(1000), unique=True, nullable=False)
    published_date = Column(DateTime(timezone=True), nullable=True)
    source = Column(String(200), default="Press Information Bureau")
    category = Column(String(100), default="Uncategorized")
