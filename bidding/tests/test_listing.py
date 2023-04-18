from datetime import datetime
import pytest
from bidding.entities import Listing
from bidding.value_objects import Money, Seller, UUID

@pytest.mark.unit
def test_listing_initial_price():
    seller = Seller(id=UUID.v4())
    listing = Listing(
        seller=seller,
        initial_price=Money(10),
        ends_at=datetime.utcnow(),
    )
    assert listing.initial_price == Money(10)