# Copyright (c) 2014 The Johns Hopkins University/Applied Physics Laboratory
# All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from kmip.core.factories.payloads import PayloadFactory

from kmip.core.messages.payloads import create
from kmip.core.messages.payloads import destroy
from kmip.core.messages.payloads import get
from kmip.core.messages.payloads import locate
from kmip.core.messages.payloads import register


class RequestPayloadFactory(PayloadFactory):

    def _create_create_payload(self):
        return create.CreateRequestPayload()

    def _create_register_payload(self):
        return register.RegisterRequestPayload()

    def _create_locate_payload(self):
        return locate.LocateRequestPayload()

    def _create_get_payload(self):
        return get.GetRequestPayload()

    def _create_destroy_payload(self):
        return destroy.DestroyRequestPayload()