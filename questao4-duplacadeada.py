"" "
Questao 4
Programe três estruturas de dados para imprimir listas de alimentos, clientes e funcionários.
* Lista Duplamente Encadeada; (incluir todos os seus desempenhos)
- Lista Linear; (incluir os seus executar)
- Lista Encadeada. (incluir seus desempenhos)
"" "
 Nó da classe :
    def  __init__ ( próprio , dado ):
        eu . value  =  dado
        eu . next  =  Nenhum
        eu . prev  =  Nenhum

classe  DuplamenteEncadeada :
    def  __init__ ( próprio , dado ):
        eu . inicio  =  Nó ( dado )
        eu . fim  =  auto . inicio

    def  append ( próprio , dado ):
        ponteiro  =  auto . inicio
        enquanto  ponteiro . next  ! =  Nenhum :
            ponteiro  =  ponteiro . Próximo

        novoNo  =  Nó ( dado )
        ponteiro . next  =  novoNo
        novoNo . prev  =  ponteiro
        eu . fim  =  novoNo

    def  insertNode ( self , dado , novoDado ):
        se  eu . fim . valor  ==  dado :
            eu . acrescentar ( novoDado )
        elif  auto . inicio . valor  ==  dado :
            novoNode  =  Nó ( novoDado )
            novoNode . next  =  self . inicio . Próximo
            novoNode . prev  =  self . inicio
            novoNode . próximo . prev  =  novoDado
            eu . inicio . next  =  novoNode
        mais :
            ponteiro  =  auto . inicio . Próximo
            enquanto  ponteiro . valor  ! =  dado :
                ponteiro  =  ponteiro . Próximo
            novoNode  =  Nó ( novoDado )
            novoNode . next  =  ponteiro . Próximo
            novoNode . próximo . prev  =  novoNode
            novoNode . prev  =  ponteiro
            ponteiro . next  =  novoNode

    def  remove ( auto , dado ):
        se  eu . inicio . valor  ==  dado :
            eu . inicio  =  self . inicio . Próximo
            eu . inicio . prev  =  Nenhum
        elif  auto . fim . valor  ==  dado :
            eu . fim  =  auto . fim . prev
            eu . fim . next  =  Nenhum
        mais :
            ponteiro  =  auto . inicio . Próximo
            enquanto  ponteiro . valor  ! =  dado :
                ponteiro  =  ponteiro . Próximo
            ponteiro . prev . next  =  ponteiro . Próximo
            ponteiro . próximo . prev  =  ponteiro . prev

    def  exibirLista ( self ):
        ponteiro  =  auto . inicio
        enquanto  ponteiro :
            print ( ponteiro . valor )
            ponteiro  =  ponteiro . Próximo



clientes  =  DuplamenteEncadeada ( "Maria" )
clientes . anexar ( "José" )
clientes . acrescentar ( "Marcos" )
clientes . acrescentar ( "Ana" )

print ( "#### Clientes ####" )
clientes . exibirLista ()
print ( "" )

clientes . remove ( "José" )
print ( "# removeu: Jose" )

clientes . acrescentar ( "João" )
print ( "# inserção: João \ n " )

print ( "#### Clientes ####" )
clientes . exibirLista ()
print ( "" )
