DROP SCHEMA IF EXISTS accounts CASCADE;

CREATE SCHEMA accounts;

CREATE ROLE postgres;

ALTER SCHEMA accounts OWNER TO postgres;

--
-- For playing, debugging and analytics
--
CREATE USER debugger WITH PASSWORD 'debugger';
GRANT CONNECT on DATABASE accounts TO debugger;

--
-- For gpbuworker only
--
-- CREATE USER gpbuworker WITH PASSWORD 'gpbuworker';
-- GRANT CONNECT on DATABASE accounts TO gpbuworker;

GRANT USAGE on SCHEMA accounts TO debugger;

GRANT USAGE on SCHEMA accounts TO gpbuworker;

SET search_path TO accounts;

--
SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;
--



DROP TABLE IF EXISTS accounts.accounts CASCADE;

CREATE TABLE accounts.accounts (
	acc_id int4 NOT NULL,
	clnt_id int4 NULL,
	"Account_num" int4 NULL,
	CONSTRAINT "Accounts_pkey" PRIMARY KEY (acc_id)
);


DROP TABLE IF EXISTS accounts.balances CASCADE;

CREATE TABLE accounts.balances (
	id_bln int4 NOT NULL,
	acc_id int4 NULL,
	"date" date NULL,
	sum float4 NULL,
	CONSTRAINT "Balances_pkey" PRIMARY KEY (id_bln)
);


DROP TABLE IF EXISTS accounts.clients CASCADE;

CREATE TABLE accounts.clients (
	"Id_clnt" int4 NOT NULL,
	"Clients_FIO" name NULL COLLATE "C",
	CONSTRAINT "Clients_pkey" PRIMARY KEY ("Id_clnt")
);


DROP TABLE IF EXISTS accounts.account CASCADE;

CREATE TABLE accounts.account (
	account_id varchar NOT NULL,
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE),
	balanse_value int4 NULL,
	date_update date NOT NULL
);


DROP TABLE IF EXISTS accounts.user_table CASCADE;

CREATE TABLE accounts.user_table (
	user_name varchar NOT NULL,
	email varchar NOT NULL,
	user_password varchar NOT NULL,
	account_id varchar NOT NULL,
	date_add date NOT NULL,
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY( INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE)
);


CREATE UNIQUE INDEX "Accounts_pkey" ON accounts.accounts USING btree (acc_id);

CREATE UNIQUE INDEX "Balances_pkey" ON accounts.balances USING btree (id_bln);

CREATE UNIQUE INDEX "Clients_pkey" ON accounts.clients USING btree ("Id_clnt");


DROP SEQUENCE accounts.account_id_seq;

CREATE SEQUENCE accounts.account_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;

CREATE SEQUENCE accounts.user_table_id_seq
	INCREMENT BY 1
	MINVALUE 1
	MAXVALUE 2147483647
	START 1
	CACHE 1
	NO CYCLE;


GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA accounts TO debugger;

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA accounts TO debugger;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA accounts TO gpbuworker;

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA accounts TO gpbuworker;
