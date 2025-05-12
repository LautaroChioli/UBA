import Asd
import Test.HUnit

main = runTestTT allTests

allTests = test[
    "similAnagrama palabra1 vacia" ~: similAnagrama [] ['a']  ~?= False,
    "similAnagrama palabra2 vacia" ~: similAnagrama ['x'] []  ~?= False,
    "similAnagrama |palabra1| = |palabra2| solo espacios blancos no es similAnagrama" ~: similAnagrama "  " "  "  ~?= False,
    "similAnagrama Falso porque son identicos" ~: similAnagrama ['a', 'a', 'a', 'a'] ['a', 'a', 'a', 'a']  ~?= False,
    "similAnagrama Falso porque tienen diferentes caracteres" ~: similAnagrama ['a', 'B', 'C', '-'] ['a', 'b', 'c', '-']  ~?= False,
    "similAnagrama True sin espacios" ~: similAnagrama ['a', 'b', 'c', 'd'] ['d', 'a', 'b', 'c']  ~?= True,
    "similAnagrama True con espacios en mismo lugar" ~: similAnagrama [' ', 'a', 'b', 'c', 'd'] [' ', 'd', 'a', 'b', 'c']  ~?= True,
    "similAnagrama True con espacios en distinto lugar" ~: similAnagrama ['a', ' ', 'b', 'c', 'd'] [' ', 'd', 'a', 'b', 'c']  ~?= True,
    "similAnagrama palabras con un elementro, False" ~: similAnagrama ['a'] ['b']  ~?= False,
    "similAnagrama True con espacios en diferente posicion" ~: similAnagrama [' ', 'a'] ['a', ' ']  ~?= True,
    "similAnagrama True varias apariciones sin espacio"  ~: similAnagrama "aabbcc" "abcabc"  ~?= True,
    "similAnagrama True varias apariciones con misma cant de espacio"  ~: similAnagrama "aab bcc" "abcab c"  ~?= True,
    "similAnagrama True varias apariciones con distina cant de espacio"  ~: similAnagrama "aab bcc" "   a b cab c"  ~?= True,
    "similAnagrama Falso palabra1 contenida en palabra2"  ~: similAnagrama "abc" "abcdd"  ~?= False,
    "similAnagrama Falso palabra2 contenida en palabra1"  ~: similAnagrama "abcde" "ab"  ~?= False
    ]