import requests
from django.core.cache import cache
from rest_framework.status import HTTP_200_OK


class Utilities:
    @staticmethod
    def send_request(method, token, url, data=None):
        headers = dict()
        if token:
            headers['Authorization'] = token
        headers['Content-Type'] = 'application/json'
        if method == 'GET':
            url = f"{url}?"
            for key in data:
                url += f"{key}={data[key]}&"
        try:
            response = requests.request(method, url=url, data=data, headers=headers)
        except requests.exceptions.ConnectionError:
            return None
        if response.status_code == HTTP_200_OK:
            return response.json()['data']
        return None


class AuthPermission:
    def __init__(self, user):
        self.user = user

    def has_perm(self, view_permission):
        permission = view_permission.split(".")[-1]
        user_permissions = self.get_permissions()
        if permission in user_permissions:
            return True
        return False

    def get_permissions(self):
        user_cache = cache.get(self.user.id)
        if user_cache:
            return user_cache
        return []


class QueryParamsFilterSet:

    def __init__(self, query_params):
        self.query_params = query_params

    def convert(self):
        request_data = dict()
        for item in self.query_params:
            if item not in ['page', 'limit'] and self.query_params.get(item) != '':
                request_data[item] = self.type_detection(self.query_params.get(item))
        return request_data

    @staticmethod
    def type_detection(key):
        if key in ['true', 'false']:
            value = bool(key)
        else:
            try:
                value = int(key)
            except (ValueError, TypeError):
                value = key
        return value
