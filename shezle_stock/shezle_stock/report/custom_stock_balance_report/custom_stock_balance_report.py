# Copyright (c) 2024, YES and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns = [
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
            'fieldname': 'barcode_no',
            'label': 'Barcode No',
            'fieldtype': 'Data',            
        },
        {
            'fieldname': 'stock_uom',
            'label': 'Stock Unit',
            'fieldtype': 'Data',            
        }
		,
		{
            'fieldname': 'item_group',
            'label': 'Item Group',
            'fieldtype': 'Link',
			'options' : "Item Group"
        }
		,
		{
            'fieldname': 'warehouse_id',
            'label': 'Warehouse ID',
            'fieldtype': 'Data',
        },
		{
            'fieldname': 'warehouse_name',
            'label': 'Warehouse Name',
            'fieldtype': 'Data',
        },
		# {
        #     'fieldID': 'location_name',
        #     'label': 'Location Name',
        #     'fieldtype': 'Data',            
        # },
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
        # {
        #     'fieldname': 'total_qty',
        #     'label': 'Total Qty',
        #     'fieldtype': 'Data',
        # },
        # {
        #     'fieldname': 'total_value',
        #     'label': 'Total Value',
        #     'fieldtype': 'Data',
        # }
		
	]
	# data = get_data()
	data = [
		{

		}
	]
	return columns, data

def get_data():
	# data = []
	# items= frappe.db.get_list("Item", pluck='name')
	# query = """
	# 		SELECT item_group ,item_code,  stock_uom as uom FROM `tabItem`;
	# 		"""

	# data = frappe.db.sql(query, as_dict=True)
	# for row in data:
	# 	warehouse_data = frappe.db.get_value("Stock Ledger Entry", {'item_code' : row['item_code']}, ['warehouse', 'qty_after_transaction', 'incoming_rate'])
	# 	try:
	# 		row['warehouse'] = warehouse_data[0]
	# 		row['qty'] = warehouse_data[1]
	# 		row['effective_unit_rate'] = warehouse_data[2]
	# 		row['value'] = row['qty'] * row['effective_unit_rate']
	# 	except:
	# 		frappe.log_error("Problem item", f"{row['item_code']}\n\n{warehouse_data}")

    item_groups = frappe.db.get_all("Item Group", pluck='name')
    for ig in item_groups:
        item_list = frappe.db.get_list("Item", {'item_group' : ig}, pluck='name')
        if item_list:
            item_list = tuple(item_list)
            
            if len(item_list) == 1:
                item_list = str(item_list).replace(",", "")
            item_list = str(item_list)
            
            query = f"""SELECT item_code,warehouse, stock_uom, qty_after_transaction as qty, incoming_rate as effective_unit_rate, qty_after_transaction*incoming_rate as value FROM `tabStock Ledger Entry`
                        WHERE item_code in {item_list};"""
            
            data = frappe.db.sql(query, as_dict=True)
            qty_total = sum(d.get('qty') for d in data)
            total_sum = sum(d.get('value') for d in data)
            
            for d in data:
                d['item_group'] = ig
                d['total_qty'] = qty_total
                d['total_value'] = total_sum

    return data

def get_data_updated():
	query = """ SELECT item_code as item_code_number, item_name FROM `tabItem`
				WHERE has_variants = 1;
			"""
	item_templates = frappe.db.sql(query, as_dict=True)
	
	for item_template in item_templates:
		# variants = frappe.db.get_list("Item", {"variant_of" : item_template['item_code']}, pluck='name')
		query = f""" SELECT item_code, item_group FROM `tabItem`
					WHERE variant_of = '{item_template}';
		"""
		data = frappe.db.sql(query, as_dict=True)
		