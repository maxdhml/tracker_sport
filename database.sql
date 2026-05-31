-- Sauvergarde de la base de données

\restrict ED89ayOSVaMngSI2H5gojvKr2mDc2O5R86KQHMyyzLjt1IY2rPQ2zh3euLDUXvK

-- Dumped from database version 15.17 (Debian 15.17-1.pgdg13+1)
-- Dumped by pg_dump version 15.17 (Debian 15.17-1.pgdg13+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: exercice; Type: TABLE; Schema: public; Owner: athlete
--

CREATE TABLE public.exercice (
    id integer NOT NULL,
    nom character varying(100) NOT NULL,
    code character varying(20) NOT NULL,
    niveau_maitrise integer NOT NULL,
    groupe_id integer NOT NULL
);


ALTER TABLE public.exercice OWNER TO athlete;

--
-- Name: exercice_id_seq; Type: SEQUENCE; Schema: public; Owner: athlete
--

CREATE SEQUENCE public.exercice_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.exercice_id_seq OWNER TO athlete;

--
-- Name: exercice_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: athlete
--

ALTER SEQUENCE public.exercice_id_seq OWNED BY public.exercice.id;


--
-- Name: groupe_musculaire; Type: TABLE; Schema: public; Owner: athlete
--

CREATE TABLE public.groupe_musculaire (
    id integer NOT NULL,
    nom character varying(100) NOT NULL,
    code character varying(20) NOT NULL,
    programme_id integer NOT NULL
);


ALTER TABLE public.groupe_musculaire OWNER TO athlete;

--
-- Name: groupe_musculaire_id_seq; Type: SEQUENCE; Schema: public; Owner: athlete
--

CREATE SEQUENCE public.groupe_musculaire_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.groupe_musculaire_id_seq OWNER TO athlete;

--
-- Name: groupe_musculaire_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: athlete
--

ALTER SEQUENCE public.groupe_musculaire_id_seq OWNED BY public.groupe_musculaire.id;


--
-- Name: programme; Type: TABLE; Schema: public; Owner: athlete
--

CREATE TABLE public.programme (
    id integer NOT NULL,
    nom character varying(100) NOT NULL,
    code character varying(20) NOT NULL
);


ALTER TABLE public.programme OWNER TO athlete;

--
-- Name: programme_id_seq; Type: SEQUENCE; Schema: public; Owner: athlete
--

CREATE SEQUENCE public.programme_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.programme_id_seq OWNER TO athlete;

--
-- Name: programme_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: athlete
--

ALTER SEQUENCE public.programme_id_seq OWNED BY public.programme.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: athlete
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    username character varying(50) NOT NULL,
    password_hash character varying(255) NOT NULL
);


ALTER TABLE public."user" OWNER TO athlete;

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: athlete
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO athlete;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: athlete
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: exercice id; Type: DEFAULT; Schema: public; Owner: athlete
--

ALTER TABLE ONLY public.exercice ALTER COLUMN id SET DEFAULT nextval('public.exercice_id_seq'::regclass);


--
-- Name: groupe_musculaire id; Type: DEFAULT; Schema: public; Owner: athlete
--

ALTER TABLE ONLY public.groupe_musculaire ALTER COLUMN id SET DEFAULT nextval('public.groupe_musculaire_id_seq'::regclass);


--
-- Name: programme id; Type: DEFAULT; Schema: public; Owner: athlete
--

ALTER TABLE ONLY public.programme ALTER COLUMN id SET DEFAULT nextval('public.programme_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: athlete
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Data for Name: exercice; Type: TABLE DATA; Schema: public; Owner: athlete
--

COPY public.exercice (id, nom, code, niveau_maitrise, groupe_id) FROM stdin;
1	Rowing Barre	ROW-BAR	3	2
2	Tirage Vertical	TIR-VER	4	2
3	Tirage Horizontal	TIR-HOR	3	2
4	Table Lombaire	TAB-LOM	4	2
5	Curl Biceps Poulie Barre Droite	CUR-BIC-POU-BAR-DRO	3	2
6	Curl Marteau Poulie Corde	CUR-MAR-POU-COR	3	2
7	D├®velopp├® couch├®	DEV-COU	5	1
8	D├®velopp├® Inclin├®	DEV-INC	2	1
9	Butterfly	BUT	3	1
10	Triceps Poulie Haute	TRI-POU-HAU	3	1
11	Triceps Poulie Basse	TRI-POU-BAS	3	1
12	Elevation lat├®rale	ELE-LAT	1	1
\.


--
-- Data for Name: groupe_musculaire; Type: TABLE DATA; Schema: public; Owner: athlete
--

COPY public.groupe_musculaire (id, nom, code, programme_id) FROM stdin;
1	Pectoraux / Triceps	PEC-TRI	1
2	Dos / Biceps	DOS-BIC	1
\.


--
-- Data for Name: programme; Type: TABLE DATA; Schema: public; Owner: athlete
--

COPY public.programme (id, nom, code) FROM stdin;
1	S├¿che ├ët├® 2026	SEC-26
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: athlete
--

COPY public."user" (id, username, password_hash) FROM stdin;
1	admin	scrypt:32768:8:1$sK98dwR5JWNVIOQB$07075ce08b12b851a03edaadae6fd2f99ca48568e4a186e8d37f0268d4295b55d69abdf13e38fc8898e68c0e52d367e902a6d31bf7189c6a7b88d078f8942b8e
\.


--
-- Name: exercice_id_seq; Type: SEQUENCE SET; Schema: public; Owner: athlete
--

SELECT pg_catalog.setval('public.exercice_id_seq', 12, true);


--
-- Name: groupe_musculaire_id_seq; Type: SEQUENCE SET; Schema: public; Owner: athlete
--

SELECT pg_catalog.setval('public.groupe_musculaire_id_seq', 2, true);


--
-- Name: programme_id_seq; Type: SEQUENCE SET; Schema: public; Owner: athlete
--

SELECT pg_catalog.setval('public.programme_id_seq', 1, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: athlete
--

SELECT pg_catalog.setval('public.user_id_seq', 1, true);


--
-- Name: exercice exercice_code_key; Type: CONSTRAINT; Schema: public; Owner: athlete
--

ALTER TABLE ONLY public.exercice
    ADD CONSTRAINT exercice_code_key UNIQUE (code);


--
-- Name: exercice exercice_pkey; Type: CONSTRAINT; Schema: public; Owner: athlete
--

ALTER TABLE ONLY public.exercice
    ADD CONSTRAINT exercice_pkey PRIMARY KEY (id);


--
-- Name: groupe_musculaire groupe_musculaire_code_key; Type: CONSTRAINT; Schema: public; Owner: athlete
--

ALTER TABLE ONLY public.groupe_musculaire
    ADD CONSTRAINT groupe_musculaire_code_key UNIQUE (code);


--
-- Name: groupe_musculaire groupe_musculaire_pkey; Type: CONSTRAINT; Schema: public; Owner: athlete
--

ALTER TABLE ONLY public.groupe_musculaire
    ADD CONSTRAINT groupe_musculaire_pkey PRIMARY KEY (id);


--
-- Name: programme programme_code_key; Type: CONSTRAINT; Schema: public; Owner: athlete
--

ALTER TABLE ONLY public.programme
    ADD CONSTRAINT programme_code_key UNIQUE (code);


--
-- Name: programme programme_pkey; Type: CONSTRAINT; Schema: public; Owner: athlete
--

ALTER TABLE ONLY public.programme
    ADD CONSTRAINT programme_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: athlete
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: user user_username_key; Type: CONSTRAINT; Schema: public; Owner: athlete
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_username_key UNIQUE (username);


--
-- Name: exercice exercice_groupe_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: athlete
--

ALTER TABLE ONLY public.exercice
    ADD CONSTRAINT exercice_groupe_id_fkey FOREIGN KEY (groupe_id) REFERENCES public.groupe_musculaire(id);


--
-- Name: groupe_musculaire groupe_musculaire_programme_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: athlete
--

ALTER TABLE ONLY public.groupe_musculaire
    ADD CONSTRAINT groupe_musculaire_programme_id_fkey FOREIGN KEY (programme_id) REFERENCES public.programme(id);


--
-- PostgreSQL database dump complete
--

\unrestrict ED89ayOSVaMngSI2H5gojvKr2mDc2O5R86KQHMyyzLjt1IY2rPQ2zh3euLDUXvK

