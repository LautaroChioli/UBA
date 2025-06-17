-- Ejercicio 3. Implementar una función estanRelacionados :: Integer -> Integer -> Bool
-- tal que
-- problema estanRelacionados (a : Z, b : Z) : Bool {
-- requiere: {a ̸= 0 ∧ b ̸= 0}
-- asegura: {(res = true) ↔ (a ∗ a + a ∗ b ∗ k = 0 para algún k ∈ Z con k ̸= 0)}

esMultiploDe :: Int -> Int -> Bool
esMultiploDe n m 
    |mod n m == 0 = True
    | otherwise = False

estanRelacionados :: Int -> Int -> Bool
estanRelacionados n m -- z = (-a**2)/ab => z = -a/b
    | n == 0 || m == 0 = False
    | mod n m == 0 = True
    | otherwise = False
