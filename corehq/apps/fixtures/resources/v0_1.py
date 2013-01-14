from tastypie import fields as tp_f
from corehq.apps.api.resources import JsonResource
from corehq.apps.api.resources.v0_1 import CustomResourceMeta
from corehq.apps.api.util import get_object_or_not_exist
from corehq.apps.fixtures.models import FixtureDataItem

class FixtureResource(JsonResource):
    type = "fixture"
    fields = tp_f.DictField(attribute='fields', readonly=True, unique=True)
    fixture_type_id = tp_f.CharField(attribute='data_type_id', readonly=True)

    def obj_get(self, request, **kwargs):
        domain = kwargs['domain']
        location_id = kwargs['pk']
        return get_object_or_not_exist(FixtureDataItem, location_id, domain)

    def obj_get_list(self, request, **kwargs):
        domain = kwargs['domain']
        parent_id = request.GET.get("parent_id", None)
        parent_ref_name = request.GET.get("parent_ref_name", None)
        child_type = request.GET.get("child_type", None)

        if parent_id and parent_ref_name and child_type:
            print "here"
            l = list(FixtureDataItem.by_field_value(domain, child_type, parent_ref_name, parent_id))
            return l
        return []

    class Meta(CustomResourceMeta):
        resource_name = 'fixture'
        limit = 0