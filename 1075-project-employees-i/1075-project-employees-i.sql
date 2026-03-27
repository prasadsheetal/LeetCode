# Write your MySQL query statement below
Select p.project_id,ROUND(AVG(e.experience_years),2) AS average_years 
from project as p
join employee as e
on p.employee_id=e.employee_id
Group by p.project_id;
