# DIVISÃO

frase = 'Curso em vídeo Python'

# para dividir a string na região dos espaços podemos usar split. Todas as palavras são basicamente inseridas em listas
print(frase.split())

# JUNÇÃO
# insere o caractere entre aspa no meio de cada caractere da frase
print('-'.join(frase))
# para substituir os espaços por traços, por exemplo, podemos usar as duas funções acima em conjunto
print('-'.join(frase.split()))

# caso queira colar um texto inteiro, pulando linhas e formatando do seu jeito, utilize aspas triplas com o print
print("""Python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[30]""")