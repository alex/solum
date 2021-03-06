# Copyright 2013 - Rackspace US, Inc.
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

import pecan
from pecan import rest
import wsmeext.pecan as wsme_pecan

from solum.api.controllers.v1.datamodel import plan
from solum.api.handlers import plan_handler
from solum.common import exception


class PlanController(rest.RestController):
    """Manages operations on a single plan."""

    def __init__(self, plan_id):
        self._id = plan_id

    @exception.wrap_controller_exception
    @wsme_pecan.wsexpose(plan.Plan)
    def get(self):
        """Return this plan."""
        handler = plan_handler.PlanHandler()
        return handler.get(self._id)

    @exception.wrap_controller_exception
    @wsme_pecan.wsexpose(plan.Plan, body=plan.Plan)
    def put(self, data):
        """Modify this plan."""
        handler = plan_handler.PlanHandler()
        return handler.update(self._id, data)

    @exception.wrap_controller_exception
    @wsme_pecan.wsexpose(status_code=204)
    def delete(self):
        """Delete this plan."""
        handler = plan_handler.PlanHandler()
        return handler.delete(self._id)


class PlansController(rest.RestController):
    """Manages operations on the plans collection."""

    @pecan.expose()
    def _lookup(self, plan_id, *remainder):
        if remainder and not remainder[-1]:
            remainder = remainder[:-1]
        return PlanController(plan_id), remainder

    @exception.wrap_controller_exception
    @wsme_pecan.wsexpose(plan.Plan, body=plan.Plan, status_code=201)
    def post(self, data):
        """Create a new plan."""
        handler = plan_handler.PlanHandler()
        return handler.create(data)

    @exception.wrap_controller_exception
    @wsme_pecan.wsexpose([plan.Plan])
    def get_all(self):
        """Return all plans, based on the query provided."""
        handler = plan_handler.PlanHandler()
        return handler.get_all()
