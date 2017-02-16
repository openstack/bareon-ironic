#
# Copyright 2016 Cray Inc., All Rights Reserved
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

import fixtures

from ironic.tests import base
from ironic.tests.unit.db import base as db_base


class AbstractTestCase(base.TestCase):
    pass


class AbstractDBTestCase(db_base.DbTestCase):
    def setUp(self):
        super(AbstractDBTestCase, self).setUp()

        self.config(enabled_drivers=['bare_swift_ssh'])

        self.temp_dir = self.useFixture(fixtures.TempDir())
