-- Table: public.tc_tipo_tabla

-- DROP TABLE IF EXISTS public.tc_tipo_tabla;

CREATE TABLE IF NOT EXISTS public.tc_tipo_tabla
(
    id_tipo_tabla character varying(4) COLLATE pg_catalog."default" NOT NULL,
    desc_tipo_tabla character varying(120) COLLATE pg_catalog."default" NOT NULL,
    usuario character varying(25) COLLATE pg_catalog."default" NOT NULL,
    actualizacion date NOT NULL,
    CONSTRAINT tc_tipo_tabla_pkey PRIMARY KEY (id_tipo_tabla)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tc_tipo_tabla
    OWNER to postgres;

-- Table: public.tc_ispt

-- DROP TABLE IF EXISTS public.tc_ispt;

CREATE TABLE IF NOT EXISTS public.tc_ispt
(
    id integer NOT NULL DEFAULT nextval('sq_ispt'::regclass),
    ispt_fin date NOT NULL,
    ispt_ini date NOT NULL,
    id_tipo_tabla character varying(4) COLLATE pg_catalog."default" NOT NULL,
    ispt_consec integer NOT NULL,
    ispt_lim_inf1 double precision NOT NULL,
    ispt_lim_inf2 double precision NOT NULL,
    ispt_lim_superior double precision NOT NULL,
    ispt_sueldo_bruto1 double precision NOT NULL,
    ispt_sueldo_bruto2 double precision NOT NULL,
    ispt_cuota_fija double precision NOT NULL,
    ispt_excedente double precision NOT NULL,
    ispt_subsidio double precision NOT NULL,
    usuario character varying(25) COLLATE pg_catalog."default" NOT NULL,
    actualizacion date NOT NULL,
    CONSTRAINT tc_ispt_pk PRIMARY KEY (id),
    CONSTRAINT fk_tc_ispt_01 FOREIGN KEY (id_tipo_tabla)
        REFERENCES public.tc_tipo_tabla (id_tipo_tabla) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.tc_ispt
    OWNER to postgres;

-- Index: ix_tc_ispt_01

-- DROP INDEX IF EXISTS public.ix_tc_ispt_01;

CREATE INDEX IF NOT EXISTS ix_tc_ispt_01
    ON public.tc_ispt USING btree
    (id_tipo_tabla COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
