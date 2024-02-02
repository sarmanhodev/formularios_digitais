from flask import *
import requests
import json
from datetime import datetime

app = Flask(__name__, template_folder= "templates")

@app.route("/")
def home():

    return render_template("sublocacao.html")


@app.route("/gera_formulario", methods=['GET', 'POST'])
def gera_formulario():
    if request.method == 'POST':
        #DADOS SUBLOCADOR
        nome_sublocador = request.form['nome_sublocador']
        rg_sublocador = request.form['rg_sublocador']
        cpf_sublocador = request.form['cpf_sublocador']
        cep_sublocador = request.form['cep_sublocador']
        logradouro_sublocador= request.form['logradouro_sublocador']
        bairro_sublocador = request.form['bairro_sublocador']
        numero_residencia_sublocador = request.form['numero_residencia_sublocador']
        complemento_residencia_sublocador = request.form ['complemento_residencia_sublocador']
        localidade_sublocador = request.form['localidade_sublocador']
        uf_sublocador = request.form['uf_sublocador']

        #DADOS SUBLOCATÁRIO
        nome_sublocatario = request.form['nome_sublocatario']
        rg_sublocatario = request.form['rg_sublocatario']
        cpf_sublocatario = request.form['cpf_sublocatario']
        cep_sublocatario = request.form['cep_sublocatario']
        logradouro_sublocatario = request.form['logradouro_sublocatario']
        bairro_sublocatario = request.form['bairro_sublocatario']
        numero_residencia_sublocatario = request.form['numero_residencia_sublocatario']
        complemento_residencia_sublocatario = request.form['complemento_residencia_sublocatario']
        localidade_sublocatario = request.form['localidade_sublocatario']
        uf_sublocatario = request.form['uf_sublocatario']

        #DADOS IMÓVEL
        imovel_sublocador = request.form['imovel_sublocador']
        imovel_sublocatario = request.form['imovel_sublocatario']
        cep_imovel = request.form['cep_imovel']
        logradouro_imovel = request.form['logradouro_imovel']
        bairro_imovel = request.form['bairro_imovel']
        numero_imovel = request.form['numero_imovel']
        complemento_imovel = request.form['complemento_imovel']
        localidade_imovel = request.form['localidade_imovel']
        uf_imovel = request.form['uf_imovel']
        data_locacao = request.form['data_locacao']
        atuacao_profissional = request.form['atuacao_profissional']


        #DADOS CLÁUSULA SEGUNDA
        valor_aluguel = request.form['valor_aluguel']
        dia_pagamento = request.form['dia_pagamento']

        #DADOS CLÁUSULA SEXTA
        inicio_prazo = request.form['inicio_prazo']
        termino_prazo = request.form['termino_prazo']

        #DADOS CLÁUSULA OITAVA
        estado_foro = request.form['estado_foro']
        uf_foro = request.form['uf_foro']

        #DATA DOCUMENTO
        data_atual = request.form['data_atual']

        html=f"""
            <!doctype html>
            <html lang="pt-br">

            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Modelo Contrato de Sublocação</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
            </head>

            <body>
                <br>
                <div class="row m-1">
                    <h1 class="text-center m-1">Contrato de Sublocação</h1>
                </div>
                <br>
                <div class="container-fluid m-1">
                    <p><b>SUBLOCADOR:</b> {nome_sublocador.upper()}, médico, inscrito no CRM sob nº {rg_sublocador}, inscrito no CPF sob o
                        nº {cpf_sublocador}, com domicílio profissional na {logradouro_sublocador}, número {numero_residencia_sublocador} {complemento_residencia_sublocador},
                        bairro de {bairro_sublocador}, CEP nº {cep_sublocador}, {localidade_sublocador} - {uf_sublocador}.</p>

                    <p><b>SUBLOCATÁRIO:</b> {nome_sublocatario.upper()}, médico, inscrito no CRM sob o nº {rg_sublocatario}, CPF/MF nº {cpf_sublocatario},
                        residente e domiciliada à {logradouro_sublocatario}, {numero_residencia_sublocatario} {complemento_residencia_sublocatario}, {bairro_sublocatario},
                        CEP nº {cep_sublocatario}, {localidade_sublocatario} - {uf_sublocatario}.</p> 
                        <br>
                    <div class="row">
                        <div class="fw-bold">CLAÚSULA PRIMEIRA – DO OBJETO</div>
                            <p>O <b>SUBLOCADOR</b>, sublocará a sala situada na {logradouro_imovel}, CEP nº {cep_imovel}, em sua posse por força do 
                            “Instrumento Particular de Contrato de Locação”, firmado entre {imovel_sublocador.upper()} e {imovel_sublocatario.upper()}, em {data_locacao},
                            com a finalidade exclusiva de permitir ao SUBLOCATÁRIO atuação profissional como {atuacao_profissional}.
                            </p>
                    </div>

                    <div><b class="fst-italic">Parágrafo Primeiro -</b> Os equipamentos e acessórios utilizados pelo <b>SUBLOCATÁRIO</b> na prestação dos serviços médicos nas dependências do
                    imóvel são de propriedades e responsabilidade do <b>SUBLOCADOR</b>, salvo os que forem trazidos pelo <b>SUBLOCATÁRIO</b>.</div>

                    <div><b class="fst-italic">Parágrafo Segundo -</b> O <b>SUBLOCATÁRIO</b> se obriga a manter em segurança, sob sua guarda, assim como a conservação de todos os bens que guarnecem o imóvel 
                        de forma a bem servir os pacientes, manter a segurança da clinica, funcionários e usuários dos serviços médicos prestados.</div>
                        <br>
                    <div class="row">
                        <div class="fw-bold">CLÁUSULA SEGUNDA – DO VALOR PELO DIA UTILIZADO</div>
                            <p>O <b>SUBLOCATÁRIO</b> pagará ao <b>SUBLOCADOR</b> a importância de R$ {valor_aluguel}, todo o dia <span class="fw-bold text-danger">{dia_pagamento}</span> de cada mês, referente ao pagamento pela 
                                utilização do imóvel <span class="fw-bold text-danger">1 (uma) vez por semana</span>. 
                            </p>
                    </div>
                    <br>
                    <div class="row">
                        <div class="fw-bold">CLÁUSULA TERCEIRA - DA CONSERVAÇÃO E BENFEITORIAS</div>
                            <p>O <b>SUBLOCATÁRIO</b> não poderá fazer no imóvel nenhuma benfeitoria que importe em modificações, alterações, redução, acréscimo, 
                                demolição ou mesmo reforma de qualquer espécie sem autorização expressa do <b>SUBLOCADOR</b>.  </p>
                    </div>

                    <p><span class="fw-bold fst-italic">Parágrafo Primeiro -</span> No caso do <b>SUBLOCADOR</b>, autorizar qualquer tipo de reforma, estes serão incorporados ao imóvel, não cabendo, em nenhuma hipótese, direito a indenização ou retenção, comprometendo-se o 
                        <b>SUBLOCATÁRIO</b> a repor o imóvel nas condições primitivas, se assim convir ao <b>SUBLOCADOR</b>.</p>

                    <div><span class="fw-bold fst-italic">Parágrafo Segundo -</span> O <b>SUBLOCATÁRIO</b> declara desde já ter recebido o imóvel em estado de novo, estando a pintura, instalações elétricas e hidráulicas em perfeito estado, 
                        devendo devolvê-lo no estado em que se encontra.</div>
                    <br>
                    <div class="row">
                        <div class="fw-bold">CLÁUSULA QUARTA – DAS OBRIGAÇÕES DO SUBLOCATÁRIO</div>
                        <div><b>3.1 –</b> Prestar seus serviços de acordo com as normas técnicas exigidas pela legislação vigente e, em consonância com o Código de Ética Médica, cabendo-lhe a responsabilidade pelos atos praticados no interior na clínica do <b>SUBLOCADOR</b>.</div>
                        <div><b>3.2 –</b> Proceder a inclusão no sistema de informática do <b>SUBLOCADOR</b> de todos os procedimentos realizados, para verificação e acompanhamento do paciente.</div>
                        <div><b>3.3 –</b> Os sócios, funcionários e prestadores de serviços do <b>SUBLOCATÁRIO</b> deverão comparecer às dependências do imóvel trajando uniformes apropriados e identificados, assim como observar cumprimentos das normas internas estipuladas pelo SUBLOCADOR, as quais 
                            passam a fazer parte integrante e complementar do presente contrato.</div>
                        <div><b>3.4 –</b> Providenciar a regularização de suas atividades no imóvel do <b>SUBLOCADOR</b>, junto aos órgãos municipais, estaduais e federais, remetendo anualmente cópia da documentação para exibição às autoridades e arquivo.</div>
                        <div><b>3.5 –</b> Enviar ao <b>SUBLOCADOR</b> mensalmente, as guias específicas de recolhimento do FGTS e INSS referente a seus funcionários, bem como comprovantes de pagamento dos salários dos empregados que tiver.</div>
                        <div><b>3.6 –</b> Eximir o <b>SUBLOCADOR</b> de toda e qualquer responsabilidade proveniente de eventuais ações judiciais, especialmente trabalhistas, previdenciárias, acidentarias e cíveis que objetivarem reparações de danos materiais, estéticos e morais, promovidas pelos empregados, ex-empregados ou pacientes sob procedimentos do <b>SUBLOCATÁRIO</b>.</div>
                        <div><b>3.7 –</b> Contratar seguro de responsabilidade civil médica, a fim de evitar prejuízo financeiro, causado por eventual ação judicial.</div>
                        <div><b>3.8 –</b> Em hipótese alguma, ceder, locar, emprestar ou transferir a terceiros as instalações objeto do presente contrato, nem os procedimentos que deste resultem em qualquer dependência da sede do <b>SUBLOCADOR</b>.</div>
                        <div><b>3.9 –</b> Atender os pacientes de acordo com o REGIMENTO INTERNO e normais técnicas específicas a cada atividade médica.</div>
                        <div><b>3.10 –</b> Manter a evolução na ficha específica do paciente, assim como preencher todos os formulários necessários para o acompanhamento.</div>
                        <div><b>3.11 -</b> Zelar pela limpeza, conversação, tranqüilidade, suprimento de energia elétrica, água, necessários ao bom desempenho médico do em sua atividade.</div>
                    </div>

                    <br>

                    <div class="row">
                        <div class="fw-bold">CLÁUSULA QUINTA – SÃO OBRIGAÇÕES DO SUBLOCADOR: </div>
                        <div><b>4.0 –</b> Pagamento de todas as taxas, encargos e impostos referente ao imóvel, objeto do presente contrato.</div>
                        <div><b>4.1 –</b> Promover o pagamento de todos os reparos estruturais, a fim de manter o imóvel em condições de atendimento e consulta pelo <b>SUBLOCATÁRIO</b>.</div>
                        <div><b>4.2 –</b> Fazer a contratação de funcionários administrativos para auxiliar o <b>SUBLOCATÁRIO</b> no desempenho de sua função.</div>
                        <div><b>4.3 –</b> Fazer todos os pagamentos referentes a encargos trabalhistas dos funcionários que eventualmente forem contratados.</div>
                    </div>

                    <br>
                    
                    <div class="row" style='margin-top: 50px;'>
                        <div class="fw-bold">CLÁUSULA SEXTA - DO PRAZO</div>
                        <div>O presente contrato se iniciará em {inicio_prazo} e terá o seu término previsto para {termino_prazo}, onde as partes irão discutir sobre a 
                            possibilidade de renovação do presente e termo e as novas condições.</div>
                        <div><span class="fw-bold fst-italic">Parágrafo Único -</span> O presente contrato não terá renovação automática, se encerrando ao seu término, independentemente de qualquer notificação e/ou aviso.</div>
                    </div>
                    
                    <br>
                    <div class="row">
                        <div class="fw-bold">CLÁUSULA SÉTIMA – DA RESCISÃO CONTRATUAL</div>
                        <div>Será licito ao <b>SUBLOCATÁRIO</b> devolver, ou ao <b>SUBLOCADOR</b> retomar o imóvel objeto deste contrato, mediante aviso prévio com antecedência de 60 (sessenta) dias.</div>
                        <div><span class="fw-bold fst-italic">Parágrafo Único -</span> Este contrato estará rescindido a qualquer tempo de pleno direito, sem que caiba aviso prévio estipulado no caput desta cláusula ou indenização de parte a parte nos seguintes casos: 
                            <div class="row m-1">
                                <li>Falência e/ou concordata das partes</li>
                                <li>Cessão do contrato a terceiros pelo SUBLOCATÁRIO</li>
                                <li>Infração a qualquer cláusula do presente contrato</li>
                                <li>Rescisão do contrato de locação do estabelecimento do SUBLOCADOR.</li>
                            </div>
                        </div>
                    </div>

                    <br>

                    <div class="row">
                        <div class="fw-bold">CLÁUSULA OITAVA – DO FORO</div>
                        <div>As partes contratantes elegem o foro da cidade de {estado_foro}/{uf_foro.upper()}, excluindo outro por mais privilegiado que seja, 
                            para dirimir qualquer ação oriunda deste instrumento.</div>
                    </div>

                    <br>

                    <div class="row">
                        <p>E para firmeza, e como prova de assim haverem contratado, fazem este instrumento particular, em duas vias de igual teor, assinado pelas partes contratantes e pelas testemunhas abaixo qualificadas, a tudo presentes.</p>
                    </div>

                    <div class="row text-center">
                            <div>{data_atual}</div>
                    </div>


                    <div class="text-center" style='margin-top: 40px;'>
                        <div>_________________________________________________</div>
                        <div>{nome_sublocador.upper()}</div>
                        <div class="fw-bold">SUBLOCADOR</div>
                        <br>
                        <br>
                        <div>_________________________________________________</div>
                        <div>{nome_sublocatario.upper()}</div>
                        <div class="fw-bold">SUBLOCATARIO</div>
                    </div>

                    

                    <div class="row" style='margin-top: 5px;'>
                        <div class="fw-bold">Testemunhas:</div>
                        <div>Testemunha:_______________________________________________</div>
                        <div>CPF: ______________________</div>
                        <br>
                        <br>
                        <div>Testemunha:_______________________________________________</div>
                        <div>CPF: ______________________</div>
                    </div>
                    <br>
                </div>
                </style>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
            </body>

            </html>"""
        
        return html
        




if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')
    

