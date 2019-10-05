from django.db import models

# Create your models here.
"""
-- DOMAINS
Create domain AreaCode as Varchar(5);
Create domain EmployeeKey as Varchar(5);
Create domain ClientKey as Varchar(5);
Create domain ProductKey as Varchar(10);
Create domain CategoryKey as Varchar(10);
Create domain ProviderKey as Varchar(10);
Create domain NotificationKey as Varchar(10);

-- CREATE TABLE
Create table Area (
	area_code AreaCode NOT NULL,
	area varchar(30) NOT NULL,
    primary key (area_code)
) Without Oids;

* empleado
    - id
    - email
    - password
    - nombre
    - apellido
    - fecha_inicio
    - area
    - sueldo
    - is_super_user
    - is_area_admin

-- CREATE TABLE
CREATE TABLE Employee (
    emp_key EmployeeKey NOT NULL, 
    email varchar(75) NOT NULL UNIQUE, 
    password varchar(128) NOT NULL, 
    first_name varchar(50) NOT NULL, 
    last_name varchar(50) NOT NULL, 
    date_joined timestamp with time zone NOT NULL,
    area AreaCode,
    is_superuser boolean NOT NULL, 
    is_areaadmin boolean NOT NULL, 
    is_simplemortal boolean NOT NULL, 
    primary key (emp_key)
) Without Oids;

-- FOREIGN KEYS Employee
Alter table Employee add foreign key (area) references Area (area_code) on update cascade on delete set null;

* cliente
    - claveCliente
    - nombre
    - RFC
    - direccion
    - correo
    - telefono

-- CREATE TABLE
CREATE TABLE Client (
    client_key ClientKey NOT NULL, 
    name varchar(50) NOT NULL,
    rfc varchar(128) NOT NULL UNIQUE, 
    address varchar(60) NOT NULL, 
    email varchar(75), 
    phone varchar(30), 
    primary key (client_key)
) Without Oids;

-- CREATE TABLE
CREATE TABLE Category (
    category_key CategoryKey NOT NULL, 
    name varchar(75) NOT NULL, 
    description varchar(128), 
    primary key (category_key)
) Without Oids;

-- CREATE TABLE
CREATE TABLE Provider (
    provider_key ProviderKey NOT NULL, 
    name varchar(50) NOT NULL,
    rfc varchar(128) NOT NULL UNIQUE, 
    address varchar(60) NOT NULL, 
    email varchar(75), 
    phone varchar(30), 
    primary key (provider_key)
) Without Oids;

-- CREATE TABLE
CREATE SEQUENCE seq_autoid_prod
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9999
  START 1;

-- STORED PROCEDURE
CREATE OR REPLACE FUNCTION generate_product_id() RETURNS varchar AS 
$$
  DECLARE
    id_producto ProductKey;
  BEGIN
    SELECT TO_CHAR(nextval('seq_autoid_prod'::regclass),'"PROD"fm0000') INTO id_producto;
    return id_producto;
  END;
$$ LANGUAGE 'plpgsql'


CREATE TABLE Product (
    product_key ProductKey NOT NULL, 
    name varchar(75) NOT NULL, 
    description varchar(128), 
    price numeric(10,2) NOT NULL, 
    category CategoryKey,
    provider ProviderKey,
    primary key (product_key)
) Without Oids;

-- FOREIGN KEYS Product
Alter table Product add foreign key (category) references Category (category_key) on update cascade on delete set null;
Alter table Product add foreign key (provider) references Provider (provider_key) on update cascade on delete set null;

CREATE TABLE Stock (
    id serial NOT NULL,
    product ProductKey,
    amount numeric(10),
    primary key(id)
) Without Oids;

-- FOREIGN KEYS Stock
Alter table Stock add foreign key (product) references Product (product_key) on update cascade on delete cascade;

CREATE OR REPLACE FUNCTION editStock(id_product ProductKey, new_amount numeric(10)) RETURNS BOOLEAN AS 
$$    
  BEGIN
    UPDATE Stock  
    SET amount = new_amount
    WHERE product = id_product;  
    RETURN found;
  END;
$$ LANGUAGE 'plpgsql';

CREATE TABLE Purchase (
    id serial NOT NULL,
    product ProductKey NOT NULL,
    amount numeric(10) NOT NULL,
    provider ProviderKey,
    total numeric(12,2),
    buyer EmployeeKey NOT NULL,
    purchase_date timestamp with time zone NOT NULL,
    primary key(id)
) Without Oids;

-- FOREIGN KEYS Purchase
Alter table Purchase add foreign key (provider) references Provider (provider_key) on update cascade on delete set null;
Alter table Purchase add foreign key (buyer) references Employee (emp_key) on update cascade on delete set null;

CREATE OR REPLACE FUNCTION purchaseProduct(id_product ProductKey, amount_product numeric(10), provider ProviderKey, total numeric(12,2), buyer EmployeeKey) RETURNS BOOLEAN AS 
$$    
  DECLARE
	purchase_date timestamp; 
	amount_purchase decimal(10);
	current_amount decimal(10);
	new_amount decimal(10);
	id_purchase decimal(10);
  BEGIN
	SELECT now() INTO purchase_date;
	  Select nextval(pg_get_serial_sequence('Sale', 'id')) INTO id_purchase;
	amount_purchase:= amount_product;
	INSERT INTO Purchase VALUES(id_purchase, id_product, amount_product, provider, total, buyer, purchase_date);
	IF found THEN
	SELECT amount INTO current_amount FROM Stock WHERE product = id_product;
	new_amount := current_amount + amount_purchase;
		UPDATE Stock  
		SET amount = new_amount
		WHERE product = id_product; 
		RETURN found;   
	ELSE
		RETURN found;
	END IF;
  END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION deletePurchase(id_purchase decimal(10)) RETURNS BOOLEAN  AS
$$
   BEGIN
    DELETE FROM Purchase WHERE id = id_purchase;
    RETURN found;  
   END;
$$ LANGUAGE 'plpgsql';

CREATE TABLE Sale (
    id serial NOT NULL,
    product ProductKey NOT NULL,
    amount numeric(10) NOT NULL,
    client ClientKey,
    total numeric(12,2),
    seller EmployeeKey NOT NULL,
    sale_date timestamp with time zone NOT NULL,
    primary key(id)
) Without Oids;

-- FOREIGN KEYS Sale
Alter table Sale add foreign key (client) references Client (client_key) on update cascade on delete set null;
Alter table Sale add foreign key (seller) references Employee (emp_key) on update cascade on delete set null;

CREATE OR REPLACE FUNCTION sellProduct(id_product ProductKey, amount_product numeric(10), client ClientKey, total numeric(12,2), seller EmployeeKey) RETURNS BOOLEAN AS 
$$    
  DECLARE
    sell_date timestamp; 
    amount_sale decimal(10);
    current_amount decimal(10);
    new_amount decimal(10);
	  id_sell decimal(10);
  BEGIN
    SELECT now() INTO sell_date;
	  Select nextval(pg_get_serial_sequence('Sale', 'id')) INTO id_sell;
    amount_sale:= amount_product;
    INSERT INTO Sale VALUES(id_sell, id_product, amount_product, client, total, seller, sell_date);
    IF found THEN
    SELECT amount INTO current_amount FROM Stock WHERE product = id_product;
    new_amount := current_amount - amount_sale;
		UPDATE Stock  
        SET amount = new_amount
        WHERE product = id_product; 
        RETURN found;   
    ELSE
        RETURN found;
    END IF;
  END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION deleteSale(id_sale decimal(10)) RETURNS BOOLEAN  AS
$$
   BEGIN
    DELETE FROM Sale WHERE id = id_sale;
    RETURN found;  
   END;
$$ LANGUAGE 'plpgsql';

CREATE TABLE Notification (
    notification_key NotificationKey NOT NULL,
    transmitter EmployeeKey,
    description varchar(128),
    transmitter_area AreaCode,
    notification_type decimal(2),
    primary key(notification_key)
) Without Oids;

-- FOREIGN KEYS Notification
Alter table Notification add foreign key (transmitter) references Employee (emp_key) on update cascade on delete set null;
Alter table Notification add foreign key (transmitter_area) references Area (area_code) on update cascade on delete set null;

CREATE TABLE NotiEmployee (
    id serial NOT NULL,
    last_notification NotificationKey,
    employee EmployeeKey,
    area AreaCode,
    primary key(id)
) Without Oids;

-- FOREIGN KEYS Notification
Alter table NotiEmployee add foreign key (last_notification) references Notification (notification_key) on update cascade on delete cascade;
Alter table NotiEmployee add foreign key (employee) references Employee (emp_key) on update cascade on delete cascade;

-- INSERTS Area
INSERT INTO Area VALUES('AAVEN','Administrador Ventas');
INSERT INTO Area VALUES('AACOM','Administrador Compras');
INSERT INTO Area VALUES('AAALM','Administrador Almacén');
INSERT INTO Area VALUES('SADMI','Super Administrador');
INSERT INTO Area VALUES('AA','Área Almacén');
INSERT INTO Area VALUES('AC','Área Compras');
INSERT INTO Area VALUES('AV','Área Ventas');

-- INSERTS Employee
INSERT INTO Employee VALUES('SA001','edgar@mail.com','pbkdf2_sha256$150000$wE9JmStZJWPh$TRMl/z4tXQYs2VqerMc3di0d0trHq2tPANELEoxmjm4=','Edgar', 'Gómez', '2019-09-23 09:46:31.22461-05', 'SADMI', TRUE, FALSE, FALSE);
INSERT INTO Employee VALUES('SA002','paola@mail.com','pbkdf2_sha256$150000$k0PywcaQyaaV$v/aW088rgR4LrYXJKCgviu956N7j09bmDQz4fIBl2h0=','Paola', 'Quezada', '2019-09-23 09:46:31.22461-05', 'SADMI', TRUE, FALSE, FALSE);
-- Password: employee123
INSERT INTO Employee VALUES('AA001','juan@mail.com','pbkdf2_sha256$150000$OXNYAGopz2wm$L9VkR91l0dEbZgPVmUk2tUwK5CQelrakG9pdiSsq9Qg=','Juan', 'López', '2019-09-23 09:46:31.22461-05', 'AA', FALSE, FALSE, TRUE);
INSERT INTO Employee VALUES('AC001','maria@mail.com','pbkdf2_sha256$150000$OXNYAGopz2wm$L9VkR91l0dEbZgPVmUk2tUwK5CQelrakG9pdiSsq9Qg=','Maria', 'Echeverria', '2019-09-23 09:46:31.22461-05', 'AC', FALSE, FALSE, TRUE);
INSERT INTO Employee VALUES('AC002','saul@mail.com','pbkdf2_sha256$150000$OXNYAGopz2wm$L9VkR91l0dEbZgPVmUk2tUwK5CQelrakG9pdiSsq9Qg=','Saul', 'Dorantes', '2019-09-23 09:46:31.22461-05', 'AC', FALSE, FALSE, TRUE);
INSERT INTO Employee VALUES('AV001','rodrigo@mail.com','pbkdf2_sha256$150000$OXNYAGopz2wm$L9VkR91l0dEbZgPVmUk2tUwK5CQelrakG9pdiSsq9Qg=','Rodrigo', 'Huerta', '2019-09-23 09:46:31.22461-05', 'AV', FALSE, FALSE, TRUE);
INSERT INTO Employee VALUES('AV002','anahi@mail.com','pbkdf2_sha256$150000$OXNYAGopz2wm$L9VkR91l0dEbZgPVmUk2tUwK5CQelrakG9pdiSsq9Qg=','Anahi', 'Martinez', '2019-09-23 09:46:31.22461-05', 'AV', FALSE, FALSE, TRUE);
-- Password: admin123
INSERT INTO Employee VALUES('AAC01','margarita@mail.com','pbkdf2_sha256$150000$xwzLHlVLuCzf$fdbqPpA02u1sVusR90/nAhu/b7DQUWcLqDzBAMkwaKM=','Margarita', 'Prado', '2019-09-23 09:46:31.22461-05', 'AACOM', FALSE, TRUE, FALSE);
INSERT INTO Employee VALUES('AAL01','alejandro@mail.com','pbkdf2_sha256$150000$xwzLHlVLuCzf$fdbqPpA02u1sVusR90/nAhu/b7DQUWcLqDzBAMkwaKM=','Alejandro', 'León', '2019-09-23 09:46:31.22461-05', 'AAALM', FALSE, TRUE, FALSE);

INSERT INTO Client VALUES('CL001','Luis Perez','LUPE0201694','Calle Santa Fe #18', 'luis@mail.com', '442-210-1520');
INSERT INTO Client VALUES('CL002','Andrea Montes','AN856985984','Calle Santa Fe #18', 'luis@mail.com', '442-210-1520');


INSERT INTO NotiEmployee VALUES(1, NULL, 'SA001', 'SADMI');
INSERT INTO NotiEmployee VALUES(2, NULL, 'AA001', 'SADMI');
INSERT INTO NotiEmployee VALUES(3, NULL, 'AC001', 'AA');
INSERT INTO NotiEmployee VALUES(4, NULL, 'AV001', 'AC');
INSERT INTO NotiEmployee VALUES(5, NULL, 'SA001', 'AV');
INSERT INTO NotiEmployee VALUES(6, NULL, 'AAC01', 'AACOM');
INSERT INTO NotiEmployee VALUES(7, NULL, 'AAL01', 'AAALM');

-- INSERTS Category
INSERT INTO Category VALUES('BOMBON','Bombones', 'Golosina elaborada con azúcar, claras, saborizantes y grenetina, cubierta con azúcar glass y almidón.');
INSERT INTO Category VALUES('CARAMELO','Caramelos', 'El caramelo es un alimento preparado generalmente a base de azúcar.');
INSERT INTO Category VALUES('CHOCOLATE','Chocolates', 'El chocolate se obtiene mezclando azúcar con dos productos derivados de la manipulación de las semillas del cacao.');
INSERT INTO Category VALUES('GALLETA','Galletas', 'La galleta es un producto alimenticio pequeño y plano, dulce o salado, horneado.');
INSERT INTO Category VALUES('GOMITA','Gomitas', 'Caramelos masticables muy dulces, elaborados con gelatina animal añadiendo edulcorantes, saborizantes y colorantes alimentarios');
INSERT INTO Category VALUES('PALETA','Paletas', 'Helado hecho a base de agua, colorante, saborizante y azúcar, de forma alargada y con un palo que lo atraviesa para tomarlo.');
INSERT INTO Category VALUES('PAPA','Papas', 'Se preparan cortándose en rodajas o en forma de bastones y friéndolas en aceite caliente hasta que queden doradas.');

INSERT INTO Provider VALUES('DLAROSA','De la Rosa', 'RO180201694', 'Avenida Siempre Viva #18', 'durose@mail.com', '2101616');
INSERT INTO Provider VALUES('RIKOLINO','Rikolino', 'RIDU180204UF8', 'Calle Hinojosa #5', 'rikolino@mail.com', '2101617');
INSERT INTO Provider VALUES('WONKA','Wonka', 'DUWO180207UV6', 'Avenida Revolucion #30', 'wonka@mail.com', '2101618');
INSERT INTO Provider VALUES('JOLLYRAN','Jolly Rancher', 'JORD1803074910', 'Carretera 57 #255', 'jolly@mail.com', '2101619');
INSERT INTO Provider VALUES('GABI','Gabi', 'GAGA180309I74', 'Carretera San Juan S/N', 'gabiga@mail.com', '2101716');
INSERT INTO Provider VALUES('MARINELA','Marinela', 'MAGA180329FU9', 'Epigmenio Gonzales #13', 'marinela@mail.com', '2101717');
INSERT INTO Provider VALUES('GAMESA','Gamesa', 'GAGA100920QY8', 'Calle Benito Juarez #515', 'gamesa@mail.com', '2101718');
INSERT INTO Provider VALUES('CORONADO','Coronado', 'CODU1004111P6', 'Avenida Allende #8A', 'coronado@mail.com', '2101719');
INSERT INTO Provider VALUES('SABRITAS','Sabritas', 'PASA101011396', 'Carretera Mexico-Qro #853', 'sabritas@mail.com', '2102016');
INSERT INTO Provider VALUES('COYOTES','Coyotes', 'PACO151211GS0', 'Avenida Roldan #95', 'coyotes@mail.com', '2102017');


-- INSERTS CATEGORÍA BOMBON

INSERT INTO Product VALUES(generate_product_id(),'MALVAVISCO CHOC ATREVETE', 'Caja con 28P', 478.91, 'BOMBON', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'MALVALLENO SABOR FRESA', 'Caja con 12P', 254.52, 'BOMBON', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'AMBELITOS MEDIANO DELICIAS ', 'Caja con 15P', 146.99, 'BOMBON', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'BOMBON AMBELITOS M.M. DELICIAS', 'Caja con 5P', 142.32, 'BOMBON', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'MALVAVISCO FIGURAS DELICIAS', 'Caja con 60P', 279.97, 'BOMBON', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'BOMBON GRAGEA', 'Caja con 36P', 420.57, 'BOMBON', 'GABI');
INSERT INTO Product VALUES(generate_product_id(),'BOMBON ARCOIRIS', 'Caja con 36P', 420.57, 'BOMBON', 'GABI');
INSERT INTO Product VALUES(generate_product_id(),'BOMBON ANILLO', 'Caja con 28P', 359.83, 'BOMBON', 'GABI');
INSERT INTO Product VALUES(generate_product_id(),'BOMBON MINI', 'Caja con 15P', 233.60, 'BOMBON', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'BOMBON GRAGEA CORAZON', 'Caja con 18P', 276.79, 'BOMBON', 'RIKOLINO');


-- INSERTS CATEGORÍA CARAMELO

INSERT INTO Product VALUES(generate_product_id(),'NEW LOOK CANDY', 'Caja con 28P', 584.74, 'CARAMELO', 'JOLLYRAN');
INSERT INTO Product VALUES(generate_product_id(),'PAQUETE DIVERSION', 'Caja con 6P', 715.18, 'CARAMELO', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'APPLE GREEN RING', 'Caja con 8P', 441.26, 'CARAMELO', 'WONKA');
INSERT INTO Product VALUES(generate_product_id(),'CARAMELO SUAVE DISNEY', 'Caja con 30P', 733.02, 'CARAMELO', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'CARAMELO HANNA MONTANA', 'Caja con 30P', 525.33, 'CARAMELO', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'CARAMELO SUAVE TOY', 'Caja con 30P', 733.02, 'CARAMELO', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'REVOLCADITAS MANGO', 'Caja con 24P', 741.29, 'CARAMELO', 'COYOTES');
INSERT INTO Product VALUES(generate_product_id(),'CONFITADO CHICO', 'Caja con 50P', 918.32, 'CARAMELO', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'CONFITADO CHICO', 'Caja con 50P', 918.32, 'CARAMELO', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'CHILIROKAS FRESA', 'Caja con 24P', 517.52, 'CARAMELO', 'CORONADO');
INSERT INTO Product VALUES(generate_product_id(),'CHILIROKAS SDA', 'Caja con 24P', 587.52, 'CARAMELO', 'CORONADO');


-- INSERTS CATEGORÍA CHOCOLATE

INSERT INTO Product VALUES(generate_product_id(),'BUBULUBU', 'Caja con 24P', 313.16, 'CHOCOLATE', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'DUVALIN', 'Caja con 24P', 416.73, 'CHOCOLATE', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'BON O BON', 'Caja con 12P', 663.24, 'CHOCOLATE', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'POLLITOS DE CHOCOLATE', 'Caja con 20P', 525.54, 'CHOCOLATE', 'CORONADO');
INSERT INTO Product VALUES(generate_product_id(),'PALETON GRAGONS', 'Caja con 12P', 355.60, 'CHOCOLATE', 'JOLLYRAN');
INSERT INTO Product VALUES(generate_product_id(),'BALON CHUTAZO', 'Caja con 20P', 524.08, 'CHOCOLATE', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'CANASTA ROMPOPE', 'Caja con 24P', 278.49 , 'CHOCOLATE', 'CORONADO');
INSERT INTO Product VALUES(generate_product_id(),'CANASTA FRESA', 'Caja con 24P', 305.59 , 'CHOCOLATE', 'CORONADO');
INSERT INTO Product VALUES(generate_product_id(),'KRANKY GRANEL', 'Caja con 12P', 207.24, 'CHOCOLATE', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'CHOCORETAS', 'Caja con 10P', 460.05, 'CHOCOLATE', 'RIKOLINO');

-- INSERTS PAPAS
INSERT INTO Product VALUES(generate_product_id(),'PAPA HABANERA  30G', 'Caja con 20P ', 321.92, 'PAPA', 'COYOTES');
INSERT INTO Product VALUES(generate_product_id(),'PAPA JALAPEÑO  30G', 'Caja con 20P ', 354.64, 'PAPA', 'COYOTES');
INSERT INTO Product VALUES(generate_product_id(),'PAPA ADOBADA  30G', 'Caja con 20P ', 321.92, 'PAPA', 'COYOTES');
INSERT INTO Product VALUES(generate_product_id(),'PAPA MIX  30G', 'Caja con 30P ', 474.58, 'PAPA', 'COYOTES');
INSERT INTO Product VALUES(generate_product_id(),'PAPA FUEGO  50G', 'Caja con 8P ', 181.79, 'PAPA', 'COYOTES');
INSERT INTO Product VALUES(generate_product_id(),'TOSTITOS', 'Caja con 24P ', 390.11, 'PAPA', 'SABRITAS');
INSERT INTO Product VALUES(generate_product_id(),'DORITOS NACHO', 'Caja con 18P ', 231.64, 'PAPA', 'SABRITAS');
INSERT INTO Product VALUES(generate_product_id(),'DORITOS DINAMITA', 'Caja con 18P ', 241.42, 'PAPA', 'SABRITAS');
INSERT INTO Product VALUES(generate_product_id(),'FRITOS SAL', 'Caja con 6P ', 197.95, 'PAPA', 'SABRITAS');
INSERT INTO Product VALUES(generate_product_id(),'FRITOS CJORIZO', 'Caja con 6P ', 197.95, 'PAPA', 'SABRITAS');

-- INSERS PALETAS
INSERT INTO Product VALUES(generate_product_id(),'PALETON CORONADO', 'Caja con 50P ', 572.51, 'PALETA', 'CORONADO');
INSERT INTO Product VALUES(generate_product_id(),'PALETA TIRA CORONADO', 'Caja con 50P ', 477.63, 'PALETA', 'CORONADO');
INSERT INTO Product VALUES(generate_product_id(),'PALETA PAYASO', 'Caja con 18P ', 801.36, 'PALETA', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'PALETA PAYASO MINI', 'Caja con 15P ', 637.86, 'PALETA', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'PALETA BOLA CAJETA', 'Caja con 40P ', 710.29, 'PALETA', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'PALETA AGRIMIEL', 'Caja con 20P ', 219.38, 'PALETA', 'RIKOLINO');
INSERT INTO Product VALUES(generate_product_id(),'CHUPETA ICE CREAM', 'Caja con 12P ', 448.34, 'PALETA', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'PALETON DE LA ROSA', 'Caja con 12P ', 491.44, 'PALETA', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'PALETA PELUCA MANGO', 'Caja con 18P ', 495.42, 'PALETA', 'DLAROSA');

-- INSERS GOMITAS
INSERT INTO Product VALUES(generate_product_id(),'GOMA MORA', 'Caja con 16P ', 360.10, 'GOMITA', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'GOMA FRAMBUESA', 'Caja con 16P ', 360.10, 'GOMITA', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'GOMA GRENETINA', 'Caja con 16P ', 345.47, 'GOMITA', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'GOMITA GAHOT', 'Caja con 20P ', 408.89, 'GOMITA', 'DLAROSA');
INSERT INTO Product VALUES(generate_product_id(),'JOLLY RANCHER FILLED GUMMIES', 'Caja 25LBS ', 620.73, 'GOMITA', 'JOLLYRAN');

-- INSERS GALLETAS
INSERT INTO Product VALUES(generate_product_id(),'BARRITAS FRESA', 'Caja con 12P ', 290.14, 'GALLETA', 'MARINELA');
INSERT INTO Product VALUES(generate_product_id(),'BARRITAS PIÑA', 'Caja con 12P ', 311.63, 'GALLETA', 'MARINELA');
INSERT INTO Product VALUES(generate_product_id(),'PRINCIPE', 'Caja con 9P ', 251.95, 'GALLETA', 'MARINELA');
-------------------------------------------
-- STORED PROCEDURE
CREATE OR REPLACE FUNCTION addProduct(name VARCHAR(75), description VARCHAR(75), price DECIMAL(10,2), category CategoryKey, provider ProviderKey, amount_prod numeric(10)) RETURNS BOOLEAN AS 
$$    
  DECLARE
    id_product ProductKey;
	id_stock decimal(10);
  BEGIN
    SELECT generate_product_id() INTO id_product;
    INSERT INTO Product VALUES(id_product, name, description, price, category, provider);
    IF found THEN
		SELECT MAX(id) + 1 FROM Stock INTO id_stock;
        INSERT INTO Stock(id, product, amount) VALUES(id_stock, id_product, amount_prod);
        RETURN found;  
    ELSE
        RETURN found;
    END IF;
  END;
$$ LANGUAGE 'plpgsql';

SELECT addProduct('TRIKI TRAKES', 'Caja con 10P ', 291.45, 'GALLETA', 'MARINELA', 20);
SELECT addProduct('PLATIVOLOS', 'Caja con 12P ', 274.14, 'GALLETA', 'MARINELA', 20);
SELECT addProduct('POLVORONES', 'Caja con 12P ', 273.48, 'GALLETA', 'MARINELA', 20);
SELECT addProduct('MAMUT', 'Caja con 8P ', 253.77, 'GALLETA', 'GAMESA', 20);
SELECT addProduct('CHOKIS', 'Caja con 10P ', 102.57, 'GALLETA', 'GAMESA', 20);
SELECT addProduct('CREMAX FRESA', 'Caja con 8P ', 122.03, 'GALLETA', 'GAMESA', 20);
SELECT addProduct('EMPERADOR LIMON 212G', 'Caja con 10P ', 99.72, 'GALLETA', 'GAMESA', 20);

-- INSERTS STOCK
INSERT INTO Stock VALUES(1, 'PROD0001', 20);
INSERT INTO Stock VALUES(2, 'PROD0002', 20);
INSERT INTO Stock VALUES(3, 'PROD0003', 20);
INSERT INTO Stock VALUES(4, 'PROD0004', 20);
INSERT INTO Stock VALUES(5, 'PROD0005', 20);
INSERT INTO Stock VALUES(6, 'PROD0006', 20);
INSERT INTO Stock VALUES(7, 'PROD0007', 20);
INSERT INTO Stock VALUES(8, 'PROD0008', 20);
INSERT INTO Stock VALUES(9, 'PROD0009', 20);
INSERT INTO Stock VALUES(10, 'PROD0010', 20);
INSERT INTO Stock VALUES(11, 'PROD0011', 20);
INSERT INTO Stock VALUES(12, 'PROD0012', 20);
INSERT INTO Stock VALUES(13, 'PROD0013', 20);
INSERT INTO Stock VALUES(14, 'PROD0014', 20);
INSERT INTO Stock VALUES(15, 'PROD0015', 20);
INSERT INTO Stock VALUES(16, 'PROD0016', 20);
INSERT INTO Stock VALUES(17, 'PROD0017', 20);
INSERT INTO Stock VALUES(18, 'PROD0018', 20);
INSERT INTO Stock VALUES(19, 'PROD0019', 20);
INSERT INTO Stock VALUES(20, 'PROD0020', 20);
INSERT INTO Stock VALUES(21, 'PROD0021', 20);
INSERT INTO Stock VALUES(22, 'PROD0022', 20);
INSERT INTO Stock VALUES(23, 'PROD0023', 20);
INSERT INTO Stock VALUES(24, 'PROD0024', 20);
INSERT INTO Stock VALUES(25, 'PROD0025', 20);
INSERT INTO Stock VALUES(26, 'PROD0026', 20);
INSERT INTO Stock VALUES(27, 'PROD0027', 20);
INSERT INTO Stock VALUES(28, 'PROD0028', 20);
INSERT INTO Stock VALUES(29, 'PROD0029', 20);
INSERT INTO Stock VALUES(30, 'PROD0030', 20);
INSERT INTO Stock VALUES(31, 'PROD0031', 20);
INSERT INTO Stock VALUES(32, 'PROD0032', 20);
INSERT INTO Stock VALUES(33, 'PROD0033', 20);
INSERT INTO Stock VALUES(34, 'PROD0034', 20);
INSERT INTO Stock VALUES(35, 'PROD0035', 20);
INSERT INTO Stock VALUES(36, 'PROD0036', 20);
INSERT INTO Stock VALUES(37, 'PROD0037', 20);
INSERT INTO Stock VALUES(38, 'PROD0038', 20);
INSERT INTO Stock VALUES(39, 'PROD0039', 20);
INSERT INTO Stock VALUES(40, 'PROD0040', 20);
INSERT INTO Stock VALUES(41, 'PROD0041', 20);
INSERT INTO Stock VALUES(42, 'PROD0042', 20);
INSERT INTO Stock VALUES(43, 'PROD0043', 20);
INSERT INTO Stock VALUES(44, 'PROD0044', 20);
INSERT INTO Stock VALUES(45, 'PROD0045', 20);
INSERT INTO Stock VALUES(46, 'PROD0046', 20);
INSERT INTO Stock VALUES(47, 'PROD0047', 20);
INSERT INTO Stock VALUES(48, 'PROD0048', 20);
INSERT INTO Stock VALUES(49, 'PROD0049', 20);
INSERT INTO Stock VALUES(50, 'PROD0050', 20);
INSERT INTO Stock VALUES(51, 'PROD0051', 20);
INSERT INTO Stock VALUES(52, 'PROD0052', 20);
INSERT INTO Stock VALUES(53, 'PROD0053', 20);
INSERT INTO Stock VALUES(54, 'PROD0054', 20);
INSERT INTO Stock VALUES(55, 'PROD0055', 20);
INSERT INTO Stock VALUES(56, 'PROD0056', 20);
INSERT INTO Stock VALUES(57, 'PROD0057', 20);
INSERT INTO Stock VALUES(58, 'PROD0058', 20);

-- STORED PROCEDURE
CREATE OR REPLACE FUNCTION deleteProduct(id_product ProductKey) RETURNS BOOLEAN  AS
$$
   BEGIN
    DELETE FROM Product WHERE product_key = id_product;
    RETURN found;  
   END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION editProduct(id_product ProductKey, new_name VARCHAR(75), new_description VARCHAR(75), new_price DECIMAL(10,2), new_category CategoryKey, new_provider ProviderKey, new_amount numeric(10)) RETURNS BOOLEAN AS 
$$    
  BEGIN
    UPDATE Product  
    SET name = new_name, description = new_description, price = new_price, category = new_category, provider = new_provider
    WHERE product_key = id_product;  
    IF found THEN
		UPDATE Stock  
        SET amount = new_amount
        WHERE product = id_product; 
        RETURN found;  
    ELSE
        RETURN found;
    END IF;
  END;
$$ LANGUAGE 'plpgsql';

CREATE OR REPLACE FUNCTION addNewEployee(emp_key EmployeeKey, email VARCHAR(75), passwrd VARCHAR(128), first_name varchar(50), last_name varchar(50), date_joined timestamp, area AreaCode, is_superuser boolean, is_areaadmin boolean, is_simplemortal boolean) RETURNS BOOLEAN AS 
$$   
  BEGIN
    IF is_superuser THEN
        INSERT INTO Employee VALUES(emp_key, email, passwrd, first_name, last_name, date_joined, area, TRUE, FALSE, FALSE);
        RETURN found;  
    ELSIF is_areadmin THEN
        IF area = 'AA' THEN
            INSERT INTO Employee VALUES('AAA01', email, passwrd, first_name, last_name, date_joined, area, FALSE, TRUE, FALSE);
            RETURN found;
        ELSIF area = 'AC' THEN
            INSERT INTO Employee VALUES('AAC01', email, passwrd, first_name, last_name, date_joined, area, FALSE, TRUE, FALSE);
            RETURN found;
        ELSE
            INSERT INTO Employee VALUES('AAV01', email, passwrd, first_name, last_name, date_joined, area, FALSE, TRUE, FALSE);
            RETURN found;
        END IF;
    ELSE
        INSERT INTO Employee VALUES(emp_key, email, passwrd, first_name, last_name, date_joined, area, FALSE, FALSE, TRUE);
        RETURN found;
    END IF;
  END;
$$ LANGUAGE 'plpgsql';

"""