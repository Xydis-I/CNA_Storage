use ap;

/* Question 1 */
select count(*)
	from invoices
    join vendors
    on invoices.vendor_id = vendors.vendor_id
    where vendors.vendor_name = "Pacific Bell";
    
/* Question 2 */
select invoice_number, invoice_total
	from invoices
    join vendors
    on invoices.vendor_id = vendors.vendor_id
    where vendors.vendor_name = "Pacific Bell";
    
/* Question 3 */
select sum(invoice_total) as "invoices total for Pac Bell"
	from invoices
    join vendors
    on invoices.vendor_id = vendors.vendor_id
    where vendors.vendor_name = "Pacific Bell";
    
/* Question 4 */
select vendor_name, invoice_total - (payment_total + credit_total) as "amount due"
	from invoices
    join vendors
    on invoices.vendor_id = vendors.vendor_id
    where (invoice_total - (payment_total + credit_total)) > 100
    order by (invoice_total - (payment_total + credit_total)) desc
    limit 5;
    
/* Question 4 - Sanity Check*/
select vendor_name, invoice_total, payment_total, credit_total
	from invoices
    join vendors
    on invoices.vendor_id = vendors.vendor_id
    where vendor_name = "IBM"
    order by (invoice_total - (payment_total + credit_total)) desc;
    
/* Question 5 */
select line_item_description as Description, line_item_amount as Amount
	from invoice_line_items li
    join invoices inv
    on li.invoice_id = inv.invoice_id
    where inv.invoice_number = "I77271-O01"
    order by li.invoice_sequence asc;
