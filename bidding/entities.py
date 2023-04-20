from dataclasses import dataclass, field
from datetime import datetime

from living_doc.annotations import Glossary

from bidding.value_objects import Money, Seller, Bid


@Glossary
@dataclass
class Listing:
    """An item that you can dispose in front of a buyer in order to sell in through an auction"""

    seller: Seller
    initial_price: Money
    ends_at: datetime
    bids: list[Bid] = field(default_factory=list)
    current_price: Money = field(init=False)
