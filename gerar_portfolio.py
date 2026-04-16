"""
Gerador do Portfolio: Desenvolvimento Mobile
Autora: Camila Falaschi Ide
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib import colors

# ── Margens ABNT ──────────────────────────────────────────────────────────────
LEFT_M   = 3 * cm
RIGHT_M  = 2 * cm
TOP_M    = 3 * cm
BOT_M    = 2 * cm

OUTPUT = r"C:\Users\camil\Downloads\Portfolio Desenvolvimento Mobile\Portfolio - Desenvolvimento Mobile.pdf"

# ── Estilos ───────────────────────────────────────────────────────────────────
F  = 'Helvetica'
FB = 'Helvetica-Bold'
FM = 'Courier'

def _s(name, **kw):
    return ParagraphStyle(name, **kw)

cover_text = _s('CT', fontName=F,  fontSize=12, alignment=TA_CENTER, leading=18)
cover_bold = _s('CB', fontName=FB, fontSize=16, alignment=TA_CENTER, leading=22)
cover_sub  = _s('CS', fontName=F,  fontSize=14, alignment=TA_CENTER, leading=20)

body = _s('BD', fontName=F, fontSize=12, leading=22,
          alignment=TA_JUSTIFY, firstLineIndent=1.25*cm, spaceAfter=6)

h1_st = _s('H1', fontName=FB, fontSize=12, leading=22,
           alignment=TA_LEFT, spaceBefore=6, spaceAfter=6)

h2_st = _s('H2', fontName=F, fontSize=12, leading=22,
           alignment=TA_LEFT, spaceBefore=6, spaceAfter=6)

toc_t  = _s('TOCT', fontName=FB, fontSize=12, leading=22,
            alignment=TA_CENTER, spaceAfter=18)
toc_l  = _s('TOCL', fontName=F,  fontSize=12, leading=22, alignment=TA_LEFT)

right_blk = _s('RB', fontName=F, fontSize=12, leading=22,
               alignment=TA_JUSTIFY, leftIndent=8*cm, spaceAfter=6)

code = _s('CODE', fontName=FM, fontSize=8.5, leading=13,
          alignment=TA_LEFT, leftIndent=1.25*cm,
          backColor=colors.HexColor('#f4f4f4'), spaceAfter=6,
          borderPadding=(4, 6, 4, 6))

fig_cap = _s('FIG', fontName=F, fontSize=10, leading=14,
             alignment=TA_CENTER, spaceAfter=4, spaceBefore=6)

bullet_st = _s('BUL', fontName=F, fontSize=12, leading=20,
               alignment=TA_JUSTIFY, leftIndent=2.5*cm, spaceAfter=4)

ref_st = _s('REF', fontName=F, fontSize=12, leading=22,
            alignment=TA_JUSTIFY, spaceAfter=10)


# ── Helpers ───────────────────────────────────────────────────────────────────
def sp(n=1):
    return Spacer(1, n * 0.5 * cm)

def p(txt): return Paragraph(txt, body)
def h1(txt): return Paragraph(txt, h1_st)
def h2(txt): return Paragraph(txt, h2_st)
def fig(txt): return Paragraph(txt, fig_cap)
def ref(txt): return Paragraph(txt, ref_st)

def bul(items):
    return [Paragraph(f"- {it}", bullet_st) for it in items]

def toc(num, title, pg):
    # build a dots line
    left = f"{num} {title}" if num else title
    dots = '.' * max(0, 72 - len(left) - len(str(pg)))
    return Paragraph(f"{left}{dots}{pg}", toc_l)

def toc_sub(indent, title, pg):
    left = f"   {title}"
    dots = '.' * max(0, 72 - len(left) - len(str(pg)))
    return Paragraph(f"{left}{dots}{pg}", toc_l)

def cd(txt):
    return Paragraph(txt, code)


# ── Numeração de página ───────────────────────────────────────────────────────
# Páginas físicas: 1=capa, 2=folha de rosto, 3=sumário → não exibem número
# A partir da página 4 (introdução), exibe número (começando em 3)
def page_number(canvas, doc):
    phys = doc.page          # página física (1-based)
    displayed = phys - 1    # capa e folha de rosto não contam; sumário é "2"
    if phys >= 4:           # só exibe a partir da introdução
        canvas.saveState()
        canvas.setFont(F, 10)
        x = A4[0] - RIGHT_M
        y = A4[1] - TOP_M + 0.3 * cm
        canvas.drawRightString(x, y, str(displayed))
        canvas.restoreState()


# ── Story ─────────────────────────────────────────────────────────────────────
story = []

# ═══════════════════════════════════════════════════════════════
# CAPA (p. 1)
# ═══════════════════════════════════════════════════════════════
story += [
    sp(8),
    Paragraph("ANÁLISE E DESENVOLVIMENTO DE SISTEMAS", cover_text),
    sp(1),
    Paragraph("CAMILA FALASCHI IDE", cover_text),
    sp(12),
    Paragraph("<b>PORTFOLIO:</b>", cover_bold),
    Paragraph("Desenvolvimento Mobile", cover_sub),
    sp(20),
    Paragraph("São José dos Pinhais", cover_text),
    Paragraph("2026", cover_text),
    PageBreak(),
]

# ═══════════════════════════════════════════════════════════════
# FOLHA DE ROSTO (p. 2)
# ═══════════════════════════════════════════════════════════════
story += [
    sp(2),
    Paragraph("CAMILA FALASCHI IDE", cover_text),
    sp(12),
    Paragraph("<b>PORTFOLIO:</b>", cover_bold),
    Paragraph("Desenvolvimento Mobile", cover_sub),
    sp(10),
    Paragraph(
        "Trabalho textual apresentado como requisito parcial "
        "para a obtenção de média semestral.",
        right_blk),
    sp(1),
    Paragraph("Orientador:  Prof. Luis Gustavo Cardoso", right_blk),
    sp(18),
    Paragraph("São José dos Pinhais", cover_text),
    Paragraph("2026", cover_text),
    PageBreak(),
]

# ═══════════════════════════════════════════════════════════════
# SUMÁRIO (p. 3)
# ═══════════════════════════════════════════════════════════════
story += [
    sp(2),
    Paragraph("SUMÁRIO", toc_t),
    toc("1", "INTRODUÇÃO", 3),
    toc("2", "DESENVOLVIMENTO", 4),
    toc_sub(3, "2.1 Criação do Projeto e Interface Inicial", 4),
    toc_sub(3, "2.2 Estilização e Imagens", 6),
    toc_sub(3, "2.3 Implementação das Funcionalidades", 8),
    toc_sub(3, "2.4 Envio de Pedido via Intent", 10),
    toc("3", "CONCLUSÃO", 11),
    toc("",  "REFERÊNCIAS", 12),
    PageBreak(),
]

# ═══════════════════════════════════════════════════════════════
# 1 INTRODUÇÃO (p. 3 exibida)
# ═══════════════════════════════════════════════════════════════
story += [
    h1("1 INTRODUÇÃO"),
    p(
        "Este relatório apresenta a aplicação prática dos conceitos de desenvolvimento "
        "mobile, demonstrando a construção de um aplicativo Android funcional para a "
        "hamburgueria HamburgueriaZ. O projeto foi desenvolvido com o objetivo de "
        "permitir que os clientes realizem seus pedidos diretamente pelo aplicativo, "
        "sem a necessidade de plataformas de entrega de terceiros."
    ),
    p(
        "Para sua realização, foram utilizados o Android Studio Flamingo (2022.2.1) "
        "como ambiente de desenvolvimento integrado (IDE) e a linguagem Java para a "
        "implementação das funcionalidades. O trabalho abrange desde a criação da "
        "interface visual até a implementação da lógica de negócio e o envio de pedidos "
        "por e-mail por meio de Intents, estrutura nativa da plataforma Android."
    ),
    PageBreak(),
]

# ═══════════════════════════════════════════════════════════════
# 2 DESENVOLVIMENTO (p. 4 exibida)
# ═══════════════════════════════════════════════════════════════
story += [
    h1("2 DESENVOLVIMENTO"),
    p(
        "O projeto foi desenvolvido utilizando o Android Studio Flamingo (2022.2.1), "
        "IDE oficial para o desenvolvimento de aplicações Android, em conjunto com o "
        "Java JDK 20. A construção do aplicativo foi organizada em etapas progressivas, "
        "iniciando pela criação da interface visual e avançando até a implementação "
        "completa das funcionalidades e da integração com o aplicativo de e-mail do "
        "dispositivo."
    ),
]

# ── 2.1 ──────────────────────────────────────────────────────────────────────
story += [
    h2("2.1 Criação do Projeto e Interface Inicial"),
    p(
        "Para iniciar o desenvolvimento, foi criado um novo projeto no Android Studio "
        "por meio do menu \"File > New > New Project\", selecionando o template "
        "\"Empty Activity\". Na janela de configuração, foram definidos: o nome "
        "HamburgueriaZ, a linguagem Java e o SDK mínimo API 23 (Android 6.0 "
        "Marshmallow), garantindo compatibilidade com aproximadamente 95,6% dos "
        "dispositivos Android em uso."
    ),
    p(
        "A interface do aplicativo foi construída no arquivo activity_main.xml. Para "
        "permitir a sobreposição entre o formulário de pedido e o rodapé fixo, foi "
        "utilizado um FrameLayout como container principal. Um ScrollView envolve o "
        "conteúdo rolável, garantindo a navegação adequada em telas menores. A "
        "estrutura geral do layout pode ser observada na Figura 2.1.1."
    ),
    fig("Figura 2.1.1 | Estrutura geral do arquivo activity_main.xml"),
    cd(
        "&lt;FrameLayout ...&gt;\n"
        "    &lt;ScrollView ...&gt;\n"
        "        &lt;LinearLayout android:orientation=\"vertical\"&gt;\n"
        "            &lt;ImageView android:id=\"@+id/imageLogo\" .../&gt;\n"
        "            &lt;!-- Formulário: nome, adicionais, quantidade --&gt;\n"
        "        &lt;/LinearLayout&gt;\n"
        "    &lt;/ScrollView&gt;\n"
        "    &lt;!-- Footer fixo: resumo + total + botão FAZER PEDIDO --&gt;\n"
        "&lt;/FrameLayout&gt;"
    ),
    fig("Fonte: Elaborado pelo autor"),
    sp(1),
    p(
        "Os elementos que compõem o formulário de pedido são os seguintes:"
    ),
    *bul([
        "EditText (editNome): campo de texto para inserção do nome do cliente, "
        "com inputType definido como textPersonName;",
        "CheckBox (checkBacon, checkQueijo, checkOnionRings): lista de adicionais "
        "disponíveis — Bacon, Queijo e Onion Rings;",
        "Botões + e - (btnSomar e btnSubtrair) com um TextView central "
        "(textQuantidade) para controle e exibição da quantidade selecionada;",
        "TextView (textResumo e textTotal): exibição do resumo do pedido e do "
        "valor total no rodapé fixo;",
        "Button (btnEnviarPedido): botão para finalizar e enviar o pedido.",
    ]),
    sp(1),
    p(
        "Os elementos foram agrupados em cards utilizando LinearLayout com o estilo "
        "CardStyle.Default, conferindo separação visual clara entre as seções do "
        "formulário. O rodapé foi posicionado de forma fixa na parte inferior da tela, "
        "com elevation de 8dp para que se sobreponha ao conteúdo rolável, mantendo "
        "sempre visíveis o resumo e o botão de envio."
    ),
]

# ── 2.2 ──────────────────────────────────────────────────────────────────────
story += [
    h2("2.2 Estilização e Imagens"),
    p(
        "Para garantir consistência visual em todo o aplicativo, foram criados estilos "
        "pré-definidos no arquivo themes.xml. Essa abordagem evita a repetição de "
        "propriedades em cada view individualmente e facilita alterações futuras: ao "
        "modificar um estilo, a alteração é propagada automaticamente para todas as "
        "views que o utilizam."
    ),
    p(
        "O estilo principal criado para padronização dos textos foi o EstiloTexto, "
        "apresentado na Figura 2.2.1. Ele define as propriedades de dimensionamento, "
        "alinhamento, formatação e espaçamento que devem ser aplicadas de forma "
        "uniforme nas views de título das seções."
    ),
    fig("Figura 2.2.1 | Estilo EstiloTexto no arquivo themes.xml"),
    cd(
        "&lt;style name=\"EstiloTexto\"&gt;\n"
        "    &lt;item name=\"android:layout_width\"&gt;wrap_content&lt;/item&gt;\n"
        "    &lt;item name=\"android:layout_height\"&gt;wrap_content&lt;/item&gt;\n"
        "    &lt;item name=\"android:gravity\"&gt;center_vertical&lt;/item&gt;\n"
        "    &lt;item name=\"android:textAllCaps\"&gt;true&lt;/item&gt;\n"
        "    &lt;item name=\"android:textSize\"&gt;15sp&lt;/item&gt;\n"
        "    &lt;item name=\"android:paddingTop\"&gt;16dp&lt;/item&gt;\n"
        "    &lt;item name=\"android:paddingBottom\"&gt;16dp&lt;/item&gt;\n"
        "&lt;/style&gt;"
    ),
    fig("Fonte: Elaborado pelo autor"),
    sp(1),
    p(
        "O estilo EstiloTexto foi aplicado às seguintes views do projeto: texto "
        "\"Faça seu pedido!\", rótulo \"Quantidade\", rótulo \"Resumo do Pedido\" e o "
        "TextView que exibe o valor total do pedido. Além do EstiloTexto, foram "
        "definidos estilos complementares, como TextStyle.SectionTitle (para títulos "
        "de seção dentro dos cards), ButtonStyle.Primary (para o botão principal), "
        "ButtonStyle.Counter (para os botões de quantidade) e CheckBoxStyle.Adicional "
        "(para os itens de adicionais). O tema principal, Theme.HamburgueriaZ, foi "
        "configurado com paleta de cores vermelha, alinhada à identidade visual de "
        "uma hamburgueria."
    ),
    p(
        "Para a adição da logo do restaurante, foi utilizada uma ImageView posicionada "
        "no topo da tela, funcionando como um banner. A view recebeu layout_height de "
        "200dp e scaleType definido como centerCrop, garantindo que a imagem ocupe todo "
        "o espaço disponível sem distorções, conforme apresentado na Figura 2.2.2."
    ),
    fig("Figura 2.2.2 | Configuração da ImageView de banner"),
    cd(
        "&lt;ImageView\n"
        "    android:id=\"@+id/imageLogo\"\n"
        "    android:layout_width=\"match_parent\"\n"
        "    android:layout_height=\"200dp\"\n"
        "    android:scaleType=\"centerCrop\"\n"
        "    android:src=\"@drawable/screenshot_4\"\n"
        "    android:contentDescription=\"@string/banner_description\" /&gt;"
    ),
    fig("Fonte: Elaborado pelo autor"),
]

# ── 2.3 ──────────────────────────────────────────────────────────────────────
story += [
    h2("2.3 Implementação das Funcionalidades"),
    p(
        "As funcionalidades do aplicativo foram implementadas no arquivo "
        "MainActivity.java. No método onCreate(), todas as views foram inicializadas "
        "por meio do método findViewById() e os listeners de eventos foram configurados "
        "para cada botão e checkbox, conectando a interface à lógica da aplicação."
    ),
    p(
        "Para o controle da quantidade, foram implementados os métodos somar() e "
        "subtrair(), acionados pelos botões + e -, respectivamente. Ambos atualizam o "
        "TextView de quantidade e chamam o método atualizarFooter() após cada ação. O "
        "método subtrair() inclui uma validação que impede valores negativos, "
        "conforme demonstrado na Figura 2.3.1."
    ),
    fig("Figura 2.3.1 | Métodos somar() e subtrair()"),
    cd(
        "private void somar() {\n"
        "    quantidade++;\n"
        "    textQuantidade.setText(String.valueOf(quantidade));\n"
        "    atualizarFooter();\n"
        "}\n\n"
        "private void subtrair() {\n"
        "    if (quantidade > 0) {\n"
        "        quantidade--;\n"
        "        textQuantidade.setText(String.valueOf(quantidade));\n"
        "        atualizarFooter();\n"
        "    }\n"
        "}"
    ),
    fig("Fonte: Elaborado pelo autor"),
    sp(1),
    p(
        "O cálculo do preço total foi implementado no método calcularTotal(), que "
        "considera o preço base do hambúrguer (R$ 20,00) somado ao valor dos adicionais "
        "selecionados — Bacon (R$ 2,00), Queijo (R$ 2,00) e Onion Rings (R$ 3,00) — "
        "multiplicado pela quantidade escolhida. Os preços foram definidos como "
        "constantes da classe, conforme a Figura 2.3.2."
    ),
    fig("Figura 2.3.2 | Constantes de preço e método calcularTotal()"),
    cd(
        "private static final double PRECO_BASE   = 20.0;\n"
        "private static final double PRECO_BACON  =  2.0;\n"
        "private static final double PRECO_QUEIJO =  2.0;\n"
        "private static final double PRECO_ONION  =  3.0;\n\n"
        "private double calcularTotal() {\n"
        "    double adicionais = 0;\n"
        "    if (checkBacon.isChecked())      adicionais += PRECO_BACON;\n"
        "    if (checkQueijo.isChecked())     adicionais += PRECO_QUEIJO;\n"
        "    if (checkOnionRings.isChecked()) adicionais += PRECO_ONION;\n"
        "    return (PRECO_BASE + adicionais) * quantidade;\n"
        "}"
    ),
    fig("Fonte: Elaborado pelo autor"),
    sp(1),
    p(
        "O método atualizarFooter() é chamado sempre que há alteração na seleção de "
        "adicionais ou na quantidade, atualizando o resumo e o total em tempo real. "
        "Para isso, os listeners setOnCheckedChangeListener() dos checkboxes foram "
        "configurados para chamar atualizarFooter() a cada mudança de estado."
    ),
    p(
        "A função enviarPedido() foi responsável por reunir todas as informações do "
        "pedido antes do envio. Ela realiza duas validações: verifica se o nome foi "
        "preenchido e se ao menos um hambúrguer foi selecionado, exibindo mensagens de "
        "Toast em caso de inconsistências. Após a validação, monta a string de resumo "
        "completo e a exibe no rodapé, conforme o formato especificado na atividade:"
    ),
    cd(
        "Nome do cliente: [nome]\n"
        "Tem Bacon? Sim/Não\n"
        "Tem Queijo? Sim/Não\n"
        "Tem Onion Rings? Sim/Não\n"
        "Quantidade: [n]\n"
        "Preço final: R$ [valor]"
    ),
]

# ── 2.4 ──────────────────────────────────────────────────────────────────────
story += [
    h2("2.4 Envio de Pedido via Intent"),
    p(
        "Para finalizar o aplicativo, foi implementada a integração com o cliente de "
        "e-mail do dispositivo por meio de um Intent. Os Intents são estruturas da "
        "plataforma Android que permitem a comunicação entre componentes e aplicativos, "
        "possibilitando que um app acione funcionalidades de outros apps instalados no "
        "dispositivo sem precisar implementá-las do zero."
    ),
    p(
        "Dentro do método enviarPedido(), foi criado um Intent do tipo ACTION_SENDTO, "
        "configurado com o URI \"mailto:\" para indicar que se trata de um envio de "
        "e-mail. O assunto do e-mail é preenchido automaticamente com o nome do "
        "cliente, e o corpo contém o resumo completo do pedido, conforme apresentado "
        "na Figura 2.4.1."
    ),
    fig("Figura 2.4.1 | Intent de envio de e-mail em enviarPedido()"),
    cd(
        "Intent intent = new Intent(Intent.ACTION_SENDTO);\n"
        "intent.setData(Uri.parse(\"mailto:\"));\n"
        "intent.putExtra(Intent.EXTRA_SUBJECT, \"Pedido de \" + nome);\n"
        "intent.putExtra(Intent.EXTRA_TEXT, resumoEmail);\n\n"
        "if (intent.resolveActivity(getPackageManager()) != null) {\n"
        "    startActivity(intent);\n"
        "}"
    ),
    fig("Fonte: Elaborado pelo autor"),
    sp(1),
    p(
        "A verificação intent.resolveActivity(getPackageManager()) != null garante que "
        "a chamada só seja realizada caso haja algum aplicativo de e-mail disponível no "
        "dispositivo, evitando erros em tempo de execução. Ao clicar no botão \"Fazer "
        "Pedido\", o cliente de e-mail padrão é aberto com o assunto e o corpo já "
        "preenchidos, bastando ao usuário selecionar o destinatário e confirmar o envio."
    ),
    p(
        "Com todas as funcionalidades implementadas, o projeto foi exportado para um "
        "arquivo .zip por meio do menu \"File > Export > Export to Zip File\", "
        "finalizando assim o desenvolvimento do aplicativo HamburgueriaZ."
    ),
    PageBreak(),
]

# ═══════════════════════════════════════════════════════════════
# 3 CONCLUSÃO
# ═══════════════════════════════════════════════════════════════
story += [
    h1("3 CONCLUSÃO"),
    p(
        "O desenvolvimento do projeto HamburgueriaZ permitiu aplicar na prática os "
        "principais conceitos do desenvolvimento mobile Android. A construção da "
        "interface demonstrou o uso correto das views disponíveis na plataforma, como "
        "EditText, CheckBox, Button e ImageView, além do uso de layouts aninhados para "
        "organizar os elementos de forma clara e funcional."
    ),
    p(
        "A estilização por meio do arquivo themes.xml se mostrou uma abordagem "
        "eficiente para a padronização visual do aplicativo. Ao centralizar as "
        "propriedades em estilos reutilizáveis, qualquer ajuste é propagado "
        "automaticamente para todas as views que os utilizam, eliminando a necessidade "
        "de alterações individuais e tornando a manutenção do projeto mais ágil."
    ),
    p(
        "A implementação das funcionalidades em Java consolidou o entendimento sobre "
        "eventos, manipulação de componentes e cálculos dinâmicos em tempo de execução. "
        "Por fim, o uso de Intents evidenciou como o Android permite a comunicação entre "
        "aplicativos de forma simples e eficiente, sem a necessidade de reescrever "
        "funcionalidades já existentes no sistema operacional."
    ),
    PageBreak(),
]

# ═══════════════════════════════════════════════════════════════
# REFERÊNCIAS
# ═══════════════════════════════════════════════════════════════
story += [
    Paragraph("REFERÊNCIAS", toc_t),
    ref(
        "ANDROID DEVELOPERS. <b>Android Studio</b>. Disponível em: "
        "&lt;https://developer.android.com/studio&gt;. Acesso em: 14 abr. 2026."
    ),
    ref(
        "ANDROID DEVELOPERS. <b>Intents and Intent Filters</b>. Disponível em: "
        "&lt;https://developer.android.com/guide/components/intents-filters&gt;. "
        "Acesso em: 14 abr. 2026."
    ),
    ref(
        "ANDROID DEVELOPERS. <b>Layouts</b>. Disponível em: "
        "&lt;https://developer.android.com/guide/topics/ui/declaring-layout&gt;. "
        "Acesso em: 14 abr. 2026."
    ),
    ref(
        "ORACLE. <b>Java SE Downloads</b>. Disponível em: "
        "&lt;https://www.oracle.com/java/technologies/downloads/#java20&gt;. "
        "Acesso em: 14 abr. 2026."
    ),
]

# ═══════════════════════════════════════════════════════════════
# Build
# ═══════════════════════════════════════════════════════════════
doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    leftMargin=LEFT_M,
    rightMargin=RIGHT_M,
    topMargin=TOP_M,
    bottomMargin=BOT_M,
    title="Portfolio: Desenvolvimento Mobile",
    author="Camila Falaschi Ide",
)

doc.build(story, onFirstPage=page_number, onLaterPages=page_number)
print(f"PDF gerado com sucesso: {OUTPUT}")
