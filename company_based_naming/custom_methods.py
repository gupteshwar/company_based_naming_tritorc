import frappe

# def custom_autoname(doc,method):
#     frappe.msgprint(doc.company)
#     from frappe.model.naming import make_autoname
#     series = frappe.get_list("Naming Setting Detail",filters={"parent":doc.company,"doctypes":doc.doctype,"enable":1,"enable_multiple_series":0},fields={'naming_series_'})
#     if series:
#         doc.name = make_autoname(series[0]['naming_series_'])
#     else:
#         pass

# method to check if naming for the company is set in naming setting
@frappe.whitelist()
def get_series_1(company,doctype):
    return frappe.db.get_all("Naming Setting Detail",filters={"parent":company,"doctypes":doctype,"enable":1},fields={'naming_series_',"enable_multiple_series"})