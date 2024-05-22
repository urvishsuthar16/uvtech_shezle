import frappe

# def execute(filters):
#     columns = [
#         {'fieldname': 'date', 'label': 'Date', 'fieldtype': 'Date'},
#         {'fieldname': 'parenttype', 'label': 'IN Voucher Type', 'fieldtype': 'Data'},
#         {'fieldname': 'item_code_number', 'label': 'Item Code Number', 'fieldtype': 'Data'},
#         {'fieldname': 'item_name', 'label': 'Item Name', 'fieldtype': 'Data'},
#         {'fieldname': 'item_code', 'label': 'Item Code Name', 'fieldtype': 'Data'},
#         {'fieldname': 'barcode', 'label': 'Barcode No', 'fieldtype': 'Data'},
#         {'fieldname': 'stock_uom', 'label': 'Stock Unit', 'fieldtype': 'Data'},
#         {'fieldname': 'item_group', 'label': 'Item Group', 'fieldtype': 'Link', 'options': 'Item Group'},
#         {'fieldname': 'client_id', 'label': 'Client ID', 'fieldtype': 'Data'},
#         {'fieldname': 'supplier_name', 'label': 'Supplier Name', 'fieldtype': 'Data'},
#         {'fieldname': 'customer_name', 'label': 'Customer Name', 'fieldtype': 'Data'},
#         {'fieldname': 'in_qty', 'label': 'In Qty', 'fieldtype': 'Data'},
#         {'fieldname': 'unit_price', 'label': 'Unit Price', 'fieldtype': 'Data'},
#         {'fieldname': 'net_total_value', 'label': 'Net Total Value', 'fieldtype': 'Data'},
#         {'fieldname': 'taxes', 'label': 'Taxes', 'fieldtype': 'Data'},
#         {'fieldname': 'additions', 'label': 'Additions', 'fieldtype': 'Data'},
#         {'fieldname': 'reductions', 'label': 'Reductions', 'fieldtype': 'Data'},
#         {'fieldname': 'gross_total_value', 'label': 'Gross Total Value', 'fieldtype': 'Data'},
#         {'fieldname': 'warehouse_id_in', 'label': 'Warehouse ID', 'fieldtype': 'Data'},
#         {'fieldname': 'warehouse_name_in', 'label': 'Warehouse Name', 'fieldtype': 'Data'},
#         {'fieldname': 'location_name_in', 'label': 'Location Name', 'fieldtype': 'Data'},
#         {'fieldname': 'location_id_in', 'label': 'Location ID', 'fieldtype': 'Data'},
#         {'fieldname': 'packaging_type_in', 'label': 'Packaging Type', 'fieldtype': 'Data'},
#         {'fieldname': 'packaging_qty_in', 'label': 'Packaging Quantity', 'fieldtype': 'Data'},
#         {'fieldname': 'voucher_type_out', 'label': 'Out Voucher Type', 'fieldtype': 'Data'},
#         {'fieldname': 'out_qty', 'label': 'Out Qty', 'fieldtype': 'Data'},
#         {'fieldname': 'unit_price_out', 'label': 'Unit Price ', 'fieldtype': 'Data'},
#         {'fieldname': 'net_total_value_out', 'label': 'Net Total Value ', 'fieldtype': 'Data'},
#         {'fieldname': 'taxes_out', 'label': 'Taxes ', 'fieldtype': 'Data'},
#         {'fieldname': 'additions_out', 'label': 'Additions ', 'fieldtype': 'Data'},
#         {'fieldname': 'reductions_out', 'label': 'Reductions ', 'fieldtype': 'Data'},
#         {'fieldname': 'gross_total_value_out', 'label': 'Gross Total Value ', 'fieldtype': 'Data'},
#         {'fieldname': 'warehouse_id_out', 'label': 'Warehouse ID ', 'fieldtype': 'Data'},
#         {'fieldname': 'warehouse_name_out', 'label': 'Warehouse Name ()', 'fieldtype': 'Data'},
#         {'fieldname': 'location_name_out', 'label': 'Location Name ', 'fieldtype': 'Data'},
#         {'fieldname': 'location_id_out', 'label': 'Location ID ', 'fieldtype': 'Data'},
#         {'fieldname': 'packaging_type_out', 'label': 'Packaging Type ', 'fieldtype': 'Data'},
#         {'fieldname': 'packaging_qty_out', 'label': 'Packaging Quantity ', 'fieldtype': 'Data'},
#     ]
    
#     invoices_with_items = get_invoice_with_items()
#     get_invoice_with_items_purchse1 = get_invoice_with_items_purchse()
#     sales_orders_with_customers = get_sales_order_with_customer()
    
    
#     data = []
#     for invoice in invoices_with_items:
       
#         customer_data = find_customer_data(invoice.get('item_code'), sales_orders_with_customers)
#         data.append({
#             'date': invoice.get('posting_date'),
#             'parenttype': invoice.get('parenttype'),
#             'item_code_number': invoice.get('item_code_number'),
#             'item_name': invoice.get('item_name'),
#             'item_code': invoice.get('item_code'),
#             'barcode': invoice.get('barcode'),
#             'stock_uom': invoice.get('uom'),
#             'item_group': invoice.get('item_group'),
#             'client_id': invoice.get('client_id'),
#             'supplier_name': invoice.get('supplier_name'),
#             'customer_name': customer_data.get('customer_name', ''),
#             'in_qty': invoice.get('total_qty'),
#             'unit_price': invoice.get('effective_unit_price'),
#             'net_total_value': invoice.get('net_total_value'),
#             'taxes': invoice.get('total_gst'),
#             'additions': invoice.get('total_additions'),
#             'reductions': invoice.get('discount_amount'),
#             'gross_total_value': invoice.get('total_gross_total_value'),
#             'warehouse_id_in': invoice.get('warehouse_id_in'),
#             'warehouse_name_in': invoice.get('warehouse'),
#             'location_name_in': invoice.get('location_name_in'),
#             'location_id_in': invoice.get('location_id'),
#             'packaging_type_in': invoice.get('uom'),
#             'packaging_qty_in': invoice.get('total_qty'),
#             'voucher_type_out': customer_data.get('parenttype', ''),
#             'out_qty': customer_data.get('total_qty', ''),
#             'unit_price_out': customer_data.get('effective_unit_price', ''),
#             'net_total_value_out': customer_data.get('net_total_value', ''),
#             'taxes_out': customer_data.get('total_gst', ''),
#             'additions_out': customer_data.get('total_additions', ''),
#             'reductions_out': customer_data.get('discount_amount', ''),
#             'gross_total_value_out': customer_data.get('total_gross_total_value', ''),
#             'warehouse_id_out': customer_data.get('warehouse_id_out', ''),
#             'warehouse_name_out': customer_data.get('warehouse', ''),
#             'location_name_out': customer_data.get('location_name_out', ''),
#             'location_id_out': customer_data.get('location_id', ''),
#             'packaging_type_out': customer_data.get('uom', ''),
#             'packaging_qty_out': customer_data.get('total_qty', ''),
#         })
    
#     chart_data = None
#     return columns, data, None, chart_data
def execute(filters):
    # Get column definitions
    columns = get_columns()
    
    # Fetch and compile data
    invoices_with_items = get_invoice_with_items()
    invoices_with_items_purchase = get_invoice_with_items_purchse()
    sales_orders_with_customers = get_sales_order_with_customer()
    get_invoice_with_items_return = get_invoice_with_items_return_not()
    get_sales_order_with_customer_return = get_sales_order_with_customer_return_not()
    
    # Combine data from different sources
    data = compile_data(invoices_with_items, sales_orders_with_customers)
    data += compile_data(invoices_with_items_purchase, sales_orders_with_customers)
    data += compile_data(get_invoice_with_items_return, get_sales_order_with_customer_return)

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
            'warehouse_id_in': invoice.get('warehouse_id_in'),
            'warehouse_name_in': invoice.get('warehouse'),
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

def get_invoice_with_items():
    sql_query = """
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
        pii.warehouse,
        pi.discount_amount,
        SUM(pii.cgst_amount + pii.sgst_amount + pii.igst_amount) AS total_gst
    FROM 
        `tabPurchase Invoice` pi
    JOIN 
        `tabPurchase Invoice Item` pii ON pi.name = pii.parent
    WHERE
    pi.update_stock = 1
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
        else:
            d['barcode'] = ''

    for w in invoices_with_items:
        Warehouse = frappe.get_doc('Warehouse', w['warehouse'])
        w['warehouse_id_in'] = Warehouse.warehouse_name
        w['location_name_in'] = Warehouse.custom_location
    
    return invoices_with_items

def get_sales_order_with_customer():
    sql_query = """
    SELECT 
        pii.parenttype,
        pi.customer_name,
        pii.item_code,
        pii.item_name,
        SUM(pii.qty) AS total_qty,
        ROUND((SUM(pii.amount) / SUM(pii.qty)), 2) AS effective_unit_price,
        SUM(pii.amount) AS net_total_value,
        SUM(CASE WHEN pii.qty > 0 THEN pii.amount ELSE 0 END) AS total_additions,
        SUM(CASE WHEN pii.qty < 0 THEN pii.amount ELSE 0 END) AS total_reductions,
        SUM(pii.amount) AS total_gross_total_value,
        pii.uom,
        pii.warehouse,
        pi.discount_amount,
        SUM(pii.cgst_amount + pii.sgst_amount + pii.igst_amount) AS total_gst
    FROM 
        `tabSales Invoice` pi
    JOIN 
        `tabSales Invoice Item` pii ON pi.name = pii.parent
    GROUP BY 
        pi.customer_name, pii.item_code, pii.item_name
    """
    sales_orders_with_customers = frappe.db.sql(sql_query, as_dict=True)

    for sales in sales_orders_with_customers:
        Warehouse_sales = frappe.get_doc('Warehouse', sales['warehouse'])
        sales['warehouse_id_out'] = Warehouse_sales.warehouse_name
        sales['location_name_out'] = Warehouse_sales.custom_location

    return sales_orders_with_customers

def find_customer_data(item_code, sales_orders):
    for order in sales_orders:
        if order['item_code'] == item_code:
            return order
    return {}

def get_invoice_with_items_purchse():
    sql_query = """SELECT 
        pi.supplier AS supplier_name,
        pii.parenttype,
        pii.item_code,
        pii.item_name,
        SUM(pii.qty) AS total_qty,
        ROUND((SUM(pii.amount) / SUM(pii.qty)), 2) AS effective_unit_price,
        SUM(pii.amount) AS net_total_value,
        SUM(CASE WHEN pii.qty < 0 THEN pii.amount ELSE 0 END) AS total_reductions,
        SUM(pii.amount) AS total_gross_total_value,
        pii.uom,
        pii.warehouse,
        pi.discount_amount,
        SUM(pii.cgst_amount + pii.sgst_amount + pii.igst_amount) AS total_gst
    FROM 
        `tabPurchase Receipt` pi
    JOIN 
        `tabPurchase Receipt Item` pii ON pi.name = pii.parent
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
        else:
            d['barcode'] = ''

    for w in invoices_with_items:
        Warehouse = frappe.get_doc('Warehouse', w['warehouse'])
        w['warehouse_id_in'] = Warehouse.warehouse_name
        w['location_name_in'] = Warehouse.custom_location
    
    return invoices_with_items



def get_invoice_with_items_return_not():
    sql_query = """SELECT 
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
        pii.warehouse,
        pi.discount_amount,
        SUM(pii.cgst_amount + pii.sgst_amount + pii.igst_amount) AS total_gst
    FROM 
        `tabPurchase Invoice` pi
    JOIN 
        `tabPurchase Invoice Item` pii ON pi.name = pii.parent
    WHERE
    pi.update_stock = 1 AND pi.is_return = 1
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
        else:
            d['barcode'] = ''

    for w in invoices_with_items:
        Warehouse = frappe.get_doc('Warehouse', w['warehouse'])
        w['warehouse_id_in'] = Warehouse.warehouse_name
        w['location_name_in'] = Warehouse.custom_location
    
    return invoices_with_items









def get_sales_order_with_customer_return_not():
    sql_query = """
    SELECT 
        pii.parenttype,
        pi.customer_name,
        pii.item_code,
        pii.item_name,
        SUM(pii.qty) AS total_qty,
        ROUND((SUM(pii.amount) / SUM(pii.qty)), 2) AS effective_unit_price,
        SUM(pii.amount) AS net_total_value,
        SUM(CASE WHEN pii.qty > 0 THEN pii.amount ELSE 0 END) AS total_additions,
        SUM(CASE WHEN pii.qty < 0 THEN pii.amount ELSE 0 END) AS total_reductions,
        SUM(pii.amount) AS total_gross_total_value,
        pii.uom,
        pii.warehouse,
        pi.discount_amount,
        SUM(pii.cgst_amount + pii.sgst_amount + pii.igst_amount) AS total_gst
    FROM 
        `tabSales Invoice` pi
    JOIN 
        `tabSales Invoice Item` pii ON pi.name = pii.parent
    WHERE
    pi.is_return = 1
    
    GROUP BY 
        pi.customer_name, pii.item_code, pii.item_name
    
    """
    sales_orders_with_customers = frappe.db.sql(sql_query, as_dict=True)

    for sales in sales_orders_with_customers:
        Warehouse_sales = frappe.get_doc('Warehouse', sales['warehouse'])
        sales['warehouse_id_out'] = Warehouse_sales.warehouse_name
        sales['location_name_out'] = Warehouse_sales.custom_location

    return sales_orders_with_customers

def find_customer_data(item_code, sales_orders):
    for order in sales_orders:
        if order['item_code'] == item_code:
            return order
    return {}