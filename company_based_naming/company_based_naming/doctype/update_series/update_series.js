// Copyright (c) 2020, First ERP and contributors
// For license information, please see license.txt

frappe.ui.form.on('Update Series', {
	refresh: function(frm) {
		frappe.call({
			method: "get_series",
			doc: frm.doc,
			callback: function(r) {
				console.log(r.message)
				frm.set_df_property("series", "options", r.message);
			}
		});
	},
	series:function(frm){
		frappe.call({
			method: "company_based_naming.company_based_naming.doctype.update_series.update_series.get_current",
			args:{
				"series":frm.doc.series
			},
			callback: function(r) {
				console.log(r.message)
				frm.set_value('current',r.message)
				// frm.set_df_property("series", "options", r.message);
			}
		})
	},
	update:function(frm){
		frappe.call({
			method: "company_based_naming.company_based_naming.doctype.update_series.update_series.update_series",
			args:{
				"series":frm.doc.series,
				"current":frm.doc.current
			},
			callback: function(r) {
				console.log(r.message)
				// frm.set_value('current',r.message)
				// frm.set_df_property("series", "options", r.message);
			}
		})
	}
});
