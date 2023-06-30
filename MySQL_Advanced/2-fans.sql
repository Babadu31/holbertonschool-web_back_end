-- lists fans by country of origin

SELECT origin, SUM(fans) as nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;
