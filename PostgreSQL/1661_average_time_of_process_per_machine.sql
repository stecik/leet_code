SELECT
  a1.machine_id,
  ROUND(AVG(a2.end - a1.start):: NUMERIC, 3) AS processing_time
FROM
  (
    SELECT
      machine_id,
      process_id,
      timestamp AS start
    FROM
      Activity
    WHERE
      activity_type = 'start'
  ) AS a1
  JOIN (
    SELECT
      machine_id,
      process_id,
      timestamp AS
  end
FROM
  Activity
WHERE
  activity_type = 'end'
) AS a2 ON a1.machine_id = a2.machine_id
AND a1.process_id = a2.process_id
GROUP BY
  a1.machine_id;


SELECT
  a1.machine_id,
  ROUND(AVG(a2.timestamp - a1.timestamp):: NUMERIC, 3) AS processing_time
FROM
  Activity AS a1
  JOIN Activity AS a2 ON a1.machine_id = a2.machine_id
  AND a1.process_id = a2.process_id
  AND a1.activity_type = 'start'
  AND a2.activity_type = 'end'
GROUP BY
  a1.machine_id;


SELECT
  a1.machine_id,
  ROUND(AVG(a2.timestamp - a1.timestamp):: NUMERIC, 3) AS processing_time
FROM
  Activity AS a1,
  Activity AS a2
WHERE
  a1.machine_id = a2.machine_id
  AND a1.process_id = a2.process_id
  AND a1.activity_type = 'start'
  AND a2.activity_type = 'end'
GROUP BY
  a1.machine_id;