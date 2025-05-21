# Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo
# actual. Asumir que el saldo inicial es 0. Las tuplas tienen una letra que nos indica el tipo de movimiento “I” para ingreso
# de dinero y “R” para retiro de dinero, y adem´as el monto de cada operaci´on. Por ejemplo, si la lista de tuplas es [(‘‘I’’,
# 2000), (‘‘R’’, 20),(‘‘R’’, 1000),(‘‘I’’, 300)] entonces el saldo actual es 1280.
# problema saldoActual (in movimientos: seq⟨Char × Z⟩) : Z {
# requiere: { Para todo i ∈ Z si 0 ≤ i < |movimientos| → movimientos[i]0 ∈ {“I”,“R”} y movimientos[i]1 > 0 }
# asegura: { res =
# Pingresos
# i movimientos[i]1 −
# Pretiros
# i movimientos[i]1 }
# }

def saldo_actual(movimientos: list) -> int:
    saldo_inicial: int= 0
    for movimiento in movimientos:
        saldo_inicial += transaccion(movimiento)
    return saldo_inicial

def transaccion(transaccion: tuple) -> int:
    if transaccion[0] == 'I':
        return transaccion[1]
    return  (-transaccion[1])
    
