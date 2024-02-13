# -*- coding: utf-8 -*-
# Copyright (c) 2020, First ERP and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class UpdateSeries(Document):
	def get_series(self):
		return frappe.db.sql('''select name from `tabSeries`''')
	
@frappe.whitelist()
def get_current(series):
	return frappe.db.sql('''select current from `tabSeries` where name=%s''',series,as_list=True)

@frappe.whitelist()
def update_series(series,current):
	frappe.db.sql('''update `tabSeries` set current=%s where name=%s''',(current,series))