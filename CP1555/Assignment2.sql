use world;

-- Question #1
select * from city;

-- Question #2
select distinct language from countrylanguage order by language;

-- Question #3
select name, region from country order by name;

-- Question #4
select name from city where countrycode = "CAN" order by name;

-- Question #5
select name from country where population > 100000000 order by name;

-- Question #6
select name from country where continent = "Asia" or continent = "Europe" or continent = "Africa" order by name;

-- Question #7
select language from countrylanguage where countrycode = "FRA" order by language;

-- Question #8
select name from city where id = (select capital from country where code = "USA");
