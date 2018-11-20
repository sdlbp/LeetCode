"""
duplicate-emails
"""
"""
SELECT Email
FROM Person 
GROUP BY Email
having count(Email) > 1;
"""