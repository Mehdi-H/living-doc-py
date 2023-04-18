from datetime import datetime
from functools import total_ordering
import uuid

from dataclasses import field, dataclass

from living_doc.annotations import Glossary

UUID = uuid.UUID
UUID.v4 = uuid.uuid4


@Glossary
@dataclass
class Bidder:
    """A party who make a Bid (see Bid)"""

    id: UUID


@Glossary
@dataclass
class Seller:
    """A party who presents an object to an auction in order to sell it"""

    id: UUID


@dataclass
@Glossary
class Bid:
    """Offer of an amount higher than the opening bid or previous offers, during an auction"""

    price: "Money"
    bidder: Bidder
    placed_at: datetime = field(default_factory=datetime.utcnow)


@total_ordering
@dataclass
class Money:
    amount: int = 0
    currency: str = "USD"

    def __eq__(self, other):
        assert self.currency == other.currency
        return self.amount == other.amount

    def __lt__(self, other):
        assert self.currency == other.currency
        return self.amount < other.amount

    def __repr__(self) -> str:
        return f"{self.amount}{self.currency}"
