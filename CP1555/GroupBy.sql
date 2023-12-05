use ap;

select vendor_id, round(avg(invoice_total), 2) as average_invoice_amount
	from invoices
    group by vendor_id
    having avg(invoice_total) > 2000
    order by average_invoice_amount desc;
    
    
select round(avg(invoice_total), 2) as average_invoice_amount from invoices;

select vendor_name, vendor_state,
		round(avg(invoice_total), 2) as average_invoice_amount
	from vendors join invoices on vendors.vendor_id = invoices.vendor_id
    group by vendor_name
    having avg(invoice_total) > 2000
    order by average_invoice_amount desc;
    
    
-- Summary Queries
select vendor_id, count(*) as invoice_qty
	from invoices
    group by vendor_id;
    
select vendor_state, vendor_city, count(*) as invoice_qty,
		round(avg(invoice_total), 2) as invoice_avg
	from invoices join vendors on invoices.vendor_id = vendors.vendor_id
    group by vendor_state, vendor_city
    having count(*) > 2
    -- order by vendor_state, vendor_city;
    order by invoice_qty desc;
