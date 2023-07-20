from django.db import models
from django.utils.timezone import now


class BookModel(models.Model):
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)
    allow_delete = models.BooleanField(default=True)


    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        super(BookModel, self).delete(*args, **kwargs)

    def _delete(self):
        self.is_deleted = True
        self.deleted_at = now()
        self.save()

    def save(self, *args, **kwargs):
        self.updated_at = now()
        super(BookModel, self).save(*args, **kwargs)
