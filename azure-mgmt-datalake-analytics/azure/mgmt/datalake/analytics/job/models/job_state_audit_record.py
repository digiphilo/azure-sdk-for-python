# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobStateAuditRecord(Model):
    """The Data Lake Analytics U-SQL job state audit records for tracking the
    lifecycle of a job.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar new_state: Gets the new state the job is in.
    :vartype new_state: str
    :ivar time_stamp: Gets the time stamp that the state change took place.
    :vartype time_stamp: datetime
    :ivar requested_by_user: Gets the user who requests the change.
    :vartype requested_by_user: str
    :ivar details: Gets  the details of the audit log.
    :vartype details: str
    """ 

    _validation = {
        'new_state': {'readonly': True},
        'time_stamp': {'readonly': True},
        'requested_by_user': {'readonly': True},
        'details': {'readonly': True},
    }

    _attribute_map = {
        'new_state': {'key': 'newState', 'type': 'str'},
        'time_stamp': {'key': 'timeStamp', 'type': 'iso-8601'},
        'requested_by_user': {'key': 'requestedByUser', 'type': 'str'},
        'details': {'key': 'details', 'type': 'str'},
    }

    def __init__(self):
        self.new_state = None
        self.time_stamp = None
        self.requested_by_user = None
        self.details = None
