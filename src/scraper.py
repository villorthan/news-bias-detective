
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
@dataclass
class Article:
    """ Represents a single news article from one outlet """
    url:str
    source:str
    headline:str
    body:str
    author: Optional[str] = None
    published: Optional[str] = None
    fetch_time:datetime = field(default_factory=datetime.now)

    def word_count(self) -> int:
        return len(self.body.split())
    
    def summary(self) ->str:
        return self.body[:200] +  "..." if len(self.body)>200 else self.body
    def __repr__(self) -> str:
        return f"Article(source='{self.source}', headline={self.headline[:50]}...', words={self.word_count()})"
    