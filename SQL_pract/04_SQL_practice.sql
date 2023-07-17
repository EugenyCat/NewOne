--=============== МОДУЛЬ 6. POSTGRESQL =======================================
--= ПОМНИТЕ, ЧТО НЕОБХОДИМО УСТАНОВИТЬ ВЕРНОЕ СОЕДИНЕНИЕ И ВЫБРАТЬ СХЕМУ PUBLIC===========
SET search_path TO public;

--======== ОСНОВНАЯ ЧАСТЬ ==============

--ЗАДАНИЕ №1
--Напишите SQL-запрос, который выводит всю информацию о фильмах 
--со специальным атрибутом "Behind the Scenes".

explain analyze --72.50
select film_id, title, special_features
from film 
where special_features::text like '%Behind the Scenes%' 
and film_id = 1


--ЗАДАНИЕ №2
--Напишите еще 2 варианта поиска фильмов с атрибутом "Behind the Scenes",
--используя другие функции или операторы языка SQL для поиска значения в массиве.

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
	from film
	) t
where unnest = 'Behind the Scenes' and film_id = 1
group by film_id, title

--3:
explain analyze --77.50
select film_id, title, special_features
from film 
where 'Behind the Scenes' = any (special_features)


--3
with my_cte as (
	select film_id, title, special_features
	from film f
	where special_features::text like '%Behind the Scenes%' 
)
select r.customer_id , count(mc.film_id)
from rental r
left join inventory i on i.inventory_id = r.inventory_id 
right join my_cte mc on mc.film_id  = i.film_id 
group by r.customer_id


--4:
explain analyze --67.50
select film_id, title, special_features
from film 
where array_position (special_features ,'Behind the Scenes') is not null 


--ЗАДАНИЕ №3
--Для каждого покупателя посчитайте сколько он брал в аренду фильмов 
--со специальным атрибутом "Behind the Scenes.

--Обязательное условие для выполнения задания: используйте запрос из задания 1, 
--помещенный в CTE. CTE необходимо использовать для решения задания.

explain analyze --775.71
with  cte_table as (
	select film_id, title, special_features
	from film 
	where special_features::text ilike '%Behind the Scenes%')
	
select c.customer_id, count(cte_table.film_id) as "Количество фильмов"
from customer c
left join rental r on c.customer_id = r.customer_id
left join inventory i on r.inventory_id = i.inventory_id
left join cte_table on cte_table.film_id = i.film_id 
group by c.customer_id
order by c.customer_id 


--ЗАДАНИЕ №4
--Для каждого покупателя посчитайте сколько он брал в аренду фильмов
-- со специальным атрибутом "Behind the Scenes".

--Обязательное условие для выполнения задания: используйте запрос из задания 1,
--помещенный в подзапрос, который необходимо использовать для решения задания.

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

--ЗАДАНИЕ №5
--Создайте материализованное представление с запросом из предыдущего задания
--и напишите запрос для обновления материализованного представления

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

--ЗАДАНИЕ №6
--С помощью explain analyze проведите анализ скорости выполнения запросов
-- из предыдущих заданий и ответьте на вопросы:

--1. Каким оператором или функцией языка SQL, используемых при выполнении домашнего задания, 
--   поиск значения в массиве происходит быстрее
--2. какой вариант вычислений работает быстрее: 
--   с использованием CTE или с использованием подзапроса


--======== ДОПОЛНИТЕЛЬНАЯ ЧАСТЬ ==============

--ЗАДАНИЕ №1
--Откройте по ссылке SQL-запрос. (sql-hw5.sql)

--Сделайте explain analyze этого запроса.
--Основываясь на описании запроса, найдите узкие места и опишите их.
--Сравните с вашим запросом из основной части (если ваш запрос изначально укладывается в 15мс — отлично!).
--Сделайте построчное описание explain analyze на русском языке оптимизированного запроса.
-- Описание строк в explain можно посмотреть по ссылке (https://use-the-index-luke.com/sql/explain-plan/postgresql/operations).

explain analyze --1090
select distinct cu.first_name  || ' ' || cu.last_name as name, 
	count(ren.iid) over (partition by cu.customer_id)
from customer cu
full outer join 
	(select *, r.inventory_id as iid, inv.sf_string as sfs, r.customer_id as cid
	from rental r 
	full outer join 
		(select *, unnest(f.special_features) as sf_string
		from inventory i
		full outer join film f on f.film_id = i.film_id) as inv 
		on r.inventory_id = inv.inventory_id) as ren 
	on ren.cid = cu.customer_id 
where ren.sfs like '%Behind the Scenes%'
order by count desc



--ЗАДАНИЕ №2
--Используя оконную функцию выведите для каждого сотрудника
--сведения о самой первой продаже этого сотрудника.


	--рабочая

select distinct p2.staff_id ,
	first_value (p2.payment_id) over (partition by p2.staff_id order by payment_date)
	from payment p2 
	left join rental r on p2.rental_id = r.rental_id 
	left join inventory i on r.inventory_id =i.inventory_id 
	left join film f on f.film_id =i.film_id 
	group  by p2.staff_id ,p2.payment_id, payment_date


--ЗАДАНИЕ №3
--Для каждого магазина определите и выведите одним SQL-запросом следующие аналитические показатели:
-- 1. день, в который арендовали больше всего фильмов (день в формате год-месяц-день)
-- 2. количество фильмов взятых в аренду в этот день
-- 3. день, в который продали фильмов на наименьшую сумму (день в формате год-месяц-день)
-- 4. сумму продажи в этот день

	
	select  distinct s.store_id as "ID_магазина" ,
	first_value (p.payment_date::date) over (partition by s.store_id order by count(p.payment_id) desc) as "День, больше всего фильмов",
	first_value (count (p.rental_id)) over (partition by s.store_id order by count(p.rental_id) desc) as "Кол-во фильмов" ,
	first_value (p.payment_date::date) over (partition  by s.store_id order by  sum(amount) ) as "День меньше всего" ,
	first_value (sum(p.amount)) over (partition by s.store_id order by sum(p.amount) ) as "Кол-во фильмов"
from payment p 
left join customer c on c.customer_id=p.customer_id 
left join store s on c.store_id =s.store_id 
group by s.store_id, p.payment_date::date 
