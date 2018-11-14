"""
combine-two-tables
"""
"""
select FirstName, LastName, City, State
from Person left join Address
on Person.PersonID = Address.PersonID 
"""
"""
select a.Name Employee
from Employee e
JOIN Employee a
on e.Id=a.ManagerId
where e.Salary < a.Salary
"""