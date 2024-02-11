from enum import unique

from pystagram.graph_api.components.fields.fields import Fields


@unique
class CatalogFields(Fields):
    CATALOG_ID = "catalog_id"
    CATALOG_NAME = "catalog_name"
    SHOP_NAME = "shop_name"
    PRODUCT_COUNT = "product_count"
