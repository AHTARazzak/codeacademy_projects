select *
from countries
limit 10;

select *
from population_years
limit 5;


-- How many entries in the database are from Africa?
select count(*)
from countries
where continent='Africa';


-- What was the total population of Oceania in 2005?
select year, sum(population), countries.continent 
FROM population_years 
JOIN countries 
on population_years.country_id = countries.id 
WHERE population_years.year = 2005 
AND countries.continent = 'Oceania';


-- What is the average population of countries in South America in 2003?
select year, avg(population), countries.continent 
FROM population_years 
join countries
on population_years.country_id = countries.id 
WHERE population_years.year = 2003
AND countries.continent = 'South America';


-- What country had the smallest population in 2007?
select year, min(population), countries.name
from population_years
join countries
on population_years.country_id = countries.id 
WHERE population_years.year = 2007;


-- What is the average population of Poland during the time period covered by this dataset?
select countries.name, avg(population)
from population_years
join countries
on population_years.country_id = countries.id 
WHERE countries.name = 'Poland';


-- How many countries have the word "The" in their name?
select count(*)
from countries
WHERE name like '%the%';



-- What was the total population of each continent in 2010?
select year, sum(population), countries.continent 
FROM population_years 
JOIN countries 
on population_years.country_id = countries.id 
WHERE population_years.year = 2010
group by countries.continent;

