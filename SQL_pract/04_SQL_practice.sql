--=============== ������ 6. POSTGRESQL =======================================
--= �������, ��� ���������� ���������� ������ ���������� � ������� ����� PUBLIC===========
SET search_path TO public;

--======== �������� ����� ==============

--������� �1
--�������� SQL-������, ������� ������� ��� ���������� � ������� 
--�� ����������� ��������� "Behind the Scenes".

explain analyze --72.50
select film_id, title, special_features
from film 
where special_features::text like '%Behind the Scenes%' 
and film_id = 1


--������� �2
--�������� ��� 2 �������� ������ ������� � ��������� "Behind the Scenes",
--��������� ������ ������� ��� ��������� ����� SQL ��� ������ �������� � �������.

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


--������� �3
--��� ������� ���������� ���������� ������� �� ���� � ������ ������� 
--�� ����������� ��������� "Behind the Scenes.

--������������ ������� ��� ���������� �������: ����������� ������ �� ������� 1, 
--���������� � CTE. CTE ���������� ������������ ��� ������� �������.

explain analyze --775.71
with  cte_table as (
	select film_id, title, special_features
	from film 
	where special_features::text ilike '%Behind the Scenes%')
	
select c.customer_id, count(cte_table.film_id) as "���������� �������"
from customer c
left join rental r on c.customer_id = r.customer_id
left join inventory i on r.inventory_id = i.inventory_id
left join cte_table on cte_table.film_id = i.film_id 
group by c.customer_id
order by c.customer_id 


--������� �4
--��� ������� ���������� ���������� ������� �� ���� � ������ �������
-- �� ����������� ��������� "Behind the Scenes".

--������������ ������� ��� ���������� �������: ����������� ������ �� ������� 1,
--���������� � ���������, ������� ���������� ������������ ��� ������� �������.

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

--������� �5
--�������� ����������������� ������������� � �������� �� ����������� �������
--� �������� ������ ��� ���������� ������������������ �������������

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

--������� �6
--� ������� explain analyze ��������� ������ �������� ���������� ��������
-- �� ���������� ������� � �������� �� �������:

--1. ����� ���������� ��� �������� ����� SQL, ������������ ��� ���������� ��������� �������, 
--   ����� �������� � ������� ���������� �������
--2. ����� ������� ���������� �������� �������: 
--   � �������������� CTE ��� � �������������� ����������


--======== �������������� ����� ==============

--������� �1
--�������� �� ������ SQL-������. (sql-hw5.sql)

--�������� explain analyze ����� �������.
--����������� �� �������� �������, ������� ����� ����� � ������� ��.
--�������� � ����� �������� �� �������� ����� (���� ��� ������ ���������� ������������ � 15�� � �������!).
--�������� ���������� �������� explain analyze �� ������� ����� ����������������� �������.
-- �������� ����� � explain ����� ���������� �� ������ (https://use-the-index-luke.com/sql/explain-plan/postgresql/operations).

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



--������� �2
--��������� ������� ������� �������� ��� ������� ����������
--�������� � ����� ������ ������� ����� ����������.


	--�������

select distinct p2.staff_id ,
	first_value (p2.payment_id) over (partition by p2.staff_id order by payment_date)
	from payment p2 
	left join rental r on p2.rental_id = r.rental_id 
	left join inventory i on r.inventory_id =i.inventory_id 
	left join film f on f.film_id =i.film_id 
	group  by p2.staff_id ,p2.payment_id, payment_date


--������� �3
--��� ������� �������� ���������� � �������� ����� SQL-�������� ��������� ������������� ����������:
-- 1. ����, � ������� ���������� ������ ����� ������� (���� � ������� ���-�����-����)
-- 2. ���������� ������� ������ � ������ � ���� ����
-- 3. ����, � ������� ������� ������� �� ���������� ����� (���� � ������� ���-�����-����)
-- 4. ����� ������� � ���� ����

	
	select  distinct s.store_id as "ID_��������" ,
	first_value (p.payment_date::date) over (partition by s.store_id order by count(p.payment_id) desc) as "����, ������ ����� �������",
	first_value (count (p.rental_id)) over (partition by s.store_id order by count(p.rental_id) desc) as "���-�� �������" ,
	first_value (p.payment_date::date) over (partition  by s.store_id order by  sum(amount) ) as "���� ������ �����" ,
	first_value (sum(p.amount)) over (partition by s.store_id order by sum(p.amount) ) as "���-�� �������"
from payment p 
left join customer c on c.customer_id=p.customer_id 
left join store s on c.store_id =s.store_id 
group by s.store_id, p.payment_date::date 
