# Copyright (c) 2025, sameer and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CalculationEntry(Document):
    """
    Doctype to store our calcualtion entry data

    """

    def before_insert(self):
        """
        Increament counter on every entry for a customer
        """
        count = frappe.db.count("Calculation Entry", filters={"customer": self.customer})
        self.counter = count + 1
