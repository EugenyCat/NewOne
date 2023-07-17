--Simple queries: select, where, group by, limit, order by and 
--some functions: concat_ws, char_length, ::date, upper, left, split_part

--simple SELECT to table from DB
select * from postgres.public.country c


--Output unique cities, which start the letter 'L'and end the letter 'a'
select distinct city from postgres.public.city c 
where city like 'L%a'

--Output list of payments, 
--where data >= 14.02.2007 <= 15.02.2007 and amount > 1; sort by payment_date
select payment_id, payment_date, amount from postgres.public.payment p 
where payment_date >= '14.02.2007' and payment_date < '16.02.2007' and amount > 1
order by payment_date

--Output information about last 10 payments
select payment_id, payment_date, amount from postgres.public.payment p 
order by payment_date desc 
limit 10


--Output Name of customer, email and lengh of email, date last update without time
select 	concat_ws(' ', c.first_name, c.last_name) as "Customer Name",
		c.email,
		char_length(c.email) as "Email len",
		c.last_update::date as "Last update"
from postgres.public.customer c 
 

--Output active customers , who are named like Kelly or Willie
select concat_ws(' ', c.first_name, c.last_name) as "Customer Name" from postgres.public.customer c 
where c.activebool = true and (lower(c.first_name)  like 'kelly' or lower(c.first_name)  like 'willie')




--Films with raiting R and rent worth [0;3] OR raiting PG-13 and worth [4;]
select f.film_id, f.title , f.description, f.rating, f.rental_rate  from postgres.public.film f 
where 	(f.rating = 'R' and (f.rental_rate >=0 and f.rental_rate <=3))
		or 
		(f.rating = 'PG-13' and f.rental_rate >=4)
order by f.film_id 


--The 3 films with most long description
select f.film_id , f.title , f.description from postgres.public.film f 
order by char_length(f.description) desc
limit 3


--Each customer with separated email (before and after @ + first letter is big)
select 	c.customer_id, 
		c.email,
		concat(upper(left(split_part(c.email, '@', 1), 1)), lower(right(split_part(c.email, '@', 1), char_length(split_part(c.email, '@', 1))-1))) as "Email before @",
		concat(upper(left(split_part(c.email, '@', 2), 1)), lower(right(split_part(c.email, '@', 1), char_length(split_part(c.email, '@', 2))-1))) as "Email after @"
from postgres.public.customer c 
order by c.customer_id

--------------------------------------
--PART2--
--------------------------------------

--For each customer -> address, city, country
SELECT c.customer_id as "ID Customer", 
		concat_ws(' ', c.first_name , c.last_name) as "Customer", 
		a.address as "Customer Address", 
		c2.city as "City", 
		c3.country as "Country" 
FROM postgres.public.customer c 
left join postgres.public.address a on a.address_id = c.address_id 
left join postgres.public.city c2 on c2.city_id = a.city_id 
left join postgres.public.country c3 on c3.country_id = c2.country_id 


--For each store -> count(Customer) where that dim > 300. Additional inf: City, Full name of seller.
select count(distinct c.customer_id) as "Count Customer", c.store_id, c2.city, concat_ws(' ', s2.first_name, s2.last_name) as "Seller" 
from postgres.public.customer c 
left join postgres.public.store s on s.store_id = c.store_id 
left join postgres.public.address a on s.address_id = a.address_id
left join postgres.public.staff s2 on s2.staff_id  = s.manager_staff_id 
left join postgres.public.city c2 on c2.city_id = a.city_id 
group by c.store_id, c2.city, concat_ws(' ', s2.first_name, s2.last_name)
having  count(distinct c.customer_id) > 300

--TOP-5 customer by count of rent films
select concat_ws(' ', c.first_name, c.last_name), count(r.rental_id) as "Count Rent Films"
from postgres.public.customer c 
left join postgres.public.rental r on r.customer_id = c.customer_id 
group by concat_ws(' ', c.first_name, c.last_name)
order by count(r.rental_id) desc
limit 5

--For each customer: Count of films, sum of rent, min and max paymant
select concat_ws(' ', c.first_name, c.last_name), count(r.rental_id) as "Count Rent", sum(p.amount) as "Sum Rent", min(p.amount) as "Min Rent", max(p.amount) as "Max Rent" 
from postgres.public.customer c 
left join postgres.public.rental r on r.customer_id = c.customer_id 
left join postgres.public.payment p on p.customer_id = c.customer_id 
group by concat_ws(' ', c.first_name, c.last_name)
2

--Combination city1-city2 where city1 <> city2
select concat_ws('<->', c.city , c2.city) as "Combination"
from postgres.public.city c 
cross join postgres.public.city c2
where c.city_id <> c2.city_id


--For each customer: avg(DayCountRent)
select c.customer_id as "ID_Customer",
		avg(r.return_date::date - r.rental_date::date) as "Avg Count Day of Return"
from postgres.public.customer c 
left join postgres.public.rental r on r.customer_id = c.customer_id 
group by c.customer_id



--1. For each film: rent count, common sum of rent 
--2. Films was't rented
select f.film_id, f.title, count(p.rental_id) as "Count Rent" , sum(p.amount) as "Sum Rent"  from postgres.public.film f 
left join postgres.public.inventory i on i.film_id = f.film_id 
left join postgres.public.rental r on r.inventory_id = i.inventory_id 
left join postgres.public.payment p on p.rental_id = r.rental_id 
group by f.film_id, f.title
having count(p.rental_id) = 0


--For each seller: sum of sells
select concat_ws(' ', s.first_name, s.last_name) as "Seller", 
		SUM(p.amount) as "Sells" ,
		case 
			when SUM(p.amount) > 31000 then 'Да'
			else 'Нет'
		end as "Bonus"
from postgres.public.payment p 
left join postgres.public.staff s on p.staff_id = s.store_id 
group by concat_ws(' ', s.first_name, s.last_name)

