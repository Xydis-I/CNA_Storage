/* Assignment 4 */
use ap;

/* Question 1 */
select invoice_total, 
	   format(invoice_total, 1),
       convert(invoice_total, signed),
       cast(invoice_total as signed) from invoices;
       
/* Question 2 */
select invoice_date,
	   cast(invoice_date as datetime),
       cast(invoice_date as char(7)) from invoices;
       
/* Question 3 */
create table weekdays(id_num int not null auto_increment,
					  lastname varchar(255) not null,
                      firstname varchar(255) not null,
                      workday enum("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday") not null,
                      primary key (id_num));
				
insert into weekdays values (null, "Barrett", "Christian", "Tuesday");
insert into weekdays values (null, "Barrett", "Riley", "Friday");
insert into weekdays values (null, "Jacque", "Sheldon", "Tuesday");
insert into weekdays values (null, "Harris", "Tyson", "Sunday");
insert into weekdays values (null, "King", "Matthew", "Tuesday");
insert into weekdays values (null, "Loveys", "Steven", "Wednesday");

select * from weekdays where workday = "Tuesday";

/* Question 4 */
create table colors(id_num int not null auto_increment,
					color_name varchar(255) not null,
					constituents set("Red", "Yellow", "Blue") not null,
					primary key (id_num));

insert into colors values (null, "Orange", "Red,Yellow");
insert into colors values (null, "Green", "Blue,Yellow");
insert into colors values (null, "Purple", "Blue,Red");

select * from colors where constituents like '%Red%';
