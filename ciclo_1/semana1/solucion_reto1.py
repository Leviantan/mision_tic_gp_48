def CDT(usuario: str, capital: int, tiempo: int):
    porcentaje_interes = 0.03
    porcentaje_aperder = 0.02

    if (tiempo > 2):
        valor_inte = (capital * porcentaje_interes * tiempo) / 12
        valor_total = capital + valor_inte
    else:
        valor_aperder = capital * porcentaje_aperder
        valor_total = capital - valor_aperder
    
    return f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}"  
    
print(CDT("AB1012",1000000,3))