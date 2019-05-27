from lark import Lark

gramatica = """
    start: sentencias
    sentencias: sentencia sentencias | sentencia
    sentencia: sen_if | sen_for | sen_while | sen_asig | condicion
    sen_if: "Syuca" corchete_abre condicion corchete_cierra llave_abre sentencias llave_cierra
    sen_for: "Fyuca" condicion llave_abre sentencias llave_cierra
    sen_while: "Myuca" corchete_abre condicion corchete_cierra llave_abre sentencias llave_cierra
    sen_asig: "nuevayuca" WORD signo_asig valor cierra_linea
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
    Myuca {a<b}[
        nuevayuca sssss..
        Syuca{b}[
            nuevayuca verde..
        ]
        nuevayuca rucha..
    ]
"""))