app_name = "shezle_stock"
app_title = "Shezle Stock"
app_publisher = "yes"
app_description = "Shezle reports"
app_email = "yes@mail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/shezle_stock/css/shezle_stock.css"
# app_include_js = "/assets/shezle_stock/js/shezle_stock.js"

# include js, css files in header of web template
# web_include_css = "/assets/shezle_stock/css/shezle_stock.css"
# web_include_js = "/assets/shezle_stock/js/shezle_stock.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "shezle_stock/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "shezle_stock.utils.jinja_methods",
# 	"filters": "shezle_stock.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "shezle_stock.install.before_install"
# after_install = "shezle_stock.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "shezle_stock.uninstall.before_uninstall"
# after_uninstall = "shezle_stock.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "shezle_stock.utils.before_app_install"
# after_app_install = "shezle_stock.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "shezle_stock.utils.before_app_uninstall"
# after_app_uninstall = "shezle_stock.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "shezle_stock.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"shezle_stock.tasks.all"
# 	],
# 	"daily": [
# 		"shezle_stock.tasks.daily"
# 	],
# 	"hourly": [
# 		"shezle_stock.tasks.hourly"
# 	],
# 	"weekly": [
# 		"shezle_stock.tasks.weekly"
# 	],
# 	"monthly": [
# 		"shezle_stock.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "shezle_stock.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "shezle_stock.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "shezle_stock.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["shezle_stock.utils.before_request"]
# after_request = ["shezle_stock.utils.after_request"]

# Job Events
# ----------
# before_job = ["shezle_stock.utils.before_job"]
# after_job = ["shezle_stock.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"shezle_stock.auth.validate"
# ]
