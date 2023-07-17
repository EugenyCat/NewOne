SET search_path TO public;


--Write a SQL query that displays all information about movies 
--with a special attribute "Behind the Scenes".

explain analyze --72.50
select film_id, title, special_features
from film 
where special_features::text like '%Behind the Scenes%' 



--Write 2 more movie search options with the "Behind the Scenes" attribute, 
--using other functions or SQL language operators to find values in an array.

--1:
explain analyze --67.50
select film_id, title, special_features
from film 
where special_features && array['Behind the Scenes']

--2:
explain analyze --250.04
select title, array_agg(unnest)
from (
	select title, unnest(special_features), film_id
	from film) t
where unnest = 'Behind the Scenes'
group by film_id, title

--3:
explain analyze --77.50
select film_id, title, special_features
from film 
where 'Behind the Scenes' = any (special_features)

--4:
explain analyze --67.50
select film_id, title, special_features
from film 
where array_position (special_features ,'Behind the Scenes') is not null 




--For each buyer count how much he rented movies 
--with a special attribute "Behind the Scenes. Use CTE

explain analyze --775.71
with  cte_table as (
	select film_id, title, special_features
	from film 
	where special_features::text ilike '%Behind the Scenes%')	
select c.customer_id, count(cte_table.film_id) as "Film count"
from customer c
left join rental r on c.customer_id = r.customer_id
left join inventory i on r.inventory_id = i.inventory_id
left join cte_table on cte_table.film_id = i.film_id 
group by c.customer_id
order by c.customer_id 



--For each buyer count how much he rented movies 
--with a special attribute "Behind the Scenes. Use Subquery

explain analyze --158.85
select r.customer_id, count (t.film_id)
from (
	select film_id, title, special_features
	from film 
	where special_features::text ilike '%Behind the Scenes%') t
left join inventory i on t.film_id = i.film_id
left join rental r on i.inventory_id = r.inventory_id
group by r.customer_id
order by r.customer_id



--Create a materialized view with a query from the previous job 
--and write a query to update the materialized view

create materialized view task_5 as
select r.customer_id, count (t.film_id)
from (
	select film_id, title, special_features
	from film 
	where special_features::text ilike '%Behind the Scenes%') t
left join inventory i on t.film_id = i.film_id
left join rental r on i.inventory_id = r.inventory_id
group by r.customer_id
order by r.customer_id

REFRESH MATERIALIZED view task_5 

explain analyze --10
select * from task_5 t 




--Use window function to print out for each employee information about 
--the very first sale of this employee.

select distinct p2.staff_id ,
	first_value (p2.payment_id) over (partition by p2.staff_id order by payment_date)
	from payment p2 
	left join rental r on p2.rental_id = r.rental_id 
	left join inventory i on r.inventory_id =i.inventory_id 
	left join film f on f.film_id =i.film_id 
	group  by p2.staff_id ,p2.payment_id, payment_date



--For each store, identify and print the following analytics with a single SQL query:
--1. the day on which the most rented films (day in year-month-day format)
--2. number of films rented on that day
--3. The day on which the films were sold for the lowest amount (day in year-month-day format)
--4. the amount of sale on that day

	select  distinct s.store_id as "ID_магазина" ,
	first_value (p.payment_date::date) over (partition by s.store_id order by count(p.payment_id) desc) as "Date, max_count films",
	first_value (count (p.rental_id)) over (partition by s.store_id order by count(p.rental_id) desc) as "Count films max" ,
	first_value (p.payment_date::date) over (partition  by s.store_id order by  sum(amount) ) as "Date, min_count films" ,
	first_value (sum(p.amount)) over (partition by s.store_id order by sum(p.amount) ) as "Count films min"
from payment p 
left join customer c on c.customer_id=p.customer_id 
left join store s on c.store_id =s.store_id 
group by s.store_id, p.payment_date::date 
