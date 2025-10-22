q_tablas_ispt = '''
    select  id_tipo_tabla as tipo_tabla, 
            ispt_lim_inf1 as limite_inferior, 
            ispt_lim_superior as limite_superior,  
            ispt_sueldo_bruto2 as bruto, 
            ispt_cuota_fija as cuota_fija, 
            ispt_excedente as excedente
    from    tc_ispt
    where   ispt_fin = '2099-01-01'
    order by id_tipo_tabla, ispt_consec
'''

