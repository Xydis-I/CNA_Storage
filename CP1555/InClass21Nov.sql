use ap;

/* Question 4 */
insert into invoices
	values (null, 32, "AX-014-027", '2018-08-01', 434.58, 0, 0, 2, '2018-08-31', null);
    
/* Question 5 */
insert into invoice_line_items values
	((select invoice_id from invoices where invoice_number = "AX-014-027"), 1, 160, 180.23, "Hard drive");
insert into invoice_line_items values
	((select invoice_id from invoices where invoice_number = "AX-014-027"), 2, 527, 254.35, "Exchange Server update");
    
/* Question 6 */
update invoices set credit_total = invoice_total*0.10, payment_total = (invoice_total - (invoice_total*0.10))
	where invoice_number = "AX-014-027";
    
/* Question 7 */
update vendors set default_account_number = 403 where vendor_id = 44;

/* Question 8 */
update invoices set terms_id = 2
	where vendor_id in (select vendor_id from vendors where default_terms_id = 2);
    
/* Question 9 */
delete from invoice_line_items
	where invoice_id = (select invoice_id from invoices where invoice_number = "AX-014-027");
delete from invoices where invoice_number = "AX-014-027";
