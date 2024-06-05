// Copyright (c) 2024, yes and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Custom Stock balance report"] = {
	"filters": [
		{
			fieldname: 'item',
			label: __('Item'),
			fieldtype: 'Item',
			options: 'Item',
			default: frappe.defaults.get_user_default('item')
		},

	]
};
// changesss