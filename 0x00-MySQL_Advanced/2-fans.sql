-- ranks countries by the number of fans they have
SELECT origin , SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans  DESC;
