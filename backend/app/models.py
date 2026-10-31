
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    UniqueConstraint,
    func
)
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


class TranslationCache(Base):
    __tablename__ = "translation_cache"

    id = Column(Integer, primary_key=True, index=True)

    news_id = Column(
        Integer,
        ForeignKey("news.id", ondelete="CASCADE"),
        nullable=False
    )

    target_language = Column(String(10), nullable=False)

    title = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    content = Column(Text, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    __table_args__ = (
        UniqueConstraint(
            "news_id",
            "target_language",
            name="unique_news_language"
        ),
    )
