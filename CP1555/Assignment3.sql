use bookstore;

/* Question 1 */
insert into author values (4, "Christian", "Barrett", '1999-10-15');
insert into book values (111999, "Insert Book Here", "science-fiction", '2023-11-20');
insert into book_author values (6, 111999, 4);

/* Question 2 */
insert into book values (111285, "Cooking by Numbers", "cooking", '2023-11-19');
insert into book_author values
	(7,
    (select isbn from book where title = "Cooking by Numbers"),
	(select author_id from author where first_name = "Jill" and last_name = "Jones"));
    
/* Question 3 */
update book set title = "Bicycle Racing 2nd", published = '2023-11-20'
	where isbn = (select isbn from book_author join author
					on book_author.author_id = author.author_id
                    where first_name = "James" and last_name = "Peters");
                    
/* Question 4 */
delete from book_author where isbn = (select isbn from book where title = "Space Adventures");
delete from book where title = "Space Adventures";

/* Question 5 */
insert into book values (978194387, "Murachs MySQL 3rd", "computers", '2019-03-19');
insert into author values (5, "Joel", "Murach", '1968-05-13');
insert into book_author values
	(8,
    (select isbn from book where title = "Murachs MySQL 3rd"),
	(select author_id from author where first_name = "Joel" and last_name = "Murach"));
