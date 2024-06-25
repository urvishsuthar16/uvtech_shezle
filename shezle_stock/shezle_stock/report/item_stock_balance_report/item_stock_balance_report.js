// Copyright (c) 2024, yes and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["item Stock Balance report"] = {
	filters: [
        {
            fieldname: 'periodicity',
            label: __('Periodicity'),
            fieldtype: 'Select',
            options: ['Monthly', 'Quarterly', 'Half-Yearly', 'Yearly',''],
            default: 'Yearly',
        }
    ],
};
