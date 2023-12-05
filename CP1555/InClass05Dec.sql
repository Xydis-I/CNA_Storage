use ap;

-- Question 1
select terms.terms_id, terms_description, count(*) as invoice_qty
	from terms
    join invoices
    on terms.terms_id = invoices.terms_id 
    group by terms.terms_id
    order by invoice_qty desc
    limit 1;
    
-- Question 2
select monthname(payment_date), count(monthname(payment_date)) as payments
	from invoices
    where monthname(payment_date) is not null
	group by monthname(payment_date);
    
-- Question 3
select account_description, count(*), sum(line_item_amount) as total
	from general_ledger_accounts
	join invoice_line_items
	on general_ledger_accounts.account_number = invoice_line_items.account_number
	group by general_ledger_accounts.account_number
	having total > 10000
    order by total desc;
    