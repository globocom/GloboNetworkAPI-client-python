# -*- coding:utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class Pagination():

    @property
    def start_record(self):
        return self.start_record

    @property
    def end_record(self):
        return self.end_record

    @property
    def asorting_cols(self):
        return self.asorting_cols

    @property
    def searchable_columns(self):
        return self.searchable_columns

    @property
    def custom_search(self):
        return self.custom_search

    def __init__(
            self,
            start_record,
            end_record,
            asorting_cols,
            searchable_columns,
            custom_search):
        self.start_record = start_record
        self.end_record = end_record
        self.asorting_cols = asorting_cols
        self.searchable_columns = searchable_columns
        self.custom_search = custom_search
