/*
insert into invoices
	(vendor_id, invoice_number, invoice_total, terms_id, invoice_date, invoice_due_date)
values
	(97, '456789', 8344.50, 1, '2018-08-01', '2018-08-31');
*/
  
/*
insert into invoices values
	(116, 97, '456709', '2018-08-02', 270.50, 0, 0, 1, '2018-09-01', null),
    (117, 97, '456791', '2018-08-03', 4390.00, 0, 0, 1, '2018-09-02', null),
    (118, 97, '456792', '2018-08-03', 565.60, 0, 0, 1, '2018-09-02', null);
*/

/* Create a table called FedEx_invoices that contains all the columns from the invoices table that refer to vendor_id 123 */
create table fedex_invoices as
	select *
    from invoices
    where vendor_id = 123;
    
/* Insert a record into the fedex_invoices table */
insert into fedex_invoices values
	(9876, 123, 'FE86453', '2023-11-14', 45, default, default, 2, '2023-12-14', null);