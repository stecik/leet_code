SELECT a.id FROM Weather AS a JOIN Weather AS b ON DATE(a.recordDate) = DATE(b.recordDate) + 1
WHERE a.temperature > b.temperature;