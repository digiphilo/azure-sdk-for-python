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

from .sub_resource import SubResource


class VirtualMachineScaleSetNetworkConfiguration(SubResource):
    """
    Describes a virtual machine scale set network profile's network
    configurations.

    :param id: Resource Id
    :type id: str
    :param name: Gets or sets the network configuration name.
    :type name: str
    :param primary: Gets or sets whether this is a primary NIC on a virtual
     machine.
    :type primary: bool
    :param ip_configurations: Gets or sets the virtual machine scale set IP
     Configuration.
    :type ip_configurations: list of
     :class:`VirtualMachineScaleSetIPConfiguration
     <azure.mgmt.compute.models.VirtualMachineScaleSetIPConfiguration>`
    """ 

    _validation = {
        'name': {'required': True},
        'ip_configurations': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'primary': {'key': 'properties.primary', 'type': 'bool'},
        'ip_configurations': {'key': 'properties.ipConfigurations', 'type': '[VirtualMachineScaleSetIPConfiguration]'},
    }

    def __init__(self, name, ip_configurations, id=None, primary=None):
        super(VirtualMachineScaleSetNetworkConfiguration, self).__init__(id=id)
        self.name = name
        self.primary = primary
        self.ip_configurations = ip_configurations
