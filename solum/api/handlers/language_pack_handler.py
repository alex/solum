# Copyright 2014 - Rackspace
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from solum.api.controllers.v1.datamodel import language_pack
from solum.api.handlers import handler


class LanguagePackHandler(handler.Handler):
    """Fulfills a request on the language pack resource."""

    def get(self, id):
        response = language_pack.LanguagePack.sample()
        return response

    def get_all(self):
        """Return all language packs, based on the query provided."""
        response = []
        return response
