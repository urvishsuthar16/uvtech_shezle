frappe.query_reports["Custom Stock Ledger"] = {
	"filters": [
		{
			// Filter for selecting an item
			fieldname: 'item', // Field name in the query report
			label: __('Item'), // Label displayed to the user
			fieldtype: 'Link', // Type of field (Link for selecting a document)
			options: 'Item', // Options to be populated in the field (from the 'Item' doctype)
		},
	]
};

