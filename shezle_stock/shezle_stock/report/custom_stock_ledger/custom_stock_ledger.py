import frappe

def execute(filters):
    item_filter = filters.get('item')
    customer_filter = filters.get('customer')

    # Get column definitions
    columns = get_columns()

    # Fetch and compile data with filters
    invoices_with_items = get_invoice_with_items(item_filter)
    invoices_with_items_purchase = get_invoice_with_items_purchase(item_filter)
    sales_orders_with_customers = get_sales_order_with_customer(item_filter, customer_filter)
    invoices_with_items_return = get_invoice_with_items_return(item_filter)
    sales_orders_with_customers_return = get_sales_order_with_customer_return(item_filter, customer_filter)

    # Combine data from different sources
    data = compile_data(invoices_with_items, sales_orders_with_customers)
    data += compile_data(invoices_with_items_purchase, sales_orders_with_customers)
    data += compile_data(invoices_with_items_return, sales_orders_with_customers_return)

    chart_data = None  # Placeholder for chart data if needed
    return columns, data, None, chart_data

def get_columns():
    return [
        {'fieldname': 'date', 'label': 'Date', 'fieldtype': 'Date'},
        {'fieldname': 'parenttype', 'label': 'IN Voucher Type', 'fieldtype': 'Data'},
        {'fieldname': 'item_code_number', 'label': 'Item Code Number', 'fieldtype': 'Data'},
        {'fieldname': 'item_name', 'label': 'Item Name', 'fieldtype': 'Data'},
        {'fieldname': 'item_code', 'label': 'Item Code Name', 'fieldtype': 'Data'},
        {'fieldname': 'barcode', 'label': 'Barcode No', 'fieldtype': 'Data'},
        {'fieldname': 'stock_uom', 'label': 'Stock Unit', 'fieldtype': 'Data'},
        {'fieldname': 'item_group', 'label': 'Item Group', 'fieldtype': 'Link', 'options': 'Item Group'},
        {'fieldname': 'client_id', 'label': 'Client ID', 'fieldtype': 'Data'},
        {'fieldname': 'supplier_name', 'label': 'Supplier Name', 'fieldtype': 'Data'},
        {'fieldname': 'customer_name', 'label': 'Customer Name', 'fieldtype': 'Data'},
        {'fieldname': 'in_qty', 'label': 'In Qty', 'fieldtype': 'Data'},
        {'fieldname': 'unit_price', 'label': 'Unit Price', 'fieldtype': 'Data'},
        {'fieldname': 'net_total_value', 'label': 'Net Total Value', 'fieldtype': 'Data'},
        {'fieldname': 'taxes', 'label': 'Taxes', 'fieldtype': 'Data'},
        {'fieldname': 'additions', 'label': 'Additions', 'fieldtype': 'Data'},
        {'fieldname': 'reductions', 'label': 'Reductions', 'fieldtype': 'Data'},
        {'fieldname': 'gross_total_value', 'label': 'Gross Total Value', 'fieldtype': 'Data'},
        {'fieldname': 'warehouse_id_in', 'label': 'Warehouse ID', 'fieldtype': 'Data'},
        {'fieldname': 'warehouse_name_in', 'label': 'Warehouse Name', 'fieldtype': 'Data'},
        {'fieldname': 'location_name_in', 'label': 'Location Name', 'fieldtype': 'Data'},
        {'fieldname': 'location_id_in', 'label': 'Location ID', 'fieldtype': 'Data'},
        {'fieldname': 'packaging_type_in', 'label': 'Packaging Type', 'fieldtype': 'Data'},
        {'fieldname': 'packaging_qty_in', 'label': 'Packaging Quantity', 'fieldtype': 'Data'},
        {'fieldname': 'voucher_type_out', 'label': 'Out Voucher Type', 'fieldtype': 'Data'},
        {'fieldname': 'out_qty', 'label': 'Out Qty', 'fieldtype': 'Data'},
        {'fieldname': 'unit_price_out', 'label': 'Unit Price', 'fieldtype': 'Data'},
        {'fieldname': 'net_total_value_out', 'label': 'Net Total Value', 'fieldtype': 'Data'},
        {'fieldname': 'taxes_out', 'label': 'Taxes', 'fieldtype': 'Data'},
        {'fieldname': 'additions_out', 'label': 'Additions', 'fieldtype': 'Data'},
        {'fieldname': 'reductions_out', 'label': 'Reductions', 'fieldtype': 'Data'},
        {'fieldname': 'gross_total_value_out', 'label': 'Gross Total Value', 'fieldtype': 'Data'},
        {'fieldname': 'warehouse_id_out', 'label': 'Warehouse ID', 'fieldtype': 'Data'},
        {'fieldname': 'warehouse_name_out', 'label': 'Warehouse Name', 'fieldtype': 'Data'},
        {'fieldname': 'location_name_out', 'label': 'Location Name', 'fieldtype': 'Data'},
        {'fieldname': 'location_id_out', 'label': 'Location ID', 'fieldtype': 'Data'},
        {'fieldname': 'packaging_type_out', 'label': 'Packaging Type', 'fieldtype': 'Data'},
        {'fieldname': 'packaging_qty_out', 'label': 'Packaging Quantity', 'fieldtype': 'Data'},
    ]

def compile_data(invoices, sales_orders_with_customers):
    data = []
    for invoice in invoices:
        customer_data = find_customer_data(invoice.get('item_code'), sales_orders_with_customers)
        data.append({
            'date': invoice.get('posting_date'),
            'parenttype': invoice.get('parenttype'),
            'item_code_number': invoice.get('item_code_number'),
            'item_name': invoice.get('item_name'),
            'item_code': invoice.get('item_code'),
            'barcode': invoice.get('barcode'),
            'stock_uom': invoice.get('uom'),
            'item_group': invoice.get('item_group'),
            'client_id': invoice.get('client_id'),
            'supplier_name': invoice.get('supplier_name'),
            'customer_name': customer_data.get('customer_name', ''),
            'in_qty': invoice.get('total_qty'),
            'unit_price': invoice.get('effective_unit_price'),
            'net_total_value': invoice.get('net_total_value'),
            'taxes': invoice.get('total_gst'),
            'additions': invoice.get('total_additions', ''),
            'reductions': invoice.get('discount_amount', ''),
            'gross_total_value': invoice.get('total_gross_total_value'),
            'location_name_in': invoice.get('location_name_in'),
            'location_id_in': invoice.get('location_id'),
            'packaging_type_in': invoice.get('uom'),
            'packaging_qty_in': invoice.get('total_qty'),
            'voucher_type_out': customer_data.get('parenttype', ''),
            'out_qty': customer_data.get('total_qty', ''),
            'unit_price_out': customer_data.get('effective_unit_price', ''),
            'net_total_value_out': customer_data.get('net_total_value', ''),
            'taxes_out': customer_data.get('total_gst', ''),
            'additions_out': customer_data.get('total_additions', ''),
            'reductions_out': customer_data.get('discount_amount', ''),
            'gross_total_value_out': customer_data.get('total_gross_total_value', ''),
            'warehouse_id_out': customer_data.get('warehouse_id_out', ''),
            'warehouse_name_out': customer_data.get('warehouse', ''),
            'location_name_out': customer_data.get('location_name_out', ''),
            'location_id_out': customer_data.get('location_id', ''),
            'packaging_type_out': customer_data.get('uom', ''),
            'packaging_qty_out': customer_data.get('total_qty', ''),
        })
    return data

def get_invoice_with_items(item_name=None):
    conditions = ""
    if item_name:
        conditions += f" AND pii.item_code = '{item_name}'"
        
    sql_query = f"""
    SELECT 
        pii.parenttype,
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
        SUM(pii.cgst_amount + pii.sgst_amount + pii.igst_amount) AS total_gst
    FROM 
        `tabPurchase Invoice` pi
    JOIN 
        `tabPurchase Invoice Item` pii ON pi.name = pii.parent
    WHERE
        pi.update_stock = 1
        {conditions}
    GROUP BY 
        pi.supplier, pii.item_code, pii.item_name
    """
    invoices_with_items = frappe.db.sql(sql_query, as_dict=True)
    
    for d in invoices_with_items:
        item_doc = frappe.get_doc("Item", d['item_code'])
        d['item_code_number'] = item_doc.variant_of if item_doc else ''
        d['item_group'] = item_doc.item_group if item_doc else ''
        
        barcodes = item_doc.get('barcodes')
        if barcodes:
            d['barcode'] = barcodes[0].barcode

    return invoices_with_items

def get_invoice_with_items_purchase(item_name=None):
    conditions = ""
    if item_name:
        conditions += f" AND pii.item_code = '{item_name}'"
        
    sql_query = f"""
    SELECT 
        pii.parenttype,
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
        SUM(pii.cgst_amount + pii.sgst_amount + pii.igst_amount) AS total_gst
    FROM 
        `tabPurchase Invoice` pi
    JOIN 
        `tabPurchase Invoice Item` pii ON pi.name = pii.parent
    WHERE
        pi.update_stock = 0
        {conditions}
    GROUP BY 
        pi.supplier, pii.item_code, pii.item_name
    """
    invoices_with_items = frappe.db.sql(sql_query, as_dict=True)
    
    for d in invoices_with_items:
        item_doc = frappe.get_doc("Item", d['item_code'])
        d['item_code_number'] = item_doc.variant_of if item_doc else ''
        d['item_group'] = item_doc.item_group if item_doc else ''
        
        barcodes = item_doc.get('barcodes')
        if barcodes:
            d['barcode'] = barcodes[0].barcode

    return invoices_with_items

def get_sales_order_with_customer(item_name=None, customer_name=None):
    conditions = ""
    
    if customer_name:
        conditions += f" AND so.customer_name = '{customer_name}'"
    
    sql_query = f"""
    SELECT
        sii.parenttype,
        sii.item_code,
        so.customer_name,
        SUM(sii.qty) AS total_qty,
        ROUND((SUM(sii.amount) / SUM(sii.qty)), 2) AS effective_unit_price,
        SUM(sii.amount) AS net_total_value,
        SUM(CASE WHEN sii.qty < 0 THEN sii.amount ELSE 0 END) AS total_reductions,
        SUM(sii.amount) AS total_gross_total_value,
        sii.uom,
        so.discount_amount,
        SUM(sii.cgst_amount + sii.sgst_amount + sii.igst_amount) AS total_gst
        
    FROM
        `tabSales Order` so
    JOIN
        `tabSales Order Item` sii ON so.name = sii.parent
    WHERE
        1=1
        {conditions}
    GROUP BY
        sii.item_code, so.customer_name
    """
    sales_orders_with_customers = frappe.db.sql(sql_query, as_dict=True)
    return sales_orders_with_customers

def get_invoice_with_items_return(item_name=None):
    conditions = ""
    if item_name:
        conditions += f" AND sii.item_code = '{item_name}'"
        
    sql_query = f"""
    SELECT 
        sii.parenttype,
        si.customer_name,
        sii.item_code,
        sii.item_name,
        SUM(sii.qty) AS total_qty,
        ROUND((SUM(sii.amount) / SUM(sii.qty)), 2) AS effective_unit_price,
        SUM(sii.amount) AS net_total_value,
        SUM(CASE WHEN sii.qty < 0 THEN sii.amount ELSE 0 END) AS total_reductions,
        SUM(sii.amount) AS total_gross_total_value,
        sii.uom,
        si.discount_amount,
        SUM(sii.cgst_amount + sii.sgst_amount + sii.igst_amount) AS total_gst
    FROM 
        `tabSales Invoice` si
    JOIN 
        `tabSales Invoice Item` sii ON si.name = sii.parent
    WHERE
        si.is_return = 1
        {conditions}
    GROUP BY 
        sii.item_code, si.customer_name
    """
    invoices_with_items = frappe.db.sql(sql_query, as_dict=True)
    
    for d in invoices_with_items:
        item_doc = frappe.get_doc("Item", d['item_code'])
        d['item_code_number'] = item_doc.variant_of if item_doc else ''
        d['item_group'] = item_doc.item_group if item_doc else ''
        
        barcodes = item_doc.get('barcodes')
        if barcodes:
            d['barcode'] = barcodes[0].barcode

    return invoices_with_items

def get_sales_order_with_customer_return(item_name=None, customer_name=None):
    # Initialize the conditions string
    conditions = ""
    
    # Append item name condition if provided
    
    
    # Append customer name condition if provided
    if customer_name:
        conditions += f" AND si.customer_name = '{customer_name}'"
    
    # SQL query to retrieve the sales orders with customer returns
    sql_query = f"""
    SELECT
        sii.parenttype,
        sii.item_code,
        si.customer_name,
        SUM(sii.qty) AS total_qty,
        ROUND((SUM(sii.amount) / SUM(sii.qty)), 2) AS effective_unit_price,
        SUM(sii.amount) AS net_total_value,
        SUM(CASE WHEN sii.qty < 0 THEN sii.amount ELSE 0 END) AS total_reductions,
        SUM(sii.amount) AS total_gross_total_value,
        sii.uom,
        si.discount_amount,
        SUM(sii.cgst_amount + sii.sgst_amount + sii.igst_amount) AS total_gst
    FROM
        `tabSales Invoice` si
    JOIN
        `tabSales Invoice Item` sii ON si.name = sii.parent
    WHERE
        si.is_return = 1
        {conditions}
    GROUP BY
        sii.item_code, si.customer_name
    """
    
    # Execute the SQL query
    sales_orders_with_customers = frappe.db.sql(sql_query, as_dict=True)
    
    # Return the query results
    return sales_orders_with_customers

def find_customer_data(item_code, sales_orders_with_customers):
    # Iterate through the list of sales orders with customer returns
    for order in sales_orders_with_customers:
        # Return the order if the item code matches
        if order['item_code'] == item_code:
            return order
    
    # Return an empty dictionary if no matching item code is found
    return {}
