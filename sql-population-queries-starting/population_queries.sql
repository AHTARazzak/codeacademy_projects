-- This is the first query:

SELECT DISTINCT year from population_years;

-- Add your additional queries below:

select population
from population_years
where country = 'Gabon'
order by population desc
limit 1;

select country
from population_years
where year = 2005
order by population asc
limit 10;

select distinct country as '6_country'
from population_years
where population > 100
and year = 2010;

select distinct country
from population_years
where country like '%Islands%';

select *
from population_years
where country = 'Indonesia' and year between 1999 and 2010;
