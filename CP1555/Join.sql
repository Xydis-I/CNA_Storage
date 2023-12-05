-- select invoice_number, vendor_name from vendors inner join invoices on vendors.vendor_id = invoices.vendor_id order by invoice_number;

-- Exercise 1
-- select * from vendors join invoices on vendors.vendor_id = invoices.vendor_id;

-- Exercise 2
select vendor_name, invoice_number, invoice_date, (invoice_total - (payment_total + credit_total)) as balance_due
	from vendors v
	join invoices i
    on v.vendor_id = i.vendor_id
    where (invoice_total - (payment_total + credit_total)) != 0;
