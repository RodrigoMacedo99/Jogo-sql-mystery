import _sqlite3
banco =_sqlite3.connect('cimatec_ia.db')
cursor = banco.cursor()

def criar_tabelas():
     #Tabela para 'suspeitos'
    cursor.execute('CREATE TABLE IF NOT EXISTS suspeitos ( id_pessoa INTEGER PRIMARY KEY AUTOINCREMENT, Nome TEXT NOT NULL, Cargo_Cimatec TEXT, Especializacao TEXT)')

    # Tabela para 'Acesso_Laboratorio'
    cursor.execute('(CREATE TABLE Acesso_Laboratorio (id_laboratorio INTEGER PRIMARY KEY AUTOINCREMENT,Nome_Laboratorio TEXT NOT NULL, Horario_Entrada TEXT NOT NULL, Horario_Saida TEXT,Nivel_Acesso TEXT,fk_pessoa INTEGER,FOREIGN KEY (fk_pessoa) REFERENCES suspeitos(id_pessoa)')

    # Tabela para 'Arquivos_Projetos'
    cursor.execute('CREATE TABLE Arquivos_Projetos (id_registro INTEGER PRIMARY KEY AUTOINCREMENT,Nome_Arquivo TEXT NOT NULL,Horario_Modificacao TEXT,Data_Modificacao TEXT,Area_Modificada TEXT,Responsavel_fk INTEGER,FOREIGN KEY (Responsavel_fk) REFERENCES suspeitos(id_pessoa)')

    # Tabela para 'email_corporacao'
    cursor.execute('banco.execute(CREATE TABLE email_corporacao (id_mensagem INTEGER PRIMARY KEY AUTOINCREMENT,id_remetente INTEGER,id_destinatario INTEGER,Mensagem TEXT,Horario TEXT,FOREIGN KEY (id_remetente) REFERENCES suspeitos(id_pessoa),FOREIGN KEY (id_destinatario) REFERENCES suspeitos(id_pessoa)')
    
    banco.commit()

def inserir_dados():
    # Tabela para suspeitos
    # Inserindo Flavia na tabela suspeitos
    cursor.execute("INSERT INTO suspeitos (Nome, Cargo_Cimatec, Especializacao) VALUES (?, ?, ?)",
                ('Flavia', 'Pesquisadora', 'Visão Computacional'))
    # Inserindo dados de acesso ao laboratório para Flavia
    cursor.execute("INSERT INTO Acesso_Laboratorio (Nome_Laboratorio, Horario_Entrada, Horario_Saida, Nivel_Acesso, fk_pessoa) VALUES (?, ?, ?, ?, ?)",
                ('LAB-Robotica', '13:00', '17:00', 'Baixa', 5))  # Supondo que Flavia tenha o ID 5


    # Inserindo arquivo de projeto modificado por Flavia
    cursor.execute("INSERT INTO Arquivos_Projetos (Nome_Arquivo, Horario_Modificacao, Data_Modificacao, Area_Modificada, Responsavel_fk) VALUES (?, ?, ?, ?, ?)",
                ('IA - v3.2', '16:00', '2024-09-01', 'Inteligencia Artificial', 5))  # Supondo que Flavia tenha o ID 5


        # Tabela para Acesso_Laboratorio
        # Inserindo email enviado por Gustavo para a equipe
    cursor.execute("INSERT INTO email_corporacao (id_remetente, id_destinatario, Mensagem, Horario) VALUES (?, ?, ?, ?)",
                    (1, None, '''Equipe,
    
                    Conforme combinado, a atualização da nossa IA de reconhecimento de padrões e tomada de decisão (versão 3.2) está programada para o dia 21 de setembro. O código em Ruby ainda precisa de alguns ajustes para garantir a compatibilidade com o módulo de visão computacional.
                    
                    Adriana, você poderia verificar se a sua parte relacionada à lógica de decisão está dentro do cronograma? Precisamos garantir que tudo estará pronto até o dia 20 para que possamos rodar os testes finais.
                    
                    Lembrem-se de que nenhuma modificação deve ser feita na IA até a data acordada.
                    
                    Att., Gustavo''', '2024-09-15 11:00'))


    
    # Tabela para Arquivos_Projetos
    cursor.execute("INSERT INTO Arquivos_Projetos (Nome_Arquivo, Horario_Modificacao, Data_Modificacao, Area_Modificada, Responsavel_fk) VALUES (?, ?, ?, ?, ?)",
                ('Projeto_Robotica_v2', '14:45', '2024-09-10', 'Mecânica', 2))
    
    # Tabela para email_corporacao
    # Mensagem 1: Adriana para Gustavo
    cursor.execute("INSERT INTO email_corporacao (id_remetente, id_destinatario, Mensagem, Horario) VALUES (?, ?, ?, ?)",
                (2, 4, '''Oi, Gustavo,

                Estou terminando de ajustar a lógica de decisão na IA. O código está 80% finalizado e pretendo concluir tudo até o dia 19 de setembro. Acredito que podemos rodar os testes no dia 20, como planejado.

                É importante frisar que, se alguém alterar o código antes dessa data, corremos o risco de desestabilizar a IA e, consequentemente, o sistema de reconhecimento de padrões e a integração com o módulo de visão. Vamos garantir que tudo permaneça intocado até estarmos prontos para o rollout no dia 21.

                Abs, Adriana''', '2024-09-16 10:00'))

    # Mensagem 2: Renata para Todos (exemplo: Renata para Lucas e Gustavo)
    cursor.execute("INSERT INTO email_corporacao (id_remetente, id_destinatario, Mensagem, Horario) VALUES (?, ?, ?, ?)",
                (3, 4, '''Pessoal,

                Tudo certo da minha parte para a integração da visão computacional com a IA. Estarei disponível nos dias 19 e 20 para fazer os testes finais, conforme o planejamento.

                Lembrando que qualquer alteração na IA antes do dia 21 sem autorização pode comprometer todo o processo de reconhecimento visual. Precisamos evitar isso a todo custo.

                Abraços, Renata''', '2024-09-10 16:00'))

    # Mensagem 3: Lucas para Todos
    cursor.execute("INSERT INTO email_corporacao (id_remetente, id_destinatario, Mensagem, Horario) VALUES (?, ?, ?, ?)",
                (4, 3, '''Oi, equipe,

                Só para garantir, vou revisar a integração da IA com os robôs até o dia 20 de setembro. Precisamos manter a agenda para evitar problemas de sincronização entre a IA e os comandos do robô. Qualquer mudança no código agora pode gerar falhas no comportamento autônomo do robô.

                Vou reforçar que nenhuma modificação deve ser feita até que todos nós estejamos prontos para lançar a versão final no dia 21.

                Abs, Lucas''', '2024-09-09 09:00'))

    # Mensagem 4: Gustavo para Todos
    cursor.execute("INSERT INTO email_corporacao (id_remetente, id_destinatario, Mensagem, Horario) VALUES (?, ?, ?, ?)",
                (1, 3, '''Pessoal,

                Gostaria de reforçar que a atualização da IA, versão 3.2, NÃO está autorizada para ser realizada antes do dia 21 de setembro. Não houve nenhuma mudança no cronograma, e qualquer modificação anterior à data pode gerar sérios problemas no reconhecimento de padrões e na integração com os robôs e a visão computacional.

                Se alguém perceber algo fora do planejado, por favor, me avise imediatamente.

                Obrigado, Gustavo''', '2024-09-08 08:00'))

    banco.commit()

def main():
    criar_tabelas()
    inserir_dados()
    banco.close()

if __name__ == "__main__":
    main()   