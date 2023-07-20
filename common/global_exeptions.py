from rest_framework import status
from rest_framework.exceptions import APIException

from common.messages import GlobalCommon


class NoResultException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = GlobalCommon.NO_RESULT
    default_code = 'NO_RESULT'


class DeleteNotAllowedException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = GlobalCommon.DELETE_NOT_ALLOWED
    default_code = 'invalid'
