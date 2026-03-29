# Write your MySQL query statement below
select email as Email
from person
GROUP BY email
HAVING COUNT(email) > 1;
