"""
customers-who-never-order
"""
"""
select c.name "Customers"
from Customers c
where c.id not in
(
  select  customerid from orders
);
"""
