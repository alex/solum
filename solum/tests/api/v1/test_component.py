# Copyright 2013 - Red Hat, Inc.
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

import mock

from solum.api.controllers.v1 import component
from solum.tests import base
from solum.tests import fakes


@mock.patch('pecan.request', new_callable=fakes.FakePecanRequest)
@mock.patch('pecan.response', new_callable=fakes.FakePecanResponse)
class TestComponentController(base.BaseTestCase):
    def test_component_get(self, resp_mock, request_mock):
        obj = component.ComponentController('test_id')
        obj.get()
        self.assertEqual(200, resp_mock.status)

    def test_component_put(self, resp_mock, request_mock):
        obj = component.ComponentController('test_id')
        obj.put(None)
        self.assertEqual(501, resp_mock.status)

    def test_component_delete(self, resp_mock, request_mock):
        obj = component.ComponentController('test_id')
        obj.delete()
        self.assertEqual(501, resp_mock.status)


@mock.patch('pecan.request', new_callable=fakes.FakePecanRequest)
@mock.patch('pecan.response', new_callable=fakes.FakePecanResponse)
class TestComponentsController(base.BaseTestCase):
    def test_components_get_all(self, resp_mock, request_mock):
        component_obj = component.ComponentsController()
        resp = component_obj.get_all()
        self.assertIsNotNone(resp)
        self.assertEqual(200, resp_mock.status)

    def test_components_post(self, resp_mock, request_mock):
        obj = component.ComponentsController()
        obj.post(None)
        self.assertEqual(501, resp_mock.status)
