"" "
Questao 4
Programe três estruturas de dados para imprimir listas de alimentos, clientes e funcionários.
- Lista Duplamente Encadeada; (incluir todos os seus desempenhos)
- Lista Linear; (incluir os seus executar)
- Lista Encadeada. (incluir seus desempenhos)
"" "


##################################
## NÃO
 Nó da classe :
    def  __init__ ( self , dados ):
        eu . data  =  data
        eu . next  =  Nenhum

##################################
## LISTA ENCADEADA
classe  Listaencadeada :
    # contrutor
    def  __init__ ( self ):
        eu . head  =  None
        eu . _size  =  0
    #######################

    def  append ( próprio , elemento ):
        se  eu . cabeça :
            # case ja exista uma inserção add no next
            ponteiro  =  auto . cabeça
            while ( ponteiro . próximo ):
                ponteiro  =  ponteiro . Próximo
            ponteiro . next  =  Nó ( elemento )
        mais :
            # primeira insersão
            eu . head  =  Node ( elemento )

        eu . _size  =  self . _size  +  1

    def  __len__ ( próprio ):
        "Retorna tamanho da lista"
        retornar a  si mesmo . _Tamanho

    def  _getnode ( self , item ):
        ponteiro  =  auto . cabeça
        para  i  no  intervalo ( item ):
            se  ponteiro :
                ponteiro  =  ponteiro . Próximo
            mais :
                aumentar  IndexError ( ": p Listar índice fora do intervalo" )
         ponteiro de retorno

    def  __setitem__ ( self , item , newitem ):
        # lista [2] = 10
        ponteiro  =  auto . _getnode ( item )
        se  ponteiro :
            ponteiro . data  =  item
        mais :
            aumentar  IndexError ( ": p Listar índice fora do intervalo" )

    def  __getitem__ ( self , item ):
        # b = lista [2]
        ponteiro  =  auto . _getnode ( item )
        se  ponteiro :
             ponteiro de retorno . dados
        mais :
            aumentar  IndexError ( ": p Listar índice fora do intervalo" )


     índice de definição ( auto , item ):
        "" "Retorna o índice do elemento da lista" ""
        ponteiro  =  auto . cabeça
        i  =  0
        while ( ponteiro ):
            se  ponteiro . data  ==  item :
                retornar  i
            ponteiro  =  ponteiro . Próximo
            i  =  i  +  1
        raise  ValueError ( "{} não está na lista" . format ( item ))


    def  insert ( auto , índice , item ):
        node  =  Node ( item )
        se  índice  ==  0 :
            "insere no começo"
            nó . next  =  self . cabeça
            eu . head  =  node
        mais :
            "insere no fim"
            ponteiro  =  auto . _getnode ( índice - 1 )
            node  =  Node ( item )
            nó . next  =  ponteiro . Próximo
            ponteiro . next  =  nó

    def  remove ( self , item ):
        se   eu . head  ==  Nenhum :
            raise  ValueError ( "{} não está na lista" . format ( item ))
        elif  auto . cabeça . data  ==  item :
            eu . cabeça  =  eu . cabeça . Próximo
            eu . _size  =  self . _size  -  1
            return  True
        mais :
            ante  =  self . cabeça
            ponteiro  =  auto . cabeça . Próximo
            while ( ponteiro ):
                se  ponteiro . data  ==  item :
                    ante . next  =  ponteiro . Próximo
                    ponteiro . next  =  Nenhum
                ante  =  ponteiro
                ponteiro  =  ponteiro . Próximo
            eu . _size  =  self . _size  -  1
            return  True
        #error abaixo caso não exista o item na lista
        ValueError ( "{} não está na lista" . Format ( item ))


    def  __repr__ ( próprio ):
        r  =  ""
        ponteiro  =  auto . cabeça
        while ( ponteiro ):
            r  =  r  + "[" +  str ( ponteiro . dados ) + "] ->"
            ponteiro  =  ponteiro . Próximo
        retornar  r

    def  __str__ ( próprio ):
        retornar a  si mesmo . __repr__ ()


lista  =  Listaencadeada ()

# INSERE
lista . acrescentar ( "Arroz" )
lista . acrescentar ( "Feijão" )
lista . acrescentar ( "Macarrão" )
lista . acrescentar ( "Bolacha" )
print ( "Alimentos:" , lista , " \ n " )


# BUSCA
print ( "busca Bolacha:" , lista [ 3 ])

# RETIRAR
lista . remover ( 2 )
print ( "remover Bolacha:" , lista . remover ( "Bolacha" ))

# INSERE ALIMENTOS EM ALGUMA POSICAO
lista . inserção ( 2 , "Refrigerante" )
print ( "inserção ['Refrigerante'] na posição [2]" )
print ( " \ n Alimentos:" , lista )
