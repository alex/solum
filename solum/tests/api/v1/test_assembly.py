# -*- coding: utf-8 -*-
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

from solum.api.controllers.v1 import assembly
from solum.tests import base
from solum.tests import fakes


@mock.patch('pecan.request', new_callable=fakes.FakePecanRequest)
@mock.patch('pecan.response', new_callable=fakes.FakePecanResponse)
class TestAssemblyController(base.BaseTestCase):
    def test_assembly_get(self, resp_mock, request_mock):
        assembly_obj = assembly.AssemblyController('test_id')
        assembly_obj.get()
        self.assertEqual(200, resp_mock.status)

    def test_assembly_put(self, resp_mock, request_mock):
        obj = assembly.AssemblyController('test_id')
        obj.put(None)
        self.assertEqual(501, resp_mock.status)

    def test_assembly_delete(self, resp_mock, request_mock):
        obj = assembly.AssemblyController('test_id')
        obj.delete()
        self.assertEqual(501, resp_mock.status)


@mock.patch('pecan.request', new_callable=fakes.FakePecanRequest)
@mock.patch('pecan.response', new_callable=fakes.FakePecanResponse)
class TestAssembliesController(base.BaseTestCase):
    def test_assemblies_get_all(self, resp_mock, request_mock):
        assembly_obj = assembly.AssembliesController()
        resp = assembly_obj.get_all()
        self.assertIsNotNone(resp)
        self.assertEqual(200, resp_mock.status)

    def test_assemblies_post(self, resp_mock, request_mock):
        obj = assembly.AssembliesController()
        obj.post(None)
        self.assertEqual(501, resp_mock.status)
