--Set SCHEMA
SET search_path TO countries_peoples;


/*
Design the database for the following entities:
Language (English, French, etc.);
People (Slavs, Anglo-Saxons, etc.);
countries (Russia, Germany, etc.).
The rules are as follows:
Several nationalities may speak the same language;
One nation may live in several countries;
Several nationalities may live in each country.
This should result in 5 tables: 3 reference tables and 2 connected tables (example table with links - film_actor).
Requirements for reference tables:
The entity identifier should be assigned by auto increment;
entity names should not contain null-values, no duplicate entity names should be allowed.
*/


CREATE DATABASE countries_peoples;
CREATE SCHEMA countries_peoples;


create table languages (
id_language	serial primary key,
language 	varchar(50) not null UNIQUE
);

insert into languages (language)
values ('English'), ('French'), ('Spanish'), ('Chinese')
;


create table peoples (
id_people	serial primary key,
people 		varchar(50) not null UNIQUE
);

insert into peoples (people)
values ('Englishman'), ('Frenchman'), ('Hispanic'), ('Chinese')
;


create table countries (
id_country	serial primary key,
country 	varchar(50) not null UNIQUE
);

insert into countries (country)
values ('England'), ('France'), ('Spain'), ('China')
;


create table countries_peoples (
primary key(id_country, id_people),
id_country 		INTEGER not null REFERENCES countries (id_country),
id_people 		INTEGER not null REFERENCES peoples (id_people) 
);

insert into countries_peoples (id_country, id_people)
values (1, 1), (2, 2), (3, 3), (4, 4), (2, 1)
;


create table peoples_languages (
primary key(id_people, id_language),
id_people 		INTEGER not null REFERENCES peoples (id_people),
id_language 	INTEGER not null REFERENCES languages (id_language) 
);

insert into peoples_languages (id_people, id_language)
values (1, 1), (2, 2), (3, 3), (4, 4), (2, 1)
;


-----------------------------------------------------------------------------------
--PART 2

SET search_path TO public;


--create table film_new
create table film_new(
if_film_new serial primary key, 
film_name varchar(255) not null,
film_year integer check (film_year > 0),
film_rental_rate numeric(4, 2) default 0.99,
film_duration integer not null check(film_duration > 0)
);


--insert data into film_new
insert into film_new (film_name, film_year, film_rental_rate, film_duration)
values 
('The Shawshank Redemption'	, 1994, 2.99, 142), 
('The Green Mile'			, 1999, 0.99, 189),
('Back to the Future'		, 1985, 1.99, 116),
('Forrest Gump'				, 1994, 2.99, 142),
('Schindler’s List'			, 1993, 3.99, 195)
;


--Update film_rental_rate = film_rental_rate+1.41
update film_new
SET  film_rental_rate = film_rental_rate + 1.41
;


--Delete 'Back to the Future'
delete from film_new
where film_name = 'Back to the Future'
;


--Add data about new film 
insert into film_new (film_name, film_year, film_rental_rate, film_duration)
values 
('Titanic'	, 1997, 4.99, 194)
;


--Add new column duration in hours
alter table film_new
ADD column duration_in_hours numeric(4, 2)
;

update film_new SET duration_in_hours=film_duration/60.0
;

ALTER TABLE film_new
ALTER COLUMN duration_in_hours SET NOT null
;

--Drop table film_new
drop table film_new
;
