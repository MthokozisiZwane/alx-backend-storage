-- SQL script that ranks country origins of bands
-- script can be executed on any database

SELECT b.origin, COUNT(f.id) as nb_fans
FROM bands b
JOIN fans f ON b.id = f.band_id
GROUP BY b.origin
ORDER BY nb_fans DESC;
