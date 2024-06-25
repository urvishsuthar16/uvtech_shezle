// Copyright (c) 2024, g  and contributors
// For license information, please see license.txt

frappe.query_reports["Item Stock movement analysis report"] = {
    filters: [
        {
            fieldname: 'periodicity',
            label: __('Periodicity'),
            fieldtype: 'Select',
            options: ['Monthly', 'Quarterly', 'Half-Yearly', 'Yearly',''],
            default: 'Yearly',
        }
    ],
}

