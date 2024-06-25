import frappe

def execute(filters=None):
    if not filters:
        filters = {}
    item_name = filters.get('item')
    periodicity = filters.get('periodicity')

    columns = get_columns()
    data = get_data_updated(item_name, periodicity)
    return columns, data

def get_columns():
    return [
        {
            'fieldname': 'item_code_number',
            'label': 'Item Code Number',
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'item_name',
            'label': 'Item Name',
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'item_code',
            'label': 'Item Code Name (One of multiple)',
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'barcode',
            'label': 'Barcode No',
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'stock_uom',
            'label': 'Stock Unit',
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'item_group',
            'label': 'Item Group',
            'fieldtype': 'Link',
            'options': "Item Group"
        },
        {
            'fieldname': 'warehouse_name',
            'label': 'Warehouse Name',
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'location_name',
            'label': 'Location Name',
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'qty',
            'label': 'Qty',
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'effective_unit_rate',
            'label': 'Effective Unit Rate',
            'fieldtype': 'Data',
        },
        {
            'fieldname': 'value',
            'label': 'Value',
            'fieldtype': 'Data',
        },
    ]

def get_data_updated(item_name, periodicity):
    conditions = ""
    start_date = None

    if periodicity:
        today = frappe.utils.nowdate()
        if periodicity == 'Monthly':
            start_date = frappe.utils.add_months(today, -1)
        elif periodicity == 'Quarterly':
            start_date = frappe.utils.add_months(today, -3)
        elif periodicity == 'Half-Yearly':
            start_date = frappe.utils.add_months(today, -6)
        elif periodicity == 'Yearly':
            start_date = frappe.utils.add_years(today, -1)

    if start_date:
        conditions += f" AND pi.posting_date >= '{start_date}'"

    if item_name:
        conditions += f" AND pii.item_code = '{item_name}'"

    query = f"""
        SELECT 
            pii.item_code, 
            it.barcode AS barcode,
            it.item_group, 
            it.variant_of AS item_code_number,
            pii.uom AS stock_uom, 
            SUM(pii.qty) AS qty,
            ROUND(SUM(pii.qty * pii.rate) / SUM(pii.qty), 2) AS effective_unit_rate, 
            SUM(pii.qty) * ROUND(SUM(pii.qty * pii.rate) / SUM(pii.qty), 2) AS value
        FROM 
            `tabPurchase Invoice Item` pii
        INNER JOIN 
            `tabPurchase Invoice` pi ON pi.name = pii.parent AND pi.update_stock = 1
        LEFT JOIN 
            (SELECT 
                item.item_code, 
                item_barcode.barcode, 
                item.item_group, 
                item.variant_of  
            FROM 
                `tabItem` item 
            LEFT JOIN 
                `tabItem Barcode` item_barcode ON item.name = item_barcode.parent) it
        ON 
            pii.item_code = it.item_code
        WHERE 
            1=1 {conditions}
        GROUP BY 
            it.item_code
    """

    data = frappe.db.sql(query, as_dict=True)
    
    for entry in data:
        entry['item_name'] = frappe.db.get_value("Item", entry['item_code_number'], 'item_name')
    
    return data
