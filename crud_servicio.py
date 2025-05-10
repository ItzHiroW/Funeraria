## Insertar un cliente
INSERT INTO clientes (nombre, apellido, direccion, telefono, correo, idfallecido)
VALUES ('Carlos', 'López', 'Calle 123', '9611234567', 'carlos@gmail.com', 1);

## Leer (Consultar) un cliente
SELECT * FROM clientes WHERE idcliente = 1;

## Actualizar un cliente
UPDATE clientes
SET direccion = 'Calle 456', telefono = '9617654321'
WHERE idcliente = 1;

## Eliminar un cliente
DELETE FROM clientes WHERE idcliente = 1;