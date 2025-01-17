Запросы к таблице country:

1. Вывести названия всех стран Евразии:

SELECT name
FROM country
WHERE Continent = 'Asia' OR 'Europe';

2. Вывести названия регионов и стран, в которых ожидаемая продолжительность жизни меньше пятидесяти лет:

SELECT Region, Name
FROM country
WHERE LifeExpectancy IS NOT NULL AND LifeExpectancy < 50;

3. Вывести название самой крупной по площади страны Африки

SELECT Name
FROM country
WHERE Continent = 'Africa'
ORDER BY SurfaceArea DESC
LIMIT 1;

4. Вывести названия пяти азиатских стран с самой низкой плотностью населения:

SELECT Name
FROM country
WHERE Continent = 'Asia'
ORDER BY Population / SurfaceArea
LIMIT 5;

Запросы к таблице city

5. Вывести в порядке возрастания населения коды стран и названия городов, численность населения которых превышает пять миллионов человек:

SELECT CountryCode, Name
FROM city
WHERE Population > 5000000
ORDER BY Population;

6. Вывести название города в Индии с самым длинным названием:

SELECT Name
FROM city 
ORDER BY char_length(Name) DESC
LIMIT 1;