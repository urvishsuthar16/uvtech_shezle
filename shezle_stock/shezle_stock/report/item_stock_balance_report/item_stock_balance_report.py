# Copyright (c) 2024, yes and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data_updated()
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
        }
    ]

def get_data_updated():
    query = """
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
            (SELECT 
                piit.item_code, 
                
                piit.uom, 
                piit.qty, 
                piit.rate
            FROM 
                `tabPurchase Invoice Item` AS piit
            WHERE 
                piit.parent IN (SELECT name FROM `tabPurchase Invoice` WHERE update_stock = 1)) AS pii
        INNER JOIN 
            (SELECT 
                item.item_code, 
                item_barcode.barcode, 
                item.item_group, 
                item.variant_of  
            FROM 
                `tabItem` AS item 
            LEFT JOIN 
                `tabItem Barcode` AS item_barcode ON item.name = item_barcode.parent) AS it
        ON 
            pii.item_code = it.item_code
        GROUP BY 
            it.item_code;
    """
    data = frappe.db.sql(query, as_dict=True)
    
    for entry in data:
        entry['item_name'] = frappe.db.get_value("Item", entry['item_code_number'], 'item_name')
    
    return data
