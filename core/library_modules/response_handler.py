from rest_framework.response import Response as JsonResponse

from common.messages import ResponseMsg


class Response(JsonResponse):
    detail_msg = ResponseMsg.DETAIL_MSG
    code_msg = ResponseMsg.SUCCESS_DEFAULT_CODE

    def __init__(self, data=None, detail=detail_msg, code=code_msg, **kwargs):
        super(Response, self).__init__({"data": data, "detail": detail, "code": code}, **kwargs)


class ExceptionResponse(JsonResponse):
    detail_msg = ResponseMsg.DETAIL_MSG
    code_msg = ResponseMsg.DEFAULT_CODE

    def __init__(self, data=None, detail=detail_msg, code=code_msg, **kwargs):
        response = {
            "data": data,
            "detail": detail,
            "code": code
        }
        super(ExceptionResponse, self).__init__(response, **kwargs)
