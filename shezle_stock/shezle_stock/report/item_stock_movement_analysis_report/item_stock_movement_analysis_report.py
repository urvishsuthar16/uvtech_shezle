import frappe
from frappe import _

def execute(filters=None):
    columns = [
       
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
            'fieldname': 'customer_name',
            'label': _('Customer Name'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'total_in_qty',
            'label': _('Total In Qty. (Supplier)'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'e_u_p',
            'label': _('Effective Unit Price (Supplier)'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'n_t_v',
            'label': _('Net Total Value (Supplier)'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'csi',
            'label': _("Total Taxes (CGST / SGST / IGST)"),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 't_a',
            'label': _('Total Additions'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 't_r',
            'label': _('Total Reductions'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 't_g_t_v',
            'label': _('Total Gross Total Value'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'tpt',
            'label': _('Total Packaging Type'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'pq',
            'label': _('Packaging Quantity'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'c_total_in_qty',
            'label': _('Customer Total In Qty.'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'c_e_u_p',
            'label': _('Customer Effective Unit Price'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'c_n_t_v',
            'label': _('Customer Net Total Value'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'ccsi',
            'label': _("Customer Total Taxes (CGST / SGST / IGST)"),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'c_t_a',
            'label': _('Customer Total Additions'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'c_t_r',
            'label': _('Customer Total Reductions'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'c_t_g_t_v',
            'label': _('Customer Total Gross Total Value'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'c_tpt',
            'label': _('Customer Total Packaging Type'),
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'c_pq',
            'label': _('Customer Packaging Quantity'),
            'fieldtype': 'Data',
        },
    ]

    invoices_with_items = get_invoice_with_items()
    sales_orders_with_customers = get_sales_order_with_customer()

    # Construct data dictionary based on retrieved invoices with items and sales orders
    data = []
    for invoice in invoices_with_items:
        customer_data = find_customer_data(invoice.get('item_code'), sales_orders_with_customers)
        data.append({
           
            "item_code_number" :invoice.get('item_code_number'),
            'item_name': invoice.get('item_name'),
            'item_code_name': invoice.get('item_code'),
            'client_id': invoice.get('name'),  # Fill this according to your requirement
            'supplier_name': invoice.get('supplier_name'),
            'customer_name': customer_data.get('customer_name', ''),  # Append customer name
            'total_in_qty': invoice.get('total_qty'),
            'e_u_p': invoice.get('effective_unit_price'),
            'n_t_v': invoice.get('net_total_value'),
            't_a': invoice.get('total_additions'),
            't_r': invoice.get('discount_amount'),
            't_g_t_v': invoice.get('outstanding_amount'),  # Assuming you add this field in the query
            'tpt': invoice.get('uom'),
            'pq': invoice.get('total_qty'),  # Assuming this is the same as total in qty
            'csi': invoice.get('total_gst'),
            'c_total_in_qty': customer_data.get('total_qty', ''),
            'c_e_u_p': customer_data.get('effective_unit_price', ''),
            'c_n_t_v': customer_data.get('net_total_value', ''),
            'c_t_a': customer_data.get('', ''),
            'c_t_r': customer_data.get('discount_amount'),
            'c_t_g_t_v': customer_data.get('outstanding_amount_c', ''),
            'c_tpt': customer_data.get('uom', ''),
            'c_pq': customer_data.get('total_qty', ''),
            'ccsi': customer_data.get('total_gst_c', ''),
        })

    # If you have chart data, define it here
    chart_data = None

    return columns, data, None, chart_data


def get_invoice_with_items():
    # Write a SQL query to retrieve purchase invoices along with supplier, posting date, and items
    sql_query = """
    SELECT 
        pi.supplier AS supplier_name,
       
        pii.item_code,
        pii.item_name,
        SUM(pii.qty) AS total_qty,
        ROUND((SUM(pii.amount) / SUM(pii.qty)), 2) AS effective_unit_price,
        SUM(pii.amount) AS net_total_value,
        
        SUM(CASE WHEN pii.qty < 0 THEN pii.amount ELSE 0 END) AS total_reductions,
        SUM(pii.amount) AS total_gross_total_value,
        pii.uom,
        pi.discount_amount,
        SUM(SUM(pii.amount) + SUM(pii.cgst_amount + pii.sgst_amount + pii.igst_amount - pi.discount_amount)) OVER (PARTITION BY pi.supplier, pii.item_code, pii.item_name) AS outstanding_amount,
        SUM(pii.cgst_amount + pii.sgst_amount + pii.igst_amount) AS total_gst,
        pi.name
    FROM 
        `tabPurchase Invoice` pi
    JOIN 
        `tabPurchase Invoice Item` pii ON pi.name = pii.parent
    WHERE
    pi.update_stock = 1

    GROUP BY 
        pi.supplier, pii.item_code , pii.item_name
    """
    invoices_with_items = frappe.db.sql(sql_query, as_dict=True)
    
    # Fetch additional data from the "Item" table for each item code
    for d in invoices_with_items:
        # Fetch item code from the "Item" table
        item_doc = frappe.get_doc("Item", d['item_code'])
        # Assign additional item data to the dictionary
        d['item_code_number'] = item_doc.variant_of
       
        
         
    return invoices_with_items


def get_sales_order_with_customer():
   
    sql_query = """

    SELECT 
        pi.customer_name AS customer_name,
        pii.item_code,
        pii.item_name,
        SUM(pii.qty) AS total_qty,
        ROUND((SUM(pii.amount) / SUM(pii.qty)), 2) AS effective_unit_price,
        SUM(pii.amount) AS net_total_value,
        SUM(CASE WHEN pii.qty > 0 THEN pii.amount ELSE 0 END) AS total_additions,
        SUM(CASE WHEN pii.qty < 0 THEN pii.amount ELSE 0 END) AS total_reductions,
        SUM(pii.amount) AS total_gross_total_value,
        pii.uom,
        pi.discount_amount,
        SUM(SUM(pii.amount) + SUM(pii.cgst_amount + pii.sgst_amount + pii.igst_amount - pi.discount_amount)) OVER (PARTITION BY pi.customer_name, pii.item_code, pii.item_name) AS outstanding_amount_c,
        SUM(pii.cgst_amount + pii.sgst_amount + pii.igst_amount) AS total_gst_c
    FROM 
        `tabSales Invoice` pi
    JOIN 
        `tabSales Invoice Item` pii ON pi.name = pii.parent
    GROUP BY 
        pi.customer_name, pii.item_code, pii.item_name
    """

    salesorder_with_items = frappe.db.sql(sql_query, as_dict=True)
    return salesorder_with_items


def find_customer_data(item_code, sales_orders):
    for order in sales_orders:
        if order['item_code'] == item_code:
            return order
    return {}
