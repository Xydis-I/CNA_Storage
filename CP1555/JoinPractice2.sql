use sakila;

/* show the full address of each store location */
select address,city,district,country
	from ((store
	join address 
    on store.address_id = address.address_id)
    join city
    on city.city_id = address.city_id)
    join country
    on country.country_id = city.country_id;
    
/* show the first and last name of all customers at store #1, sorted by last name in alphabetical order*/
select first_name as "First Name",last_name as "Last Name"
	from customer 
    join store 
    on customer.store_id = store.store_id 
    where store.store_id = 1
    order by last_name asc;

/* show the first and last name of all customers at store #1 whose last name starts with "a", sorted by first name in alphabetical order*/
select first_name as "First Name",last_name as "Last Name"
	from customer 
    join store 
    on customer.store_id = store.store_id 
    where store.store_id = 1 and customer.last_name regexp '^a'
    order by last_name asc;
    
/* deliver all the title, length, and rental_rate greater then $2.99 of sci fi films. order by length longest first*/
select title,length,rental_rate
	from (film 
		join film_category 
		on film.film_id = film_category.film_id) 
	join category 
    on film_category.category_id = category.category_id 
    where category.category_id = 14 and film.rental_rate >= 2.99
    order by length desc;

