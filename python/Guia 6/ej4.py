def peso_pino(cm: int) -> int:
    if cm <= 300:
        return 3 * cm
    else:
        hasta_300cm = cm - 300
        return (900 + hasta_300cm*2)
    
def es_peso_util(peso: int) -> bool:
    return (peso >= 400 and peso <= 1000)

def sirve_pino(cm: int) -> bool:
    return es_peso_util(peso_pino(cm))

