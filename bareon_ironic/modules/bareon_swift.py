#
# 2016 Cray Inc., All Rights Reserved
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

"""
Bareon Swift deploy driver.
"""

from ironic.openstack.common import log

from bareon_ironic.modules import bareon_base
from bareon_ironic.modules.resources import resources

LOG = log.getLogger(__name__)


class BareonSwiftDeploy(bareon_base.BareonDeploy):
    """Interface for deploy-related actions."""

    def _get_deploy_driver(self):
        return 'swift'

    def _get_image_resource_mode(self):
        return resources.PullSwiftTempurlResource.MODE


class BareonSwiftVendor(bareon_base.BareonVendor):
    pass
