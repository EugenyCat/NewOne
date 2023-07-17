SET search_path TO public;



--window functions
select customer_id, payment_id, amount,	payment_date,
row_number() over(partition by payment_date::date order by payment_date::date) as "No of payment by date",
row_number() over(partition by customer_id order by payment_date::date) as "No of payment by customer_id",
sum(amount) over(partition by customer_id order by payment_date::date, amount) as "Sum by customer",
dense_rank() over(partition by customer_id order by amount) as "Rank of amount by customer"
from public.payment p 
--order by customer_id, payment_date::date
;



--current and previous amount by customer
select customer_id, amount,
lag(amount, 1, 0.0) over(partition by customer_id) as "Prev amount"
from public.payment p 
;


--Diff between cur and next amount
select customer_id, amount, lead(amount, 1, 0.0) over(partition by customer_id) as "next payment",
lead(amount, 1, 0.0) over(partition by customer_id) - amount as "Diff between cur and next amount"
from public.payment p 
;


--Last payment of customers
select customer_id, amount , payment_date
from ( 
		select  customer_id, amount, payment_date,
				max(payment_date) over(partition by customer_id) as "last_date"
		from public.payment p
	) t
where payment_date = "last_date"
;


--partition by customer and date
select p.staff_id, p.payment_date, amount,
sum(p.amount) over(partition by p.staff_id, p.payment_date::date order by p.payment_date) 
from payment p 
where p.payment_date::date between '2007-02-14' and '2007-02-15'
;


--On 2007-04-30 customers wnom have 40 and more payments have a disount. Find those customers.
select t.customer_id, t.payment_date, t."No of payment"
from (
		select p.customer_id, p.payment_id, p.payment_date,
		row_number() over(partition by customer_id order by customer_id) as "No of payment"
		from public.payment p 
	) t 
where t."No of payment" > 40 and t.payment_date::date = '2007-04-30'
;



--Best customers by country
select distinct c3.country, 
first_value(p.customer_id) over(partition by c3.country order by count(p.payment_id) desc) as "Customer with max count orders",
first_value(p.customer_id) over(partition by c3.country order by sum(p.amount) desc) as "Customer with max sum orders",
first_value(p.customer_id) over(partition by c3.country order by max(p.payment_date) desc) as "Customer with last orders"
from payment p 
left join customer c on c.customer_id = p.customer_id 
left join store s on s.store_id = c.store_id 
left join address a on a.address_id = s.address_id 
left join city c2 on c2.city_id = a.city_id 
left join country c3 on c3.country_id = c2.country_id
group by p.customer_id, c3.country
;



