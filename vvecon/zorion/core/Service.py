from typing import List, Type

from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from vvecon.zorion.db.models import Model

__all__ = ['Service']


class Service(serializers.ModelSerializer):
    model: Type[Model]

    def getAll(self) -> List[Model]:
        return self.model.objects.all()

    def getById(self, obj_id):
        try:
            return self.model.objects.get(pk=obj_id)
        except ObjectDoesNotExist:
            return None

    def delete(self, obj_id):
        obj = self.getById(obj_id)
        if obj is not None:
            obj.delete()
            return True
        return False

    def hard_delete(self, obj_id):
        obj = self.getById(obj_id)
        if obj is not None:
            obj.hard_delete()
            return True
        return False
