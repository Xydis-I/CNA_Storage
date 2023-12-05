/* 1 Select all items for invoice "I77271-O01" */
select *
	from invoice_line_items ili
    join invoices i
    on ili.invoice_id = i.invoice_id 
    where i.invoice_number = "I77271-O01";

/* 2 Select all invoices for vendor "Wells Fargo Bank". Use inv for invoices and ven for vendors  */
select *
	from invoices inv
    join vendors ven
    on inv.vendor_id = ven.vendor_id
    where vendor_name = "Wells Fargo Bank";

/* 3 how many invoices does the company "Federal Express Corporation" have? use alias v for vendors table and i for invoices table */
select count(*) as "Invoice_Count"
	from invoices i
    join vendors v
    on i.vendor_id = v.vendor_id
    where vendor_name = "Federal Express Corporation";
-- 47

/* 4 list the invoice number, due date and amounts for all the "Federal Express Corporation" invoices */
select invoice_number, invoice_due_date, invoice_total
	from invoices
    join vendors
    on invoices.vendor_id = vendors.vendor_id
    where vendor_name = "Federal Express Corporation";

/* 5 as above, but only the top 3 most expensive invoices. */
select invoice_number, invoice_due_date, invoice_total
	from invoices
    join vendors
    on invoices.vendor_id = vendors.vendor_id
    where vendor_name = "Federal Express Corporation"
    order by invoice_total desc
    limit 3;
    
/* 6 Select all items for invoice "963253230" */
select *
	from invoice_line_items ili
    join invoices i
    on ili.invoice_id = i.invoice_id 
    where i.invoice_number = "963253230";
    
/*7*/

/*8 What's the sum of Federal Expresss Corp. Invoices?*/    
select count(*) as "Invoice_Count", sum(invoice_total) as Sum
	from invoices i
    join vendors v
    on i.vendor_id = v.vendor_id
    where vendor_name = "Federal Express Corporation";