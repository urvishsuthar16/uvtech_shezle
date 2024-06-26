import frappe
from frappe import _
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

def execute(filters=None):
    columns, data = get_data(filters)
    return columns, data

def get_data(filters):
    columns = [
        {'fieldname': 'item_code_number', 'label': _('Item Code Number'), 'fieldtype': 'Data'},
        {'fieldname': 'item_name', 'label': _('Item Name'), 'fieldtype': 'Data'},
        {'fieldname': 'item_code_name', 'label': _('Item Code Name (one or multiple)'), 'fieldtype': 'Data'},
        {'fieldname': 'client_id', 'label': _('Client Id'), 'fieldtype': 'Data'},
        {'fieldname': 'supplier_name', 'label': _('Supplier Name'), 'fieldtype': 'Data'},
        {'fieldname': 'customer_name', 'label': _('Customer Name'), 'fieldtype': 'Data'},
        {'fieldname': 'total_in_qty', 'label': _('Total In Qty. (Supplier)'), 'fieldtype': 'Data'},
        {'fieldname': 'e_u_p', 'label': _('Effective Unit Price (Supplier)'), 'fieldtype': 'Data'},
        {'fieldname': 'n_t_v', 'label': _('Net Total Value (Supplier)'), 'fieldtype': 'Data'},
        {'fieldname': 'csi', 'label': _("Total Taxes (CGST / SGST / IGST)"), 'fieldtype': 'Data'},
        {'fieldname': 't_a', 'label': _('Total Additions'), 'fieldtype': 'Data'},
        {'fieldname': 't_r', 'label': _('Total Reductions'), 'fieldtype': 'Data'},
        {'fieldname': 't_g_t_v', 'label': _('Total Gross Total Value'), 'fieldtype': 'Data'},
        {'fieldname': 'tpt', 'label': _('Total Packaging Type'), 'fieldtype': 'Data'},
        {'fieldname': 'pq', 'label': _('Packaging Quantity'), 'fieldtype': 'Data'},
        {'fieldname': 'c_total_in_qty', 'label': _('Customer Total In Qty.'), 'fieldtype': 'Data'},
        {'fieldname': 'c_e_u_p', 'label': _('Customer Effective Unit Price'), 'fieldtype': 'Data'},
        {'fieldname': 'c_n_t_v', 'label': _('Customer Net Total Value'), 'fieldtype': 'Data'},
        {'fieldname': 'ccsi', 'label': _("Customer Total Taxes (CGST / SGST / IGST)"), 'fieldtype': 'Data'},
        {'fieldname': 'c_t_a', 'label': _('Customer Total Additions'), 'fieldtype': 'Data'},
        {'fieldname': 'c_t_r', 'label': _('Customer Total Reductions'), 'fieldtype': 'Data'},
        {'fieldname': 'c_t_g_t_v', 'label': _('Customer Total Gross Total Value'), 'fieldtype': 'Data'},
        {'fieldname': 'c_tpt', 'label': _('Customer Total Packaging Type'), 'fieldtype': 'Data'},
        {'fieldname': 'c_pq', 'label': _('Customer Packaging Quantity'), 'fieldtype': 'Data'},
        {'fieldname': 'posting_date', 'label': _('Posting Date'), 'fieldtype': 'Date'},
    ]

    from_date = filters.get('from_date')
    to_date = filters.get('to_date')
    invoices_with_items = get_invoice_with_items(from_date, to_date)
    sales_orders_with_customers = get_sales_order_with_customer(from_date, to_date)

    periodicity = filters.get('periodicity', 'Yearly')
    if periodicity != 'All':
        invoices_with_items = apply_periodicity_filter(invoices_with_items, periodicity)

    data = []
    for invoice in invoices_with_items:
        customer_data = find_customer_data(invoice.get('item_code'), sales_orders_with_customers)
        data.append({
            'item_code_number': invoice.get('item_code_number'),
            'item_name': invoice.get('item_name'),
            'item_code_name': invoice.get('item_code'),
            'client_id': customer_data.get('customer_name'),
            'supplier_name': invoice.get('supplier_name'),
            'customer_name': customer_data.get('customer_name', ''),
            'total_in_qty': invoice.get('total_qty'),
            'e_u_p': invoice.get('effective_unit_price'),
            'n_t_v': invoice.get('net_total_value'),
            'csi': invoice.get('total_gst'),
            't_a': invoice.get('total_additions'),
            't_r': invoice.get('discount_amount'),
            't_g_t_v': invoice.get('outstanding_amount'),
            'tpt': invoice.get('uom'),
            'pq': invoice.get('total_qty'),
            'c_total_in_qty': customer_data.get('total_qty', ''),
            'c_e_u_p': customer_data.get('effective_unit_price', ''),
            'c_n_t_v': customer_data.get('net_total_value', ''),
            'ccsi': customer_data.get('total_gst_c', ''),
            'c_t_a': customer_data.get('total_additions', ''),
            'c_t_r': customer_data.get('discount_amount', ''),
            'c_t_g_t_v': customer_data.get('outstanding_amount_c', ''),
            'c_tpt': customer_data.get('uom', ''),
            'c_pq': customer_data.get('total_qty', ''),
            'posting_date': invoice.get('posting_date'),
        })

    return columns, data

def apply_periodicity_filter(data, periodicity):
    today = datetime.today()

    if periodicity == 'Monthly':
        start_date = today - relativedelta(months=1)
    elif periodicity == 'Quarterly':
        start_date = today - relativedelta(months=3)
    elif periodicity == 'Half-Yearly':
        start_date = today - relativedelta(months=6)
    elif periodicity == 'Yearly':
        start_date = today - relativedelta(years=1)
    else:
        start_date = None

    if not start_date:
        return data

    filtered_data = []
    for d in data:
        posting_date_str = d.get('posting_date')
        if posting_date_str:
            posting_date = parse_date(posting_date_str)
            if posting_date:
                # Convert posting_date to datetime for comparison
                posting_datetime = datetime.combine(posting_date, datetime.min.time())
                if posting_datetime >= start_date:
                    filtered_data.append(d)

    return filtered_data

def parse_date(date_str):
    try:
        if isinstance(date_str, datetime):
            return date_str.date()
        elif isinstance(date_str, str):
            return datetime.strptime(date_str, '%Y-%m-%d').date()
        elif isinstance(date_str, date):  # Handle datetime.date objects
            return date_str
        else:
            raise TypeError(f"Unsupported type for date_str: {type(date_str)}")
    except Exception as e:
        frappe.log_error(f"Date parsing error: {e}, date_str: {date_str}")
        return None

def get_invoice_with_items(from_date=None, to_date=None):
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
        pi.name,
        pi.posting_date
    FROM 
        `tabPurchase Invoice` pi
    JOIN 
        `tabPurchase Invoice Item` pii ON pi.name = pii.parent
    WHERE
        pi.update_stock = 1
        AND (%(from_date)s IS NULL OR pi.posting_date >= %(from_date)s)
        AND (%(to_date)s IS NULL OR pi.posting_date <= %(to_date)s)
    GROUP BY 
        pi.supplier, pii.item_code, pii.item_name
    """
    invoices_with_items = frappe.db.sql(sql_query, {'from_date': from_date, 'to_date': to_date}, as_dict=True)

    for d in invoices_with_items:
        item_doc = frappe.get_doc("Item", d['item_code'])
        d['item_code_number'] = item_doc.variant_of

    return invoices_with_items

def get_sales_order_with_customer(from_date=None, to_date=None):
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
        SUM(pii.cgst_amount + pii.sgst_amount + pii.igst_amount) AS total_gst_c,
        pi.posting_date
    FROM 
        `tabSales Invoice` pi
    JOIN 
        `tabSales Invoice Item` pii ON pi.name = pii.parent
    WHERE
        (%(from_date)s IS NULL OR pi.posting_date >= %(from_date)s)
        AND (%(to_date)s IS NULL OR pi.posting_date <= %(to_date)s)
    GROUP BY 
        pi.customer_name, pii.item_code, pii.item_name
    """
    salesorder_with_items = frappe.db.sql(sql_query, {'from_date': from_date, 'to_date': to_date}, as_dict=True)
    return salesorder_with_items

def find_customer_data(item_code, sales_orders):
    for order in sales_orders:
        if order['item_code'] == item_code:
            return order
    return {}
