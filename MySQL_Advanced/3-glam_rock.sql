--script that lists glam rock bands
SELECT band_name, COALESCE(split, CURRENT_DATE) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;