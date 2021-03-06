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


class WindowsConfiguration(Model):
    """Windows operating system settings to apply to the virtual machine.

    :param enable_automatic_updates: Whether automatic updates are enabled on
     the virtual machine. If omitted, the default value is true.
    :type enable_automatic_updates: bool
    """ 

    _attribute_map = {
        'enable_automatic_updates': {'key': 'enableAutomaticUpdates', 'type': 'bool'},
    }

    def __init__(self, enable_automatic_updates=None):
        self.enable_automatic_updates = enable_automatic_updates
