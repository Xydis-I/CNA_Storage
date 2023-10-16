use ap;
-- "Dash-Dash-Space" is for making comments fyi, so is '/* [...] */
-- select * from invoices;
-- select invoice_id,vendor_id,invoice_total,payment_date from invoices where invoice_total>1000 order by payment_date
-- select invoice_id,vendor_id,invoice_total,payment_date from invoices where payment_date is null order by payment_date
-- select invoice_number,invoice_date,invoice_total from invoices order by invoice_total DESC;
-- select invoice_id,invoice_total,credit_total + payment_total from invoices;
-- select invoice_id,invoice_total,credit_total + payment_total as total_credits from invoices;
-- select invoice_id as Id,invoice_total as Total,credit_total + payment_total as total_credits from invoices;
/*
select invoice_number,invoice_date,invoice_total
from invoices
where invoice_date between '2014-06-01' and '2014-06-30'
order by invoice_date asc;
*/

-- select vendor_id,concat(first_name, ' ', last_name) as full_name from vendor_contacts
-- select vendor_id as "Vendor Id",concat(first_name, ' ', last_name) as "Full Name" from vendor_contacts
select concat(first_name, '''s last name is ', last_name) as "Full Name" from vendor_contacts
