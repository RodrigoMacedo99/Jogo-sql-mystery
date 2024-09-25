import sqlite3
def criar_tabelas():
    # Conectando ao banco de dados
    banco = sqlite3.connect('cimatec_IA.db')
    
    # Definindo o cursor
    cursor = banco.cursor()
    
    # Criando a tabela de suspeitos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS suspeitos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome TEXT NOT NULL,
        Cargo_Cimatec TEXT NOT NULL,
        Especializacao TEXT NOT NULL
    )
    ''')
    
    # Criando a tabela de Acesso_Laboratorio
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Acesso_Laboratorio (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome_Laboratorio TEXT NOT NULL,
        Horario_Entrada TEXT NOT NULL,
        Horario_Saida TEXT NOT NULL,
        Nivel_Acesso TEXT NOT NULL,
        fk_pessoa INTEGER,
        FOREIGN KEY (fk_pessoa) REFERENCES suspeitos(ID)
    )
    ''')
    
    # Criando a tabela de Arquivos_Projetos
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Arquivos_Projetos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nome_Arquivo TEXT NOT NULL,
        Horario_Modificacao TEXT NOT NULL,
        Data_Modificacao TEXT NOT NULL,
        Area_Modificada TEXT NOT NULL,
        Responsavel_fk INTEGER,
        FOREIGN KEY (Responsavel_fk) REFERENCES suspeitos(ID)
    )
    ''')
    
    # Criando a tabela de email_corporacao
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS email_corporacao (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Mensagem TEXT NOT NULL,
        Horario TEXT NOT NULL
    )
    ''')
    
    banco.commit()
    banco.close()

# Chamar a função para criar as tabelas
criar_tabelas()
def inserir_dados():
    # Conectando ao banco de dados
    banco = sqlite3.connect('nome_do_banco.db')
    
    # Definindo o cursor
    cursor = banco.cursor()
    
    # Tabela para suspeitos
    # Inserindo Flavia na tabela suspeitos
    cursor.execute("INSERT INTO suspeitos (Nome, Cargo_Cimatec, Especializacao) VALUES (?, ?, ?)",
                   ('Flavia', 'Pesquisadora', 'Visão Computacional'))
    cursor.execute("INSERT INTO Acesso_Laboratorio (Nome_Laboratorio, Horario_Entrada, Horario_Saida, Nivel_Acesso, fk_pessoa) VALUES (?, ?, ?, ?, ?)",
                   ('LAB-Robotica', '13:00', '17:00', 'Baixa', 5))  # Supondo que Flavia tenha o ID 5
    cursor.execute("INSERT INTO Arquivos_Projetos (Nome_Arquivo, Horario_Modificacao, Data_Modificacao, Area_Modificada, Responsavel_fk) VALUES (?, ?, ?, ?, ?)",
                   ('IA - v3.2', '16:00', '2024-09-01', 'Inteligencia Artificial', 5))  # Supondo que Flavia tenha o ID 5

    # Inserindo mais suspeitos
    cursor.execute("INSERT INTO suspeitos (Nome, Cargo_Cimatec, Especializacao) VALUES (?, ?, ?)",
                   ('Adriana', 'Engenheira de Software', 'Lógica de Decisão'))
    cursor.execute("INSERT INTO suspeitos (Nome, Cargo_Cimatec, Especializacao) VALUES (?, ?, ?)",
                   ('Renata', 'Cientista de Dados', 'Visão Computacional'))
    cursor.execute("INSERT INTO suspeitos (Nome, Cargo_Cimatec, Especializacao) VALUES (?, ?, ?)",
                   ('Lucas', 'Engenheiro de Robótica', 'Comandos Autônomos'))
    cursor.execute("INSERT INTO suspeitos (Nome, Cargo_Cimatec, Especializacao) VALUES (?, ?, ?)",
                   ('Gustavo', 'Gerente de Projetos', 'Coordenação'))

    # Inserindo mais acessos ao laboratório
    cursor.execute("INSERT INTO Acesso_Laboratorio (Nome_Laboratorio, Horario_Entrada, Horario_Saida, Nivel_Acesso, fk_pessoa) VALUES (?, ?, ?, ?, ?)",
                   ('LAB-IA', '09:00', '12:00', 'Alta', 2)) 
    cursor.execute("INSERT INTO Acesso_Laboratorio (Nome_Laboratorio, Horario_Entrada, Horario_Saida, Nivel_Acesso, fk_pessoa) VALUES (?, ?, ?, ?, ?)",
                   ('LAB-Visao', '10:00', '14:00', 'Média', 3)) 
    cursor.execute("INSERT INTO Acesso_Laboratorio (Nome_Laboratorio, Horario_Entrada, Horario_Saida, Nivel_Acesso, fk_pessoa) VALUES (?, ?, ?, ?, ?)",
                   ('LAB-Robotica', '11:00', '15:00', 'Alta', 4)) 

    # Inserindo mais arquivos de projetos
    cursor.execute("INSERT INTO Arquivos_Projetos (Nome_Arquivo, Horario_Modificacao, Data_Modificacao, Area_Modificada, Responsavel_fk) VALUES (?, ?, ?, ?, ?)",
                   ('Projeto_Visao_v1', '11:30', '2024-09-05', 'Visão Computacional', 3))  
    cursor.execute("INSERT INTO Arquivos_Projetos (Nome_Arquivo, Horario_Modificacao, Data_Modificacao, Area_Modificada, Responsavel_fk) VALUES (?, ?, ?, ?, ?)",
                   ('Projeto_Robotica_v3', '15:00', '2024-09-12', 'Robótica', 4))  

    # Tabela para email_corporacao
    cursor.execute("INSERT INTO email_corporacao (Mensagem, Horario) VALUES (?, ?)",
                   ('''Equipe,

                   Conforme combinado, a atualização da nossa IA de reconhecimento de padrões e tomada de decisão (versão 3.2) está programada para o dia 21 de setembro. O código em Ruby ainda precisa de alguns ajustes para garantir a compatibilidade com o módulo de visão computacional.
                   
                   Adriana, você poderia verificar se a sua parte relacionada à lógica de decisão está dentro do cronograma? Precisamos garantir que tudo estará pronto até o dia 20 para que possamos rodar os testes finais.
                   
                   Lembrem-se de que nenhuma modificação deve ser feita na IA até a data acordada.
                   
                   Att., Gustavo''', '2024-09-15 11:00'))

    cursor.execute("INSERT INTO Arquivos_Projetos (Nome_Arquivo, Horario_Modificacao, Data_Modificacao, Area_Modificada, Responsavel_fk) VALUES (?, ?, ?, ?, ?)",
                   ('Projeto_Robotica_v2', '14:45', '2024-09-10', 'Mecânica', 2))

    cursor.execute("INSERT INTO email_corporacao (Mensagem, Horario) VALUES (?, ?)",
                   ('''Oi, Gustavo,

                   Estou terminando de ajustar a lógica de decisão na IA. O código está 80% finalizado e pretendo concluir tudo até o dia 19 de setembro. Acredito que podemos rodar os testes no dia 20, como planejado.

                   É importante frisar que, se alguém alterar o código antes dessa data, corremos o risco de desestabilizar a IA e, consequentemente, o sistema de reconhecimento de padrões e a integração com o módulo de visão. Vamos garantir que tudo permaneça intocado até estarmos prontos para o rollout no dia 21.

                   Abs, Adriana''', '2024-09-16 10:00'))

    cursor.execute("INSERT INTO email_corporacao (Mensagem, Horario) VALUES (?, ?)",
                   ('''Pessoal,

                   Tudo certo da minha parte para a integração da visão computacional com a IA. Estarei disponível nos dias 19 e 20 para fazer os testes finais, conforme o planejamento.

                   Lembrando que qualquer alteração na IA antes do dia 21 sem autorização pode comprometer todo o processo de reconhecimento visual. Precisamos evitar isso a todo custo.

                   Abraços, Renata''', '2024-09-10 16:00'))

    cursor.execute("INSERT INTO email_corporacao (Mensagem, Horario) VALUES (?, ?)",
                   ('''Oi, equipe,

                   Só para garantir, vou revisar a integração da IA com os robôs até o dia 20 de setembro. Precisamos manter a agenda para evitar problemas de sincronização entre a IA e os comandos do robô. Qualquer mudança no código agora pode gerar falhas no comportamento autônomo do robô.

                   Vou reforçar que nenhuma modificação deve ser feita até que todos nós estejamos prontos para lançar a versão final no dia 21.

                   Abs, Lucas''', '2024-09-09 09:00'))

    cursor.execute("INSERT INTO email_corporacao (Mensagem, Horario) VALUES (?, ?)",
                   ('''Pessoal,

                   Gostaria de reforçar que a atualização da IA, versão 3.2, NÃO está autorizada para ser realizada antes do dia 21 de setembro. Não houve nenhuma mudança no cronograma, e qualquer modificação anterior à data pode gerar sérios problemas no reconhecimento de padrões e na integração com os robôs e a visão computacional.

                   Se alguém perceber algo fora do planejado, por favor, me avise imediatamente.

                   Obrigado, Gustavo''', '2024-09-08 08:00'))

    # Inserindo mais emails
    cursor.execute("INSERT INTO email_corporacao (Mensagem, Horario) VALUES (?, ?)",
                   ('''Oi, equipe,

                   Estou revisando a documentação do projeto e percebi que precisamos atualizar alguns detalhes sobre a integração com o módulo de visão. Vou fazer isso até o dia 18 de setembro.

                   Por favor, não façam nenhuma alteração no código até que eu termine essa revisão.

                   Abs, Flavia''', '2024-09-07 14:00'))

    cursor.execute("INSERT INTO email_corporacao (Mensagem, Horario) VALUES (?, ?)",
                   ('''Equipe,

                   A integração com o módulo de visão está quase finalizada. Precisamos garantir que todos os testes sejam feitos até o dia 20 de setembro para evitar problemas no lançamento.

                   Lembrem-se de que qualquer modificação no código deve ser comunicada a todos.

                   Att., Renata''', '2024-09-06 09:00'))

    banco.commit()
    # Inserindo mais emails
    cursor.execute("INSERT INTO email_corporacao (Mensagem, Horario) VALUES (?, ?)",
                   ('''Oi, pessoal,

                   Estou finalizando os ajustes no módulo de visão computacional. Acredito que até o dia 18 de setembro estará tudo pronto. Precisamos garantir que não haja nenhuma alteração no código até lá.

                   Abs, Renata''', '2024-09-05 10:00'))

    cursor.execute("INSERT INTO email_corporacao (Mensagem, Horario) VALUES (?, ?)",
                   ('''Equipe,

                   A integração da IA com os robôs está quase concluída. Vou precisar de mais um dia para finalizar os testes. Por favor, não façam nenhuma modificação no código até o dia 19 de setembro.

                   Att., Lucas''', '2024-09-04 15:00'))

    cursor.execute("INSERT INTO email_corporacao (Mensagem, Horario) VALUES (?, ?)",
                   ('''Oi, Gustavo,

                   Estou revisando a lógica de decisão e percebi que precisamos ajustar alguns parâmetros. Vou fazer isso até o dia 17 de setembro. Qualquer alteração no código antes disso pode comprometer o funcionamento da IA.

                   Abs, Adriana''', '2024-09-03 11:00'))

    cursor.execute("INSERT INTO email_corporacao (Mensagem, Horario) VALUES (?, ?)",
                   ('''Pessoal,

                   A revisão da documentação do projeto está em andamento. Vou precisar de mais dois dias para finalizar. Por favor, não façam nenhuma alteração no código até o dia 16 de setembro.

                   Att., Flavia''', '2024-09-02 14:00'))

    cursor.execute("INSERT INTO email_corporacao (Mensagem, Horario) VALUES (?, ?)",
                   ('''Equipe,

                   A integração do módulo de visão com a IA está quase pronta. Precisamos garantir que todos os testes sejam feitos até o dia 20 de setembro para evitar problemas no lançamento.

                   Lembrem-se de que qualquer modificação no código deve ser comunicada a todos.

                   Att., Renata''', '2024-09-01 09:00'))
    
    banco.commit()
    banco.close()


