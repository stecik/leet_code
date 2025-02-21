SELECT
  s.user_id,
  ROUND(
    COALESCE(
      COUNT(c.action) FILTER (
        WHERE
          action = 'confirmed'
      ):: FLOAT / NULLIF(
        COUNT(c.action) FILTER (
          WHERE
            action = 'timeout'
        ) + COUNT(c.action) FILTER (
          WHERE
            action = 'confirmed'
        ),
        0
      ),
      0
    ):: NUMERIC,
    2
  ) AS confirmation_rate
FROM
  Signups AS s
  LEFT JOIN Confirmations AS c ON s.user_id = c.user_id
GROUP BY
  s.user_id;