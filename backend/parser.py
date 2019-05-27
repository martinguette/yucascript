from lark import Lark

gramatica = """
    start: sentencias
    sentencias: sentencia sentencias | sentencia
    sentencia: sen_if | sen_for | sen_while | sen_asig | condicion
    sen_if: "Siyuca" corchete_abre condicion corchete_cierra llave_abre sentencias llave_cierra
    sen_for: "parayuca" iteracion llave_abre sentencias llave_cierra
    iteracion: variable "numero" operando "hasta" numero
    sen_while: "Mientrasyuca" corchete_abre condicion corchete_cierra llave_abre sentencias llave_cierra
    sen_asig: "Nuevayuca" WORD signo_asig valor cierra_linea
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

parser = Lark(gramatica)
print(parser.parse("""
    Mientrasyuca {a<b}[
        Nuevayuca yucaxd = 5..
        Siyuca{b}[
            Nuevayuca verde=10..
        ]
        Nuevayuca rucha=1..
    ]
"""))