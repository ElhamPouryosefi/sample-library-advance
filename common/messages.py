from django.utils.translation import gettext_lazy as _


class GlobalCommon:
    NO_RESULT = _('no result')
    NOT_FOUND = _('Not found.')
    SERVER_SIDE_ERROR = _('An error occurred. Please try again later')
    ITEM_ALREADY_EXISTS = _('Item already exists ')
    DELETE_NOT_ALLOWED = _('delete not allowed ')


class ResponseMsg:
    DETAIL_MSG = _("mission accomplished")
    DEFAULT_CODE = "Error"
    SUCCESS_DEFAULT_CODE = "SUCCESS"


class PermissionMsg:
    INVALID_PERMISSION = _("Invalid Permission")
    PERMISSION_DENIED = _('Permission denied.')
    AUTHENTICATION_FAILED = _("Authentication failed")
    NO_ACCESS_TO_VIEW = _('No access')