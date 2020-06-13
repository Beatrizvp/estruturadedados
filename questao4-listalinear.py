"" "
Questao 4
Programe três estruturas de dados para imprimir listas de alimentos, clientes e funcionários.
- Lista Duplamente Encadeada; (incluir todos os seus desempenhos)
* Lista Linear; (incluir os seus executar)
- Lista Encadeada. (incluir seus desempenhos)
Uma lista linear que usa uma pilha
"" "


##################################
## NÃO
 Nó da classe :
    def  __init__ ( self , dados ):
        eu . data  =  data
        eu . next  =  Nenhum

classe  ListaLinear :
    #contrutor
    def  __init__ ( self ):
        eu . top  =  Nenhum
        eu . _size  =  0
    #######################

    #insere
    def  push ( auto , elem ):
        nó  =  nó ( elem )
        nó . next  =  self . topo
        eu . top  =  nó
        eu . _size  =  self . _size  +  1
        retornar  "Insere:" + nó . dados

    #remove (parte superior)
    def  pop ( auto ):
        se  eu . _size  >  0 : #ser uma lista tiver vazia não executada
            nó  =  auto . topo
            eu . top  =  self . top . Próximo
            eu . _size  =  self . _size  -  1
            retorne  "Removeu:" + nó . dados
        mais :
            raise  IndexError ( "A lista está vazia :(" )

    #observar topo
    def  peek ( auto ):
        se  eu . _size  >  0 : #ser uma lista tiver vazia não executada
            retornar a  si mesmo . top . dados
        mais :
            raise  IndexError ( "A lista está vazia :(" )

    #retorna tamnaho
    def  __len__ ( próprio ):
        retornar a  si mesmo . _Tamanho
    def  len ( self ):
        retornar a  si mesmo . __len__ ()

    #exibir
    def  __repr__ ( próprio ):
        r  =  ""
        ponteiro  =  auto . topo
        while ( ponteiro ):
            r  =  r  + "[" +  str ( ponteiro . dados ) + "] \ n "
            ponteiro  =  ponteiro . Próximo
        retornar  r

    #exibir como string
    def  __str__ ( próprio ):
        retornar a  si mesmo . __repr__ ()


############################
## TESTE
lista  =  ListaLinear ()

#insere
lista . push ( "Auxiliar" )
lista . push ( "Operador" )
lista . push ( "Supervisor" )
lista . push ( "Lider" )
print ( " \ n ##################################" )
print ( "Funcionarios:" , lista . len ())
imprimir ( lista )

# RETIRAR
print ( lista . pop ())

# Insere
print ( lista . push ( "Diretor" ))
print ( lista . push ( "Almoxarife" ))

print ( " \ n ##################################" )
print ( "Funcionarios:" , lista . len ())
imprimir ( lista )
