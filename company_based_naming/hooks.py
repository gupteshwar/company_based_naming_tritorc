# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "company_based_naming"
app_title = "Company Based Naming"
app_publisher = "First ERP"
app_description = "Set naming of any doctype based on company "
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "support@firsterp.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/company_based_naming/css/company_based_naming.css"
# app_include_js = "/assets/company_based_naming/js/company_based_naming.js"

# include js, css files in header of web template
# web_include_css = "/assets/company_based_naming/css/company_based_naming.css"
# web_include_js = "/assets/company_based_naming/js/company_based_naming.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "company_based_naming.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "company_based_naming.install.before_install"
# after_install = "company_based_naming.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "company_based_naming.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"Sales Invoice": {
# 		"autoname": "company_based_naming.custom_methods.custom_autoname"
# 	},
# 	"Quotation": {
# 		"autoname": "company_based_naming.custom_methods.custom_autoname"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"company_based_naming.tasks.all"
# 	],
# 	"daily": [
# 		"company_based_naming.tasks.daily"
# 	],
# 	"hourly": [
# 		"company_based_naming.tasks.hourly"
# 	],
# 	"weekly": [
# 		"company_based_naming.tasks.weekly"
# 	]
# 	"monthly": [
# 		"company_based_naming.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "company_based_naming.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "company_based_naming.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "company_based_naming.task.get_dashboard_data"
# }

fixtures = [
	"Client Script"
]