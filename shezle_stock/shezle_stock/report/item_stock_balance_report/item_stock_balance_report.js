// Copyright (c) 2024, yes and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["item Stock Balance report"] = {
	filters: [
        {
            fieldname: 'periodicity',
            label: __('Periodicity'),
            fieldtype: 'Select',
            options: ['Monthly', 'Quarterly', 'Half-Yearly', 'Yearly', 'Custom'],
            default: 'Yearly',
            change: () => {
                const today = frappe.datetime.get_today();
                const periodicity = frappe.query_report.get_filter_value('periodicity');
                console.log(periodicity)
                
                if (periodicity === 'Monthly') {
                    frappe.query_report.set_filter_value('to_date',today)
                    let month1 = frappe.datetime.add_months(today, -1);
                    frappe.query_report.set_filter_value('from_date',month1)

                } else if (periodicity === 'Quarterly') {
                    frappe.query_report.set_filter_value('to_date',today)
                    let month1 = frappe.datetime.add_months(today, -3);
                    frappe.query_report.set_filter_value('from_date',month1)

                } else if (periodicity === 'Half-Yearly') {
                    frappe.query_report.set_filter_value('to_date',today)
                    let month1 = frappe.datetime.add_months(today, -6);
                    frappe.query_report.set_filter_value('from_date',month1)
                } else if (periodicity === 'Yearly') {
                    frappe.query_report.set_filter_value('to_date',today)
                    let month1 = frappe.datetime.add_months(today, -12);
                    frappe.query_report.set_filter_value('from_date',month1)
                } else {
                    // Handle 'Custom' periodicity or default to today's date
                    return today;
                }
            }
        },
        {
            fieldname: 'from_date',
            label: __('From Date'),
            fieldtype: 'Date',
            // change: () => {
                
            //     frappe.query_report.set_filter_value('periodicity','Custom');
                
            //     console.log(periodicity)
                
                
            // }
        
            

            
        },
        {
            fieldname: 'to_date',
            label: __('To Date'),
            fieldtype: 'Date',
            default: frappe.datetime.get_today(),  // Default to today's date
        }
		
		
	],
        
    
};
