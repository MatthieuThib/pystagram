from enum import unique

from pystagram.components.fields.fields import Fields


@unique
class ContainerFields(Fields):
    COPYRIGHT_CHECK_STATUS = "copyright_check_status"
    ID = "id"
    STATUS = "status"
    STATUS_CODE = "status_code"
