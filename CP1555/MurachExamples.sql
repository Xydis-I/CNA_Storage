-- Murach Examples #10
/*
select invoice_due_date as "Due Date",
	   invoice_total as "Total",
       invoice_total * 0.10 as "10%",
       invoice_total * 1.10 as "Total+10%"
from invoices
where invoice_total >= 500 and 1000 >= invoice_total
order by invoice_due_date desc;
*/

-- Murach Examples #11
/*
select invoice_number,
	   invoice_total,
       payment_total + credit_total as payment_credit_total,
       invoice_total - (payment_total + credit_total) as balance_due
from invoices
where invoice_total - (payment_total + credit_total) > 50
order by balance_due desc
limit 5;
*/

-- Murach Examples #11.5
/*
select invoice_number,
	   invoice_total,
       payment_total + credit_total as payment_credit_total,
       invoice_total - (payment_total + credit_total) as balance_due,
       date_format(invoice_due_date, '%m/%d/%Y') as 'MM/DD/YYYY'
from invoices
where invoice_total - (payment_total + credit_total) > 50
order by balance_due desc
limit 5;
*/

-- Murach Example: Distinct (122 rows becomes 53 rows)
select distinct vendor_city, vendor_state
from vendors
