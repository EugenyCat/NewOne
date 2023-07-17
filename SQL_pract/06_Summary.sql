--Which cities have more than one airport?
select city, count(distinct a.airport_code) from airports a 
group by city
having count(distinct a.airport_code) > 1


--At which airports are there flights performed by an aircraft with the maximum range of flight?
select distinct a2.airport_name from aircrafts a 
left join flights f on a.aircraft_code = f.aircraft_code 
left join airports a2 on f.departure_airport = a2.airport_code 
where a."range" = (
		select max("range")
		from aircrafts
		)
		
		
--Withdraw 10 flights with maximum delay time
select f.flight_no, (f.actual_departure - f.scheduled_departure) as "delay_time", f.actual_departure, f.scheduled_departure from flights f 
where f.actual_departure is not null 
order by "delay_time" desc
limit 10


--Were there any reservations for which boarding passes were not received?
select distinct b.book_ref, bp.boarding_no from bookings b 
left join tickets t on b.book_ref = t.book_ref 
left join boarding_passes bp on t.ticket_no = bp.ticket_no
where bp.boarding_no is null



--Find the number of available seats for each flight, their % ratio to the total number of seats on the plane. 
--Add a column with a cumulative total - a cumulative accumulation of the number of departed passengers from each airport for each day. 
--I.e. this column should reflect the cumulative amount - how many people have already left the airport on this or earlier flights during the day.
with CTE_count_passangers as (
select 	f.flight_id , 
		count(bp.seat_no) as "count passangers", 
		f.aircraft_code, 
		f.departure_airport, 
		f.actual_departure ,
		sum(count(bp.seat_no)) over (partition by f.departure_airport, f.actual_departure order by f.actual_departure) as "count pass from airport by day"
from flights f 
left join ticket_flights tf on tf.flight_id = f.flight_id 
left join boarding_passes bp on tf.ticket_no = bp.ticket_no and tf.flight_id = bp.flight_id 
group by f.flight_id, f.aircraft_code, f.departure_airport , f.actual_departure
order by f.departure_airport, f.actual_departure 
),
CTE_count_seats as (
select s.aircraft_code, count(s.seat_no) as "count seats" from seats s
group by s.aircraft_code
)
select cp.flight_id, 
		"count passangers", 
		"count seats",  round("count passangers"::float/"count seats"::float*100) as "Realtion %",
		cp.departure_airport, 
		cp.actual_departure::date ,
		cp."count pass from airport by day"
from CTE_count_passangers cp
left join CTE_count_seats cs on cs.aircraft_code = cp.aircraft_code




--Find the percentage of flights by type of aircraft from total
select f.aircraft_code
		,round((count(f.flight_id)::float / 
		(
		select count(tf.flight_id) from flights tf
		)::float*100.0))
from flights f 
group by f.aircraft_code

select count(tf.flight_id) from ticket_flights tf


--Were there cities to which you can get business class cheaper than economy class as part of the flight?
with cte_business as (
select distinct 	tf.flight_id,
					a.city ,
					tf.amount as "amount Business"
from ticket_flights tf 
left join flights f on f.flight_id = tf.flight_id 
left join airports a on a.airport_code = f.arrival_airport 
where tf.fare_conditions = 'Business'
)
select distinct 	tf.flight_id,
					tf.amount as "amount Economy", 
					cb."amount Business",
					cb.city
from ticket_flights tf 
left join cte_business cb on cb.flight_id = tf.flight_id
where tf.fare_conditions = 'Economy' and cb."amount Business" <= tf.amount


--What cities don’t have direct flights between them?

create view cities_without_right_flights
AS
select a.city as "city from", a2.city as "city to"  from airports a --a.airport_code, 
cross join airports a2
where a2.city <> a.city
except
select distinct a.city as "city from", a2.city as "city to" from flights f
left join airports a on a.airport_code = f.departure_airport 
left join airports a2 on a2.airport_code = f.arrival_airport 


select *
from cities_without_right_flights





--Calculate the distance between airports connected by direct flights, 
--compare with the permissible maximum range of flights in aircraft serving these flights*


with cte_rangeis as (
	select distinct 	f.departure_airport, 
						f.arrival_airport,
						a.city,
						a2.city,
						a3."range",
						acos(
								sin(radians(a.latitude))*sin(radians(a2.latitude)) 
								+
								cos(radians(a.latitude))*cos(radians(a2.latitude))
								*
								cos(radians(a.longitude) - radians(a2.longitude))
							) * 6371 as "Range between cities in km"
	from flights f
	left join airports a on a.airport_code = f.departure_airport 
	left join airports a2 on a2.airport_code = f.arrival_airport 
	left join aircrafts a3 on a3.aircraft_code = f.aircraft_code 
) select *,
		case 
			when "range" >= "Range between cities in km" then 'Range between cities, km is more then range of aircraft'
			when "range" < "Range between cities in km" then 'Range between cities, km is less then range of aircraft'
			else 'Error'
		end as "Comparing"
from cte_rangeis





