/* Запросы к базе

Объединение таблиц
SELECT * FROM students_data
JOIN rooms_data 
ON students_data.room=rooms_data.id

Список комнат и количество студентов в каждой из них

SELECT rooms_data.name AS room_number, 
COUNT(students_data.name) 
FROM students_data
JOIN rooms_data 
ON students_data.room=rooms_data.id
GROUP BY rooms_data.name
ORDER BY rooms_data.name DESC

5 комнат, где самый маленький средний возраст студентов

SELECT SUM((CURRENT_DATE - birthday)/365)/COUNT(birthday) AS avg_age, room
FROM students_data
GROUP BY room
ORDER BY avg_age
LIMIT 5

ИЛИ 

SELECT AVG((CURRENT_DATE - birthday)/365) AS avg_age, room
FROM students_data
GROUP BY room
ORDER BY avg_age
LIMIT 5

ИЛИ 

SELECT AVG((CURRENT_DATE - birthday)/365) AS avg_age, rooms_data.name AS room_name
FROM students_data
JOIN rooms_data 
ON students_data.room=rooms_data.id 
GROUP BY rooms_data.name
ORDER BY avg_age
LIMIT 5

5 комнат с самой большой разницей в возрасте студентов

SELECT rooms_data.name AS room_number,
MAX(CURRENT_DATE-birthday)/365 AS max_age,
MIN(CURRENT_DATE-birthday)/365 AS min_age, 
(MAX(CURRENT_DATE-birthday)- MIN(CURRENT_DATE-birthday))/365 AS delta_age
FROM students_data
JOIN rooms_data 
ON students_data.room=rooms_data.id
GROUP BY room_number
ORDER BY delta_age DESC
LIMIT 5

Список комнат где живут разнополые студенты

SELECT rooms_data.name AS room_number
FROM students_data
JOIN rooms_data 
ON students_data.room=rooms_data.id
GROUP BY room_number
HAVING COUNT(DISTINCT(sex)) = 2
*/