from typing import Optional

from pystagram.components.tags.tag import Tag


class ProductTag(Tag):
    """ Instagram Product Tag.

    :param product_id: Product id.
    :type product_id: str
    :param x: X coordinate. Range: [0, 1].
    :type x: float
    :param y: Y coordinate. Range: [0, 1].
    :type y: float
    :param merchant_id: Merchant id.
    :type merchant_id: Optional[str]
    """
    def __init__(self, product_id: str, x: float, y: float, merchant_id: Optional[str] = None):
        self.product_id = product_id
        self.merchant_id = merchant_id
        self.x = x
        self.y = y

    def dict(self) -> dict:
        """ Return a dictionary representation of the tag."""
        return {
            "product_id": self.product_id,
            "x": self.x,
            "y": self.y
        }

    def info(self) -> dict:
        """ Return an alternative dictionary representation of the tag."""
        return {
            "product_id": self.product_id,
            "merchant_id": self.merchant_id,
        }
