# Write your MySQL query statement below
Select  u.unique_id,e.name from Employees as e
Left Join EmployeeUNI as u
On e.id=u.id;