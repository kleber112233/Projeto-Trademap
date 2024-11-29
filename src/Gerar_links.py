import os
import json


paises = [
    ('-2', 'Todos'),
    ('004', 'Afeganistão'),
    ('577', 'África, não especificada'),
    ('008', 'Albânia'),
    ('012', 'Argélia'),
    ('636', 'Américas, não especificada'),
    ('016', 'Samoa Americana'),
    ('020', 'Andorra'),
    ('024', 'Angola'),
    ('660', 'Anguilla'),
    ('028', 'Antígua e Barbuda'),
    ('899', 'Área, não especificada'),
    ('032', 'Argentina'),
    ('051', 'Armênia'),
    ('533', 'Aruba'),
    ('946', 'Ásia, não especificada'),
    ('036', 'Austrália'),
    ('040', 'Áustria'),
    ('031', 'Azerbaijão'),
    ('044', 'Bahamas'),
    ('048', 'Bahrein'),
    ('050', 'Bangladesh'),
    ('052', 'Barbados'),
    ('112', 'Bielorrússia'),
    ('056', 'Bélgica'),
    ('084', 'Belize'),
    ('204', 'Benim'),
    ('060', 'Bermudas'),
    ('064', 'Butão'),
    ('068', 'Bolívia'),
    ('535', 'Bonaire, Sint Eustatius e Saba'),
    ('070', 'Bósnia e Herzegovina'),
    ('072', 'Botsuana'),
    ('074', 'Ilha Bouvet'),
    ('076', 'Brasil'),
    ('080', 'Território Antártico Britânico'),
    ('086', 'Território Britânico do Oceano Índico'),
    ('092', 'Ilhas Virgens Britânicas'),
    ('096', 'Brunei'),
    ('100', 'Bulgária'),
    ('854', 'Burkina Faso'),
    ('108', 'Burundi'),
    ('132', 'Cabo Verde'),
    ('116', 'Camboja'),
    ('120', 'Camarões'),
    ('124', 'Canadá'),
    ('129', 'Caribe, não especificado'),
    ('136', 'Ilhas Cayman'),
    ('471', 'Mercado Comum Centro-Americano, não especificado'),
    ('140', 'República Centro-Africana'),
    ('148', 'Chade'),
    ('152', 'Chile'),
    ('156', 'China'),
    ('162', 'Ilha Christmas'),
    ('166', 'Ilhas Cocos (Keeling)'),
    ('170', 'Colômbia'),
    ('174', 'Comores'),
    ('178', 'Congo'),
    ('180', 'República Democrática do Congo'),
    ('184', 'Ilhas Cook'),
    ('188', 'Costa Rica'),
    ('384', 'Costa do Marfim'),
    ('191', 'Croácia'),
    ('192', 'Cuba'),
    ('531', 'Curaçao'),
    ('196', 'Chipre'),
    ('203', 'República Tcheca'),
    ('208', 'Dinamarca'),
    ('262', 'Djibouti'),
    ('212', 'Dominica'),
    ('214', 'República Dominicana'),
    ('221', 'Leste Europeu, não especificado'),
    ('218', 'Equador'),
    ('818', 'Egito'),
    ('222', 'El Salvador'),
    ('226', 'Guiné Equatorial'),
    ('232', 'Eritreia'),
    ('233', 'Estônia'),
    ('748', 'Eswatini'),
    ('231', 'Etiópia'),
    ('697', 'Europa EFTA, não especificada'),
    ('568', 'Europa, não especificada'),
    ('492', 'União Europeia, não especificada'),
    ('238', 'Ilhas Malvinas'),
    ('234', 'Ilhas Faroé'),
    ('242', 'Fiji'),
    ('246', 'Finlândia'),
    ('251', 'França'),
    ('838', 'Zonas Francas'),
    ('258', 'Polinésia Francesa'),
    ('260', 'Territórios Franceses do Sul'),
    ('266', 'Gabão'),
    ('270', 'Gâmbia'),
    ('268', 'Geórgia'),
    ('276', 'Alemanha'),
    ('288', 'Gana'),
    ('292', 'Gibraltar'),
    ('300', 'Grécia'),
    ('304', 'Groenlândia'),
    ('308', 'Granada'),
    ('316', 'Guam'),
    ('320', 'Guatemala'),
    ('324', 'Guiné'),
    ('624', 'Guiné-Bissau'),
    ('328', 'Guiana'),
    ('332', 'Haiti'),
    ('340', 'Honduras'),
    ('344', 'Hong Kong'),
    ('348', 'Hungria'),
    ('352', 'Islândia'),
    ('699', 'Índia'),
    ('360', 'Indonésia'),
    ('364', 'Irã'),
    ('368', 'Iraque'),
    ('372', 'Irlanda'),
    ('376', 'Israel'),
    ('381', 'Itália'),
    ('388', 'Jamaica'),
    ('392', 'Japão'),
    ('400', 'Jordânia'),
    ('398', 'Cazaquistão'),
    ('404', 'Quênia'),
    ('296', 'Kiribati'),
    ('408', 'Coreia do Norte'),
    ('410', 'Coreia do Sul'),
    ('414', 'Kuwait'),
    ('417', 'Quirguistão'),
    ('418', 'Laos'),
    ('428', 'Letônia'),
    ('422', 'Líbano'),
    ('426', 'Lesoto'),
    ('430', 'Libéria'),
    ('434', 'Líbia'),
    ('440', 'Lituânia'),
    ('442', 'Luxemburgo'),
    ('446', 'Macau'),
    ('807', 'Macedônia do Norte'),
    ('450', 'Madagáscar'),
    ('454', 'Malawi'),
    ('458', 'Malásia'),
    ('462', 'Maldivas'),
    ('466', 'Mali'),
    ('470', 'Malta'),
    ('584', 'Ilhas Marshall'),
    ('478', 'Mauritânia'),
    ('480', 'Maurício'),
    ('175', 'Mayotte'),
    ('484', 'México'),
    ('583', 'Micronésia'),
    ('498', 'Moldávia'),
    ('496', 'Mongólia'),
    ('499', 'Montenegro'),
    ('500', 'Montserrat'),
    ('504', 'Marrocos'),
    ('508', 'Moçambique'),
    ('104', 'Mianmar'),
    ('516', 'Namíbia'),
    ('520', 'Nauru'),
    ('524', 'Nepal'),
    ('528', 'Holanda'),
    ('530', 'Antilhas Neerlandesas'),
    ('536', 'Zona Neutra'),
    ('540', 'Nova Caledônia'),
    ('554', 'Nova Zelândia'),
    ('558', 'Nicarágua'),
    ('562', 'Níger'),
    ('566', 'Nigéria'),
    ('570', 'Niue'),
    ('574', 'Ilha Norfolk'),
    ('290', 'Norte da África, não especificada'),
    ('637', 'América Central, não especificada'),
    ('580', 'Ilhas Marianas do Norte'),
    ('579', 'Noruega'),
    ('527', 'Oceania, não especificada'),
    ('512', 'Omã'),
    ('586', 'Paquistão'),
    ('585', 'Palau'),
    ('275', 'Palestina'),
    ('591', 'Panamá'),
    ('598', 'Papua Nova Guiné'),
    ('600', 'Paraguai'),
    ('604', 'Peru'),
    ('608', 'Filipinas'),
    ('612', 'Pitcairn'),
    ('616', 'Polônia'),
    ('620', 'Portugal'),
    ('634', 'Catar'),
    ('642', 'Romênia'),
    ('643', 'Rússia'),
    ('646', 'Ruanda'),
    ('654', 'Santa Helena'),
    ('659', 'São Cristóvão e Neves'),
    ('662', 'Santa Lúcia'),
    ('666', 'São Pedro e Miquelão'),
    ('670', 'São Vicente e Granadinas'),
    ('882', 'Samoa'),
    ('678', 'São Tomé e Príncipe'),
    ('682', 'Arábia Saudita'),
    ('686', 'Senegal'),
    ('688', 'Sérvia'),
    ('690', 'Seychelles'),
    ('694', 'Serra Leoa'),
    ('702', 'Cingapura'),
    ('534', 'Sint Maarten'),
    ('703', 'Eslováquia'),
    ('705', 'Eslovênia'),
    ('090', 'Ilhas Salomão'),
    ('706', 'Somália'),
    ('710', 'África do Sul'),
    ('728', 'Sudão do Sul'),
    ('724', 'Espanha'),
    ('839', 'Categorias Especiais'),
    ('144', 'Sri Lanka'),
    ('729', 'Sudão'),
    ('740', 'Suriname'),
    ('752', 'Suécia'),
    ('757', 'Suíça'),
    ('760', 'Síria'),
    ('490', 'Taiwan'),
    ('762', 'Tajiquistão'),
    ('834', 'Tanzânia'),
    ('999', 'Território não alocado'),
    ('764', 'Tailândia'),
    ('626', 'Timor-Leste'),
    ('768', 'Togo'),
    ('772', 'Tokelau'),
    ('776', 'Tonga'),
    ('780', 'Trindade e Tobago'),
    ('788', 'Tunísia'),
    ('792', 'Turquia'),
    ('795', 'Turcomenistão'),
    ('796', 'Ilhas Turks e Caicos'),
    ('798', 'Tuvalu'),
    ('800', 'Uganda'),
    ('804', 'Ucrânia'),
    ('784', 'Emirados Árabes Unidos'),
    ('826', 'Reino Unido'),
    ('842', 'Estados Unidos'),
    ('858', 'Uruguai'),
    ('860', 'Uzbequistão'),
    ('548', 'Vanuatu'),
    ('862', 'Venezuela'),
    ('704', 'Vietnã'),
    ('876', 'Wallis e Futuna'),
    ('732', 'Saara Ocidental'),
    ('887', 'Iêmen'),
    ('894', 'Zâmbia'),
    ('716', 'Zimbábue'),
]

grupos_paises = [
    ('-2', 'Nenhum'),
    ('7', 'África'),
    ('32', 'Acordo de Crescimento Africano (AGOA)'),
    ('29', 'Grupo de Estados Africanos, Caribenhos e do Pacífico (ACP)'),
    ('31', 'Américas'),
    ('19', 'Comunidade Andina'),
    ('20', 'Ásia'),
    ('39', 'Cooperação Econômica da Ásia-Pacífico (APEC)'),
    ('13', 'Acordo Comercial Ásia-Pacífico (APTA)'),
    ('24', 'Associação das Nações do Sudeste Asiático (ASEAN)'),
    ('40', 'Cooperação Econômica do Mar Negro (BSEC)'),
    ('5880', 'Brasil, Rússia, Índia e China (BRIC)'),
    ('6757', 'Brasil, Rússia, Índia, China e África do Sul (BRICS)'),
    ('37', 'Comunidade do Caribe (CARICOM)'),
    ('17', 'Mercado Comum Centro-Americano (CACM)'),
    ('3', 'Europa Central e Oriental (CEE)'),
    ('23', 'Repúblicas da Ásia Central'),
    ('12', 'Mercado Comum do Leste e Sul da África (COMESA)'),
    ('34', 'Mercado Comum do Sul (MERCOSUL)'),
    ('33910', 'Comunidade Britânica'),
    ('33', 'Comunidade de Estados Independentes (CEI)'),
    ('9', 'União Aduaneira da África Central (UDEAC)'),
    ('1', 'Economias de Mercado Desenvolvidas'),
    ('22934', 'Países em Desenvolvimento - 8 (D-8)'),
    ('2', 'Economias de Mercado em Desenvolvimento'),
    ('3981', 'Comunidade da África Oriental (EAC)'),
    ('29243', 'Comunidade Econômica da África Central (ECCAS)'),
    ('8', 'Comunidade Econômica dos Estados da África Ocidental (CEDEAO)'),
    ('27', 'Organização de Cooperação Econômica (ECO)'),
    ('25', 'Europa'),
    ('26', 'União Europeia (UE 15)'),
    ('42', 'União Europeia (UE 27)'),
    ('14719', 'União Europeia (UE 28)'),
    ('41', 'G7'),
    ('21', 'Grande China'),
    ('38', 'Conselho de Cooperação do Golfo (GCC)'),
    ('4327', 'Associação de Cooperação do Oceano Índico (IOR-ARC)'),
    ('5890', 'Países em Desenvolvimento sem Saída ao Mar (LLDC)'),
    ('15', 'América Latina e Caribe'),
    ('16', 'Associação Latino-Americana de Integração (ALADI)'),
    ('6577', 'Países Menos Desenvolvidos (PMD)'),
    ('10', 'Magrebe'),
    ('22', 'Oriente Médio'),
    ('14', 'Acordo de Livre Comércio da América do Norte (NAFTA)'),
    ('28', 'Oceania'),
    ('6578', 'Organização para Cooperação e Desenvolvimento Econômico (OCDE)'),
    ('4', 'OCDE - até 2010'),
    ('21491', 'Organização Internacional da Francofonia (OIF)'),
    ('51436', 'Organização dos Estados do Caribe Oriental (OECS)'),
    ('30', 'Organização dos Países Exportadores de Petróleo (OPEP)'),
    ('6', 'Organização da Cooperação Islâmica (OCI)'),
    ('5891', 'Pequenos Estados Insulares em Desenvolvimento (SID)'),
    ('18', 'Associação Sul-Asiática para Cooperação Regional (SAARC)'),
    ('11', 'União Aduaneira da África Austral (SACU)'),
    ('35', 'Comunidade de Desenvolvimento da África Austral (SADC)'),
    ('59232', 'União Econômica da Eurásia (UEE)'),
    ('36', 'União Econômica e Monetária da África Ocidental (UEMOA)'),
    ('2227', 'Organização Mundial do Comércio (OMC)'),
]


produtos = [
    ('TOTAL', 'Todos os produtos'),
    ('01', 'Animais vivos'),
    ('02', 'Carnes e derivados comestíveis'),
    ('03', 'Peixes e crustáceos'),
    ('04', 'Produtos lácteos e mel'),
    ('05', 'Outros produtos de origem animal'),
    ('06', 'Plantas vivas e flores'),
    ('07', 'Vegetais e raízes comestíveis'),
    ('08', 'Frutas e nozes'),
    ('09', 'Café, chá e especiarias'),
    ('10', 'Cereais'),
    ('11', 'Produtos da indústria de moagem'),
    ('12', 'Sementes e frutas oleaginosas'),
    ('13', 'Gomas e resinas vegetais'),
    ('14', 'Materiais para trançar e outros produtos vegetais'),
    ('15', 'Gorduras e óleos animais ou vegetais'),
    ('16', 'Preparações de carnes e peixes'),
    ('17', 'Açúcares e confeitos'),
    ('18', 'Cacau e derivados'),
    ('19', 'Preparações de cereais e produtos de panificação'),
    ('20', 'Preparações de vegetais e frutas'),
    ('21', 'Outras preparações alimentícias'),
    ('22', 'Bebidas, álcool e vinagre'),
    ('23', 'Resíduos da indústria alimentícia'),
    ('24', 'Tabaco e substitutos de tabaco'),
    ('25', 'Sal, enxofre, terras e pedras'),
    ('26', 'Minérios e escórias'),
    ('27', 'Combustíveis minerais e óleos'),
    ('28', 'Produtos químicos inorgânicos'),
    ('29', 'Produtos químicos orgânicos'),
    ('30', 'Produtos farmacêuticos'),
    ('31', 'Fertilizantes'),
    ('32', 'Corantes e pigmentos'),
    ('33', 'Óleos essenciais e cosméticos'),
    ('34', 'Sabões e produtos de limpeza'),
    ('35', 'Substâncias proteicas e enzimas'),
    ('36', 'Explosivos e pirotecnia'),
    ('37', 'Produtos fotográficos e cinematográficos'),
    ('38', 'Outros produtos químicos'),
    ('39', 'Plásticos e artigos de plástico'),
    ('40', 'Borracha e artigos de borracha'),
    ('41', 'Couro bruto e peles'),
    ('42', 'Artigos de couro e similares'),
    ('43', 'Peles e peles artificiais'),
    ('44', 'Madeira e artigos de madeira'),
    ('45', 'Cortiça e artigos de cortiça'),
    ('46', 'Cestos e artefatos de palha'),
    ('47', 'Papel e celulose'),
    ('48', 'Papel e artigos de papel'),
    ('49', 'Livros e impressos'),
    ('50', 'Seda'),
    ('51', 'Lã e pelos'),
    ('52', 'Algodão'),
    ('53', 'Outras fibras têxteis vegetais'),
    ('54', 'Filamentos artificiais'),
    ('55', 'Fibras artificiais'),
    ('56', 'Feltros e tecidos especiais'),
    ('57', 'Tapetes e coberturas de chão'),
    ('58', 'Tecidos e bordados especiais'),
    ('59', 'Tecidos impregnados e industriais'),
    ('60', 'Tecidos de malha'),
    ('61', 'Vestuário de malha'),
    ('62', 'Vestuário, não de malha'),
    ('63', 'Outros artigos têxteis'),
    ('64', 'Calçados e partes de calçados'),
    ('65', 'Chapéus e acessórios de cabeça'),
    ('66', 'Guarda-chuvas e similares'),
    ('67', 'Flores artificiais e artigos de cabelo'),
    ('68', 'Artigos de pedra e cimento'),
    ('69', 'Produtos cerâmicos'),
    ('70', 'Vidros e vidrarias'),
    ('71', 'Pérolas, pedras preciosas e metais preciosos'),
    ('72', 'Ferro e aço'),
    ('73', 'Artigos de ferro e aço'),
    ('74', 'Cobre e artigos de cobre'),
    ('75', 'Níquel e artigos de níquel'),
    ('76', 'Alumínio e artigos de alumínio'),
    ('78', 'Chumbo e artigos de chumbo'),
    ('79', 'Zinco e artigos de zinco'),
    ('80', 'Estanho e artigos de estanho'),
    ('81', 'Outros metais'),
    ('82', 'Ferramentas e talheres'),
    ('83', 'Outros artigos de metal'),
    ('84', 'Máquinas e aparelhos mecânicos'),
    ('85', 'Máquinas e aparelhos elétricos'),
    ('86', 'Locomotivas e equipamentos ferroviários'),
    ('87', 'Veículos e partes'),
    ('88', 'Aeronaves e espaçonaves'),
    ('89', 'Navios e embarcações'),
    ('90', 'Instrumentos e aparelhos óticos e médicos'),
    ('91', 'Relógios e acessórios'),
    ('92', 'Instrumentos musicais'),
    ('93', 'Armas e munições'),
    ('94', 'Móveis e produtos de iluminação'),
    ('95', 'Brinquedos e equipamentos esportivos'),
    ('96', 'Outros artigos manufaturados'),
    ('97', 'Obras de arte e antiguidades'),
    ('98', 'Mercadorias específicas por capítulo'),
    ('99', 'Mercadorias não especificadas'),
]






# Função para calcular a largura máxima disponível no terminal
def largura_terminal():
    return os.get_terminal_size().columns

# Função para exibir a mensagem de erro com um bloco visual destacado
def exibir_mensagem_erro(mensagem, largura_total):
    print("\n" + "#" * largura_total)
    print("#" + " " * (largura_total - 2) + "#")
    print("#" + mensagem.center(largura_total - 2) + "#")
    print("#" + " " * (largura_total - 2) + "#")
    print("#" * largura_total + "\n")

# Função para paginar opções com layout de 3 colunas e 15 linhas
def paginar_opcoes(opcoes, titulo, escolhas_iniciais=None):
    largura_total = largura_terminal()
    largura_coluna = largura_total // 3

    comprimento_maximo_texto = largura_coluna - 5
    espaco_entre_colunas = 2

    num_colunas = 3
    linhas_por_pagina = 15
    tamanho_pagina = num_colunas * linhas_por_pagina

    pagina_atual = 1
    total_paginas = (len(opcoes) + tamanho_pagina - 1) // tamanho_pagina
    itens_selecionados = escolhas_iniciais if escolhas_iniciais else []
    mensagem_erro = ""
    
    # Ordena as opções com "Todos" ou "Nenhum" no início, independentemente da ordem alfabética
    opcoes_ordenadas = sorted(opcoes[1:], key=lambda x: x[1])
    opcoes_ordenadas.insert(0, opcoes[0])

    while True:
        print("\n" * 100)
        
        indice_inicial = (pagina_atual - 1) * tamanho_pagina
        indice_final = min(indice_inicial + tamanho_pagina, len(opcoes_ordenadas))
        
        print("=" * largura_total)
        print(f"{titulo} (Página {pagina_atual}/{total_paginas})".center(largura_total))
        print("=" * largura_total)
        
        for i in range(indice_inicial, indice_final, num_colunas):
            linha = ""
            for j in range(i, min(i + num_colunas, indice_final)):
                texto_item = f"[{j + 1}] {opcoes_ordenadas[j][1][:comprimento_maximo_texto]}"
                linha += texto_item.ljust(largura_coluna - espaco_entre_colunas)
            print(linha)
            print()

        if itens_selecionados:
            print("_" * largura_total + "\n\nItens selecionados até agora:\n")
            for idx, item in enumerate(itens_selecionados, 1):
                print(f"{idx} | {item[1]}")

        if mensagem_erro:
            exibir_mensagem_erro(mensagem_erro, largura_total)
            mensagem_erro = ""
        
        print("\n" + "-" * largura_total)
        print("Selecione o número do item ou:\n")
        print("[A] Avançar página".ljust(30), "[V] Voltar página".ljust(30))

        if itens_selecionados:
            print("[E] Editar escolhas".ljust(30), end="")
        
        print("[P] Próxima etapa".ljust(30), "[F] Finalizar seleção".ljust(30))
        
        escolha = input("Digite sua escolha: ").strip().lower()
        
        if escolha == "a" and pagina_atual < total_paginas:
            pagina_atual += 1
        elif escolha == "v" and pagina_atual > 1:
            pagina_atual -= 1
        elif escolha == "f":
            if not itens_selecionados:
                mensagem_erro = "Você deve selecionar pelo menos um item antes de finalizar a etapa."
            else:
                break
        elif escolha == "e" and itens_selecionados:
            print("\nEdição de seleção:")
            for idx, item in enumerate(itens_selecionados, 1):
                print(f"[{idx}] {item[1]}")
            remover = input("Digite o número do item para remover ou pressione Enter para voltar: ").strip()
            if remover.isdigit() and 1 <= int(remover) <= len(itens_selecionados):
                item_removido = itens_selecionados.pop(int(remover) - 1)
                print(f"\n{item_removido[1]} removido da seleção.")
            else:
                mensagem_erro = "Opção inválida ou nenhuma alteração feita."
            continue
        elif escolha == "p":
            if not itens_selecionados:
                mensagem_erro = "Você deve selecionar pelo menos um item antes de passar para a próxima etapa."
            else:
                break
        elif escolha.isdigit() and 1 <= int(escolha) <= len(opcoes_ordenadas):
            item_selecionado = opcoes_ordenadas[int(escolha) - 1]
            if item_selecionado not in itens_selecionados:
                itens_selecionados.append(item_selecionado)
                print(f"\nSelecionado: [{escolha}] {item_selecionado[1]}")
                mais = input("Deseja selecionar mais algum? (s/n): ").strip().lower()
                if mais != "s":
                    break
            else:
                mensagem_erro = f"{item_selecionado[1]} já foi selecionado e não pode ser escolhido novamente."
        else:
            mensagem_erro = "Opção inválida, tente novamente."
    
    return itens_selecionados


# Função principal que organiza o fluxo entre os grupos e a edição final
def gerar_urls(base_url, paises_selecionados, grupos_selecionados, produtos_selecionados, parceiros_selecionados, grupos_parceiros_selecionados):
    urls = {}

    for produto in produtos_selecionados:
        produto_param = produto[0] if produto[0] != "TOTAL" else "TOTAL"
        
        # Gera combinações para quando país é "Todos"
        if any(pais[0] == "-2" for pais in paises_selecionados):
            for grupo in grupos_selecionados:
                for partner in parceiros_selecionados:
                    # Partner específico exclui a seleção de qualquer grupo de parceiros
                    if partner[0] == "-2":  # Partner "Todos"
                        for partner_group in grupos_parceiros_selecionados:
                            url = base_url.format(
                                pais="",
                                grupo=grupo[0] if grupo[0] != "-2" else "",
                                produto=produto_param,
                                partner="",
                                partner_group=partner_group[0] if partner_group[0] != "-2" else ""
                            )
                            urls[url] = {
                                "produto": produto[1],
                                "pais": "Todos",
                                "grupo de paises": grupo[1],
                                "partner": "Todos",
                                "partner_group": partner_group[1]
                            }
                    else:  # Partner específico e nenhum grupo de parceiros
                        url = base_url.format(
                            pais="",
                            grupo=grupo[0] if grupo[0] != "-2" else "",
                            produto=produto_param,
                            partner=partner[0],
                            partner_group=""
                        )
                        urls[url] = {
                            "produto": produto[1],
                            "pais": "Todos",
                            "grupo de paises": grupo[1],
                            "partner": partner[1],
                            "partner_group": "Nenhum"
                        }

        # Gera combinações para países específicos sem grupos de países
        for pais in paises_selecionados:
            if pais[0] != "-2":  # País específico
                for partner in parceiros_selecionados:
                    if partner[0] == "-2":  # Partner "Todos"
                        for partner_group in grupos_parceiros_selecionados:
                            url = base_url.format(
                                pais=pais[0],
                                grupo="",
                                produto=produto_param,
                                partner="",
                                partner_group=partner_group[0] if partner_group[0] != "-2" else ""
                            )
                            urls[url] = {
                                "produto": produto[1],
                                "pais": pais[1],
                                "grupo de paises": "Nenhum",
                                "partner": "Todos",
                                "partner_group": partner_group[1]
                            }
                    else:  # Partner específico e nenhum grupo de parceiros
                        url = base_url.format(
                            pais=pais[0],
                            grupo="",
                            produto=produto_param,
                            partner=partner[0],
                            partner_group=""
                        )
                        urls[url] = {
                            "produto": produto[1],
                            "pais": pais[1],
                            "grupo de paises": "Nenhum",
                            "partner": partner[1],
                            "partner_group": "Nenhum"
                        }

    return urls


# URL base ajustada
url_base = "https://www.trademap.org/Country_SelProduct.aspx?nvpm=1%7c{pais}%7c{grupo}%7c{partner}%7c{partner_group}%7c{produto}%7c%7c%7c2%7c1%7c1%7c1%7c1%7c1%7c2%7c1%7c1%7c1"

# Função principal que organiza o fluxo entre os grupos e a edição final
def fluxo_selecao():
    paises_selecionados = paginar_opcoes(paises, "Selecione os Países")
    grupos_selecionados = paginar_opcoes(grupos_paises, "Selecione os Grupos de Países")
    produtos_selecionados = paginar_opcoes(produtos, "Selecione os Produtos")
    parceiros_selecionados = paginar_opcoes(paises, "Selecione os Parceiros")  # Usando 'paises' para 'parceiros'
    grupos_parceiros_selecionados = paginar_opcoes(grupos_paises, "Selecione os Grupos de Parceiros")

    # Revisão Final das escolhas antes de gerar URLs
    while True:
        print("\nRevisão das escolhas finais:")
        print("1. Países Selecionados:", [pais[1] for pais in paises_selecionados])
        print("2. Grupos de Países Selecionados:", [grupo[1] for grupo in grupos_selecionados])
        print("3. Produtos Selecionados:", [produto[1] for produto in produtos_selecionados])
        print("4. Parceiros Selecionados:", [partner[1] for partner in parceiros_selecionados])
        print("5. Grupos de Parceiros Selecionados:", [grupo_partner[1] for grupo_partner in grupos_parceiros_selecionados])

        edicao = input("\nDeseja editar algum grupo? (1 - Países, 2 - Grupos de Países, 3 - Produtos, 4 - Parceiros, 5 - Grupos de Parceiros, 0 - Continuar): ").strip()
        
        if edicao == "1":
            paises_selecionados = paginar_opcoes(paises, "Selecione os Países", escolhas_iniciais=paises_selecionados)
        elif edicao == "2":
            grupos_selecionados = paginar_opcoes(grupos_paises, "Selecione os Grupos de Países", escolhas_iniciais=grupos_selecionados)
        elif edicao == "3":
            produtos_selecionados = paginar_opcoes(produtos, "Selecione os Produtos", escolhas_iniciais=produtos_selecionados)
        elif edicao == "4":
            parceiros_selecionados = paginar_opcoes(paises, "Selecione os Parceiros", escolhas_iniciais=parceiros_selecionados)
        elif edicao == "5":
            grupos_parceiros_selecionados = paginar_opcoes(grupos_paises, "Selecione os Grupos de Parceiros", escolhas_iniciais=grupos_parceiros_selecionados)
        elif edicao == "0":
            print("\nFinalizando as escolhas...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    return paises_selecionados, grupos_selecionados, produtos_selecionados, parceiros_selecionados, grupos_parceiros_selecionados


# Execução do processo de seleção e geração de URLs
paises_selecionados, grupos_selecionados, produtos_selecionados, parceiros_selecionados, grupos_parceiros_selecionados = fluxo_selecao()
urls_dict = gerar_urls(url_base, paises_selecionados, grupos_selecionados, produtos_selecionados, parceiros_selecionados, grupos_parceiros_selecionados)

# Caminho para salvar o JSON com URLs e filtros
caminho_arquivo = r"data\urls_geradas.json"

# Salva o dicionário em JSON
with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    json.dump(urls_dict, arquivo, ensure_ascii=False, indent=4)

# Exibir as escolhas finais
print("\nSUAS ESCOLHAS:")
print("_" * 100)
print("\nPaíses Selecionados:")
for pais in paises_selecionados:
    print(f"- {pais[1]}")
print("\nGrupos de Países Selecionados:")
for grupo in grupos_selecionados:
    print(f"- {grupo[1]}")
print("\nProdutos Selecionados:")
for produto in produtos_selecionados:
    print(f"- {produto[1]}")
print("\nParceiros Selecionados:")
for partner in parceiros_selecionados:
    print(f"- {partner[1]}")
print("\nGrupos de Parceiros Selecionados:")
for grupo_partner in grupos_parceiros_selecionados:
    print(f"- {grupo_partner[1]}")
print(f"\nURLs e filtros foram gerados e salvos em '{caminho_arquivo}'.")