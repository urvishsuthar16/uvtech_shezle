# Copyright (c) 2024, yes and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns = [
		{
            'fieldname': 'date',
            'label': 'Date',
            'fieldtype': 'Date',
        },
		{
            'fieldname': 'voucher_type_in',
            'label': 'IN Voucher Type',
			'fieldtype': 'Data',
        },
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
			'options' : "Item Group"
        },
		{
            'fieldname': 'client_id',
            'label': 'Client ID',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'supplier_name',
            'label': 'Suuplier Name',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'customer_name',
            'label': 'Customer Name',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'in_qty',
            'label': 'In Qty',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'unit_price',
            'label': 'Unit Price',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'net_total_value',
            'label': 'Net Total Value',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'taxes',
            'label': 'Taxes',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'additions',
            'label': 'Additions',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'reductions',
            'label': 'Reductions',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'gross_total_value',
            'label': 'Gross Total Value',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'warehouse_id_in',
            'label': 'Warehouse ID',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'warehouse_name_in',
            'label': 'Warehouse Name',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'location_name_in',
            'label': 'Location Name',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'location_id_in',
            'label': 'Location ID',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'packaging_type_in',
            'label': 'Packaging Type',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'packaging_qty_in',
            'label': 'Packaging Quantity',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },		
		{
            'fieldname': 'voucher_type_out',
            'label': 'Out Voucher Type',
			'fieldtype': 'Data',
        },
		{
            'fieldname': 'out_qty',
            'label': 'IN Voucher Type',
			'fieldtype': 'Data',
        },
		{
            'fieldname': 'unit_price',
            'label': 'Unit Price',
			'fieldtype': 'Data',
        },
		{
            'fieldname': 'net_total_value',
            'label': 'Net Total Value',
			'fieldtype': 'Data',
        },
		{
            'fieldname': 'taxes',
            'label': 'Taxes',
			'fieldtype': 'Data',
        },
		{
            'fieldname': 'additions',
            'label': 'Additions',
			'fieldtype': 'Data',
        },
		{
            'fieldname': 'reductions',
            'label': 'Reductions',
			'fieldtype': 'Data',
        },
		{
            'fieldname': 'gross_total_value',
            'label': 'Gross Total Value',
			'fieldtype': 'Data',
        },
		{
            'fieldname': 'out_qty',
            'label': 'IN Voucher Type',
			'fieldtype': 'Data',
        },
		{
            'fieldname': 'warehouse_id_out',
            'label': 'Warehouse ID',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'warehouse_name_out',
            'label': 'Warehouse Name',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'location_name_out',
            'label': 'Location Name',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'location_id_out',
            'label': 'Location ID',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'packaging_type_in',
            'label': 'Packaging Type',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },
		{
            'fieldname': 'packaging_qty_in',
            'label': 'Packaging Quantity',
            'fieldtype': 'Data',
			# 'options' : "Item Group"
        },	
	]
	data = []
	data = get_data()
	return columns, data

def get_data():	
       
    query = """ 
        SELECT pii.item_code, it.barcode as barcode ,it.item_group, it.variant_of as item_code_number,pii.warehouse as warehouse_name, 
        pii.warehouse_location as location_name, pii.uom as stock_uom, SUM(pii.qty) as qty,
        ROUND(SUM(pii.qty*pii.rate)/SUM(pii.qty),2) as effective_unit_rate , SUM(pii.qty) * ROUND(SUM(pii.qty*pii.rate)/SUM(pii.qty),2) as value FROM 
    
            (SELECT piit.item_code, piit.warehouse, piit.uom, piit.qty, piit.rate, warehouse.custom_location as warehouse_location
                FROM `tabPurchase Invoice Item` as piit LEFT JOIN `tabWarehouse` as warehouse 
                ON piit.warehouse = warehouse.name ) AS pii INNER JOIN 

            (SELECT item.item_code, item_barcode.barcode, item.item_group, item.variant_of  FROM 
                `tabItem` as item LEFT JOIN `tabItem Barcode` as item_barcode
                ON item.name = item_barcode.parent
                ) AS it
    
        ON pii.item_code = it.item_code

        GROUP BY it.item_code;
    """
    data = frappe.db.sql(query, as_dict=True)
    
    for d in data:
        d['item_name'] = frappe.db.get_value("Item", d['item_code_number'], 'item_name')

    # data.sort(key=lambda k : k['item_code_number'])
    return data
