import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {
            'fieldname': "period",
            'label': _('Period'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'item_code_number',
            'label': _('Item Code Number'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'item_name',
            'label': _('Item Name'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'item_code_name',
            'label': _('Item Code Name (one or multiple)'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'client_id',
            'label': _('Client Id'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'supplier_name',
            'label': _('Supplier Name'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'total_in_qty',
            'label': _('Total In Qty.'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'e_u_p',
            'label': _('Effective Unit Price'),
            'fieldtype': 'Data',
        },

    ]

    invoices_with_items = get_invoice_with_items()
    
    # Construct data dictionary based on retrieved invoices with items
    data = []
    for invoice in invoices_with_items:
        data.append({
            'period': invoice.get('posting_date'),  # Adjust this according to your requirement
            'item_code_number': invoice.get('item_code'),
            'item_name': invoice.get('item_name'),
            'item_code_name': invoice.get('item_code'),
            'client_id': '',  # Fill this according to your requirement
            'supplier_name': invoice.get('supplier'),
            "total_in_qty" : invoice.get('qty')
        })

    # If you have chart data, define it here
    chart_data = None

    return columns, data, None, chart_data


def get_invoice_with_items():
    # Write a SQL query to retrieve purchase invoices along with supplier, posting date, and items
    sql_query = """
    SELECT 
        pi.supplier,
        pi.posting_date,
        pii.item_code,
        pii.item_name,
        pii.qty,
        SUM(pii.qty) AS total_qty
    FROM 
        `tabPurchase Invoice` pi
    JOIN 
        `tabPurchase Invoice Item` pii ON pi.name = pii.parent
    GROUP BY 
        pi.supplier, pi.posting_date, pii.item_code, pii.item_name
"""

    invoices_with_items = frappe.db.sql(sql_query, as_dict=True)
    return invoices_with_items
