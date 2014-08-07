# -*- coding:utf-8 -*-
"""
Title: Infrastructure NetworkAPI
Author: avanzolin / S2it
Copyright: ( c )  2009 globo.com todos os direitos reservados.
"""

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
    
    def __init__(self, start_record, end_record, asorting_cols, searchable_columns, custom_search):
        self.start_record = start_record
        self.end_record = end_record
        self.asorting_cols = asorting_cols
        self.searchable_columns = searchable_columns
        self.custom_search = custom_search