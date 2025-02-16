SELECT name 
FROM (SELECT managerId FROM Employee GROUP BY managerId HAVING COUNT(managerId) >= 5) AS manId 
JOIN Employee 
ON manId.managerId = Employee.id;