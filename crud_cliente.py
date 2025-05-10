## Insertar un fallecido
INSERT INTO fallecido (idfallecido, nombre, apellido, fecha_muerte, causa_muerte, lugar_muerte)
VALUES (1, 'Juan', 'Pérez', '2023-05-09 14:00:00', 'Infarto', 'Tuxtla Gutiérrez');

## Leer (Consultar) un fallecido
SELECT * FROM fallecido WHERE idfallecido = 1;

## Actualizar un fallecido
UPDATE fallecido
SET nombre = 'Juan Carlos', causa_muerte = 'Accidente'
WHERE idfallecido = 1;

## Eliminar un fallecido
DELETE FROM fallecido WHERE idfallecido = 1;