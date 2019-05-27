from lark import Lark

gramatica = """
    start: sentencias
    sentencias: sentencia sentencias | sentencia
    sentencia: sen_if | sen_for | sen_while | sen_asig | condicion
    sen_if: "Syuca" corchete_abre condicion corchete_cierra llave_abre sentencias llave_cierra
    sen_for: "Fyuca" condicion llave_abre sentencias llave_cierra
    sen_while: "Myuca" corchete_abre condicion corchete_cierra llave_abre sentencias llave_cierra
    sen_asig: "nuevayuca" cierra_linea
    condicion: WORD comparador WORD | WORD | "!" WORD 
    comparador: "==" | "<=" | ">=" | "!=" | ">" | "<"
    corchete_abre: "{"
    corchete_cierra: "}"
    llave_abre : "["
    llave_cierra: "]"
    cierra_linea: ".."
    %import common.WS
    %import common.WORD
    %import common.INT
    %ignore WS
    """

parser = Lark(gramatica)
print(parser.parse("""
    Myuca {a<b}[
        sssss..
        Syuca{b}[
            verde..
        ]
        eeeee..
    ]
"""))