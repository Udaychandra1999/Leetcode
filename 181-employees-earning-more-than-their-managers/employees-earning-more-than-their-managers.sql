# Write your MySQL query statement below
select Worker.name as Employee from Employee as Worker 
inner join Employee as Manager 
on (Worker.managerId = Manager.id)
where Worker.salary > Manager.salary;