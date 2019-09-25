from django.db import models

# Create your models here.
"""
-- DOMAINS
Create domain AreaCode as Varchar(5);
Create domain EmployeeKey as Varchar(5);
Create domain ClientKey as Varchar(5);

-- CREATE TABLES
Create table Area (
	area_code AreaCode NOT NULL,
	area varchar(20) NOT NULL,
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

CREATE TABLE Employee (
    emp_key EmployeeKey NOT NULL, 
    email varchar(75) NOT NULL UNIQUE, 
    password varchar(128) NOT NULL, 
    first_name varchar(50) NOT NULL, 
    last_name varchar(50) NOT NULL, 
    date_joined timestamp with time zone NOT NULL,
    area AreaCode,
    is_superuser boolean NOT NULL, 
    is_area_admin boolean NOT NULL, 
    primary key (emp_key)
) Without Oids;


* cliente
    - claveCliente
    - nombre
    - RFC
    - direccion
    - correo
    - telefono

CREATE TABLE Client (
    client_key ClientKey NOT NULL, 
    name varchar(50) NOT NULL,
    rfc varchar(128) NOT NULL UNIQUE, 
    address varchar(60) NOT NULL, 
    email varchar(75), 
    phone varchar(30), 
    primary key (client_key)
) Without Oids;

-- FOREIGN KEYS
Alter table Employee add foreign key (area) references Area (area_code) on update cascade on delete set null;
"""