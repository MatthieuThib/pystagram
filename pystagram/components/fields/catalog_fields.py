from enum import unique

from pystagram.components.fields.fields import Fields


@unique
class CatalogFields(Fields):
    CATALOG_ID = "catalog_id"
    CATALOG_NAME = "catalog_name"
    SHOP_NAME = "shop_name"
    PRODUCT_COUNT = "product_count"
