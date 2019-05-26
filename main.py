from Parser import Parser


parser = Parser()


texto = """
    siyuca (){
        siyuca(){
            siyuca(){
            siyuca(){
            }
            siyuca(){
            }
            siyuca(){
            }
            }
        }
    }

"""

print( parser.compile(texto) )