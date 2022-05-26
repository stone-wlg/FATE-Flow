#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
import json

from ._base import BaseEntity


class PermissionParameters(BaseEntity):
    def __init__(self, **kwargs):
        self.src_role = None
        self.src_party_id = None
        self.role = None
        self.command = None
        self.component = None
        self.dataset = {}
        self.valid_period = None
        self.is_delete = False
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

    def to_dict(self):
        d = {}
        for k, v in self.__dict__.items():
            if v is None:
                continue
            d[k] = v
        return d


class DataSet(BaseEntity):
    def __init__(self, namespace, name, **kwargs):
        self.namespace = namespace
        self.name = name

    def to_dict(self):
        d = {}
        for k, v in self.__dict__.items():
            if v is None:
                continue
            d[k] = v
        return d

    @property
    def value(self):
        return json.dumps(self.to_dict(), sort_keys=True)

    def check(self):
        if not self.name or not self.namespace:
            raise ValueError(f"name {self.name} or namespace {self.namespace} is null")


class CheckReturn:
    SUCCESS = 0
    NO_ROLE_PERMISSION = 1
    NO_COMPONENT_PERMISSION = 2
    NO_DATASET_PERMISSION = 3
