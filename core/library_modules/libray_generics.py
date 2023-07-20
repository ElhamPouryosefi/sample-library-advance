from django.utils.timezone import now
from rest_framework import generics
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from common.global_exeptions import NoResultException, DeleteNotAllowedException
from core.library_modules.pagination_handler import DefaultPagination


class BookGenericAPIView(GenericAPIView):
    def get_serializer_context(self):
        context = super(BookGenericAPIView, self).get_serializer_context()
        context.update(
            {'user': self.request.user})
        return context

    def get_queryset(self):
        if not self.request.user:
            raise NoResultException()
        if self.request.user.is_superuser:
            return super().get_queryset()


class BookCreateView(BookGenericAPIView, generics.CreateAPIView):

    def create(self, request, **kwargs):
        instance = kwargs.pop('instance', False)
        if instance:
            serializer = self.get_serializer(instance, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class BookListView(BookGenericAPIView, generics.ListAPIView):

    pagination_class = DefaultPagination

    def paginate_queryset(self, queryset):
        if self.paginator is None or not self.request.query_params.get('page', None):
            return None
        return self.paginator.paginate_queryset(queryset, self.request, view=self)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BookUpdateView(BookGenericAPIView, generics.UpdateAPIView):
    def update(self, request, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookRetrieveView(BookGenericAPIView, generics.RetrieveUpdateAPIView):
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class BookDestroyView(BookGenericAPIView, generics.RetrieveUpdateAPIView):

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        if instance.allow_delete:
            instance.is_deleted = True
            instance.deleted_at = now()
            instance.save()
        raise DeleteNotAllowedException()


class BookModifyView(BookRetrieveView, BookUpdateView, BookDestroyView):
    def get_serializer_context(self):
        context = super(BookModifyView, self).get_serializer_context()
        context.update(
            {'user': self.request.user, 'pk': self.kwargs.get('pk', None)})
        return context


class BookUpdateRetrieveView(BookUpdateView, BookRetrieveView):
    pass


class BookListCreateView(BookListView, BookCreateView):
    pass
