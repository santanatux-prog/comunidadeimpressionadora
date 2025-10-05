from comunidadeimpressionadora import app, database
from comunidadeimpressionadora.models import Usuario

# Criar o banco de dados
# with app.app_context():
#     database.create_all()


# Criar o usuários
# with app.app_context():
#     usuario1 = Usuario(username='Santana', email='santana.tux@gmail.com', senha='123456')
#     usuario2 = Usuario(username='Joao', email='joao@gmail.com', senha='123456')
#     database.session.add(usuario1)
#     database.session.add(usuario2)
#
#     database.session.commit()

# Consultar tabela Usuario
with app.app_context():
    meus_usuarios = Usuario.query.all()
    print(meus_usuarios)
    primeiro_usuario = Usuario.query.first()
    print(primeiro_usuario.id)
    print(primeiro_usuario.username)
    print(primeiro_usuario.email)
    print(primeiro_usuario.senha)


# Consultar tabela Usuario com filtros
# with app.app_context():
#     usuarios_teste = Usuario.query.filter_by(id=2).all()
#     print(usuarios_teste)

# Consultar tabela Usuario com filtros
# with app.app_context():
#     usuarios_teste = Usuario.query.filter_by(username='Santana').first()
#     print(usuarios_teste)
#     print(usuarios_teste.email)

# Criar uma postagem
# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo='Meu primeiro post', corpo='Olá! esse é minha primeira postagem de teste. Ficou legal?')
#     database.session.add(meu_post)
#     database.session.commit()

# Consultar tabela Post
# with app.app_context():
#     post_teste = Post.query.filter_by(id_usuario=1).first()
#     print(post_teste.corpo)
#     print(post_teste.autor.username)

# Deleta e Cria um novo banco
# with app.app_context():
#     #database.drop_all()
#     database.create_all()