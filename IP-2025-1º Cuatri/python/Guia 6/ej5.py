def devolver_el_doble_si_es_par(numero: int) -> int:
    if numero % 2 == 0:
        return numero * 2
    else:
        return numero
    
def devolver_valor_si_es_par_sino_el_que_sigue(numero: int) -> int:
    if numero % 2 == 0:
        return numero
    else:
        return numero + 1

def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
    if numero % 9 == 0:
        return numero * 3
    elif numero % 3 == 0:
        return numero * 2
    else:
        return numero

def edad(edad: int, sexo: str) -> str:
    if edad <= 18:
        print("Vacaciones")
    elif sexo == "F":
        if edad >= 60:
            print("Vacaciones")
        else:
            print("A laburar")
    else:
        if edad >= 65:
            print("Vacaciones")
        else:
            print("A laburar")
