# Write your MySQL query statement below
Select c.name as Customers
from Customers as c
left join orders as o
on c.id=o.customerId
where o.customerid is null;