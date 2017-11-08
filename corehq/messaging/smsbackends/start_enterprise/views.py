from __future__ import absolute_import
from corehq.apps.sms.views import IncomingBackendView
from corehq.messaging.smsbackends.start_enterprise.models import (
    StartEnterpriseBackend,
    StartEnterpriseDeliveryReceipt,
)
from datetime import datetime
from django.http import HttpResponse, HttpResponseBadRequest


class StartEnterpriseDeliveryReceiptView(IncomingBackendView):
    urlname = 'start_enterprise_dlr'

    @property
    def backend_class(self):
        return StartEnterpriseBackend

    def get(self, request, api_key, *args, **kwargs):
        message_id = request.GET.get('msgId')

        if not message_id:
            return HttpResponseBadRequest("Missing 'msgId'")

        message_id = message_id.strip()

        try:
            dlr = StartEnterpriseDeliveryReceipt.objects.get(message_id=message_id)
        except StartEnterpriseDeliveryReceipt.DoesNotExist:
            dlr = None

        if dlr:
            dlr.received_on = datetime.utcnow()
            dlr.info = request.GET.dict()
            dlr.save()

        # Based on the documentation, a response of "1" acknowledges receipt of the DLR
        return HttpResponse("1")
