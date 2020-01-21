class book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        print('Constructor called to create a object from this class.')

    def printer(self, title, isbn):
        print(f'This is the book {title} and the {isbn} ISBN.')


# Criando o objeto Livro2 que é uma instância da classe Livro
livro = book('A Menina que Roubava Livros', 77886611)

print(livro.title)