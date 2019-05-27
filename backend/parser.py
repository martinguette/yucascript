from lark import Lark
import traceback
class Parser:
    def __init__(self):
        self.gramatica = """
        start: sentencias
        sentencias: sentencia sentencias | sentencia
        sentencia: sen_if | sen_for | sen_while | sen_asig | condicion | nueva_variable
        sen_if: "Siyuca" corchete_abre condicion corchete_cierra llave_abre sentencias llave_cierra
        sen_for: "parayuca" iteracion llave_abre sentencias llave_cierra
        iteracion: variable "desde" operando "hasta" numero
        sen_while: "Mientrasyuca" corchete_abre condicion corchete_cierra llave_abre sentencias llave_cierra
        sen_asig: variable signo_asig operando cierra_linea
        nueva_variable: "Nuevayuca" WORD cierra_linea | "Nuevayuca" WORD signo_asig operando cierra_linea
        signo_asig: "="
        valor: operando | operacion
        condicion: comparado comparador comparado | comparado | "!" comparado
        comparador: "==" | "<=" | ">=" | "!=" | ">" | "<"
        comparado: variable | numero | operacion
        operacion: operando operador operando
        operando: numero | variable
        operador: "+" | "-" | "*" | "/"
        corchete_abre: "{"
        corchete_cierra: "}"
        llave_abre : "["
        llave_cierra: "]"
        cierra_linea: ".."
        variable: WORD
        numero: INT
        %import common.WS
        %import common.WORD
        %import common.INT
        %ignore WS
        """
        self.parser = Lark(self.gramatica)
    def parse(self, data):
        print(data)
        try:
            response = self.parser.parse(data)
            return response
        except:
            traceback.print_exc()
            return "error"
#print(parser.parse("""
#    parayuca a desde 0 hasta 5[
#        Nuevayuca yucaxd = 5..
        
#            Nuevayuca verde=10..
#        Siyuca { a == b}[
#                Nuevayuca xd = 4..
#                Mientrasyuca { b < a}[
#                Nuevayuca dx..
#               Nuevayuca pp = a ..
                
                
#                ]
#        ]
#        Nuevayuca rucha=1..
#    ]
#"""))