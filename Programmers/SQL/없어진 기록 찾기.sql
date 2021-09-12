SELECT O.ANIMAL_ID, O.NAME FROM ANIMAL_OUTS O
LEFT OUTER JOIN ANIMAL_INS I
ON O.ANIMAL_ID=I.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL
ORDER BY O.ANIMAL_ID