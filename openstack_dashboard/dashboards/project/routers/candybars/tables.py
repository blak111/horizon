# vim: tabstop=4 shiftwidth=4 softtabstop=4

#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import logging

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tables

LOG = logging.getLogger(__name__)




class RemoveCandyBar(tables.DeleteAction):
    data_type_singular = _("Candy Bar")
    data_type_plural = _("Candy Bars")
    name = "candymustgo"
    failure_url = 'horizon:project:routers:detail'

    def delete(self, request, obj_id):
        try:
            LOG.info('Deleted candy bar') 
        except:
            msg = _('Failed to delete candy bar %s') % obj_id
            LOG.info(msg)


class CandyBarsTable(tables.DataTable):
    name = tables.Column("name", verbose_name=_("Name"))
    flavor = tables.Column("flavor", verbose_name=_("flavor"))


    class Meta:
        name = "candybars"
        verbose_name = _("Candy Bars")
        table_actions = (RemoveCandyBar,)
        row_actions = (RemoveCandyBar, )

