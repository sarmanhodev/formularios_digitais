//BUSCA CEP SUBLOCADOR
async function getCepSublocador() {
    var entrada_cep = document.querySelector("#entrada_cep");

    let url = "https://viacep.com.br/ws/" + entrada_cep.value + "/json/";
    try {
        let res = await fetch(url);
        return await res.json();
    } catch (error) {
        console.log(error);
    }
}


async function renderCepSublocador() {
    let dados = await getCepSublocador();
    let html = '';
    let htmlSegment = `
    <div class='row m-1'>
        <div class='col-md-6'><div class="form-floating">
            <input type="text" class="form-control" readonly value="${dados.logradouro}" name="logradouro_sublocador" id="logradouro_sublocador" placeholder="Logradouro">
            <label for="logradouro_sublocador">Logradouro</label>
        </div></div>\
        <div class='col-md-6'><div class="form-floating">
            <input type="text" class="form-control" readonly value="${dados.bairro}" name="bairro_sublocador" id="bairro_sublocador" placeholder="Bairro">
            <label for="bairro_sublocador">Bairro</label>
        </div></div>
    </div> <br>\
    <div class='row m-1'>
        <div class="col-md-6">
            <div class="form-floating">
                <input type="text" class="form-control"   name="numero_residencia_sublocador" id="numero_residencia_sublocador" placeholder="Número">
                <label for="numero_residencia_sublocador">Número</label>
            </div>
        </div>

        <div class="col-md-6">
            <div class="form-floating">
                <input type="text" class="form-control text-uppercase"  name="complemento_residencia_sublocador" id="complemento_residencia_sublocador" placeholder="Complemento">
                <label for="complemento_residencia_sublocador">Complemento</label>
            </div>
        </div>
    </div>
    <br>
    <div class='row m-1'>
    <div class='col-md-6'><div class="form-floating">
        <input type="text" class="form-control" readonly value="${dados.localidade}" name="localidade_sublocador" id="localidade_sublocador" placeholder="Localidade">
        <label for="localidade_sublocador">Localidade</label>
    </div></div>\
    <div class='col-md-6'><div class="form-floating">
        <input type="text" class="form-control" readonly value="${dados.uf}" name="uf_sublocador" id="uf_sublocador" placeholder="UF">
        <label for="uf_sublocador">UF</label>
    </div></div>\
    </div><br>`;

    html += htmlSegment;
    console.log(dados.cep)
    console.log(dados.logradouro)
    console.log(dados.bairro)
    console.log(dados.localidade)
    console.log(dados.uf)
    let container = document.querySelector('#recebe_dados');
    container.innerHTML = html;
}

renderCepSublocador();


//BUSCA CEP SUBLOCATÁRIO
async function getCepSublocatario() {
    var entrada_cep = document.querySelector("#entrada_cep_sublocatario");

    let url = "https://viacep.com.br/ws/" + entrada_cep.value + "/json/";
    try {
        let res = await fetch(url);
        return await res.json();
    } catch (error) {
        console.log(error);
    }
}


async function renderCepSublocatario() {
    let dados = await getCepSublocatario();
    let html = '';
    let htmlSegment =  `
    <div class='row m-1'>
        <div class='col-md-6'><div class="form-floating">
            <input type="text" class="form-control" readonly value="${dados.logradouro}" name="logradouro_sublocatario" id="logradouro_sublocatario" placeholder="Logradouro">
            <label for="logradouro_sublocatario">Logradouro</label>
        </div></div>\
        <div class='col-md-6'><div class="form-floating">
            <input type="text" class="form-control" readonly value="${dados.bairro}" name="bairro_sublocatario" id="bairro_sublocatario" placeholder="Bairro">
            <label for="bairro_sublocatario">Bairro</label>
        </div></div>
    </div> <br>\
    <div class='row m-1'>
        <div class="col-md-6">
            <div class="form-floating">
                <input type="text" class="form-control"   name="numero_residencia_sublocatario" id="numero_residencia_sublocatario" placeholder="Número">
                <label for="numero_residencia_sublocatario">Número</label>
            </div>
        </div>

        <div class="col-md-6">
            <div class="form-floating">
                <input type="text" class="form-control text-uppercase"  name="complemento_residencia_sublocatario" id="complemento_residencia_sublocatario" placeholder="Complemento">
                <label for="complemento_residencia_sublocatario">Complemento</label>
            </div>
        </div>
    </div>
    <br>
    <div class='row m-1'>
    <div class='col-md-6'><div class="form-floating">
        <input type="text" class="form-control" readonly value="${dados.localidade}" name="localidade_sublocatario" id="localidade_sublocatario" placeholder="Localidade">
        <label for="localidade_sublocatario">Localidade</label>
    </div></div>\
    <div class='col-md-6'><div class="form-floating">
        <input type="text" class="form-control" readonly value="${dados.uf}" name="uf_sublocatario" id="uf_sublocatario" placeholder="UF">
        <label for="uf_sublocatario">UF</label>
    </div></div>\
    </div><br>`;

    html += htmlSegment;
    console.log(dados.cep)
    console.log(dados.logradouro)
    console.log(dados.bairro)
    console.log(dados.localidade)
    console.log(dados.uf)
    let container = document.querySelector('#recebe_dados_sublocatario');
    container.innerHTML = html;
}

renderCepSublocatario();


//BUSCA CEP IMÓVEL
async function getCepImovel() {
    var entrada_cep = document.querySelector("#entrada_cep_imovel");

    let url = "https://viacep.com.br/ws/" + entrada_cep.value + "/json/";
    try {
        let res = await fetch(url);
        return await res.json();
    } catch (error) {
        console.log(error);
    }
}


async function renderCepImovel() {
    let dados = await getCepImovel();
    let html = '';
    let htmlSegment =  `
    <div class='row m-1'>
        <div class='col-md-6'><div class="form-floating">
            <input type="text" class="form-control" readonly value="${dados.logradouro}" name="logradouro_imovel" id="logradouro_imovel" placeholder="Logradouro">
            <label for="logradouro_imovel">Logradouro</label>
        </div></div>\
        <div class='col-md-6'><div class="form-floating">
            <input type="text" class="form-control" readonly value="${dados.bairro}" name="bairro_imovel" id="bairro_imovel" placeholder="Bairro">
            <label for="bairro_imovel">Bairro</label>
        </div></div>
    </div> <br>\
    <div class='row m-1'>
        <div class="col-md-6">
            <div class="form-floating">
                <input type="text" class="form-control"   name="numero_imovel" id="numero_imovel" placeholder="Número">
                <label for="numero_imovel">Número</label>
            </div>
        </div>

        <div class="col-md-6">
            <div class="form-floating">
                <input type="text" class="form-control text-uppercase"  name="complemento_imovel" id="complemento_imovel" placeholder="Complemento">
                <label for="complemento_imovel">Complemento</label>
            </div>
        </div>
    </div>
    <br>
    <div class='row m-1'>
    <div class='col-md-6'><div class="form-floating">
        <input type="text" class="form-control" readonly value="${dados.localidade}" name="localidade_imovel" id="localidade_imovel" placeholder="Localidade">
        <label for="localidade_imovel">Localidade</label>
    </div></div>\
    <div class='col-md-6'><div class="form-floating">
        <input type="text" class="form-control" readonly value="${dados.uf}" name="uf_imovel" id="uf_imovel" placeholder="UF">
        <label for="uf_imovel">UF</label>
    </div></div>\
    </div><br>`;

    html += htmlSegment;
    console.log(dados.cep)
    console.log(dados.logradouro)
    console.log(dados.bairro)
    console.log(dados.localidade)
    console.log(dados.uf)
    let container = document.querySelector('#recebe_dados_imovel');
    container.innerHTML = html;
}

renderCepImovel();


function getDados() {
    $("#sublocador").val($("#nome_sublocador").val());
    $("#sublocatario").val($("#nome_sublocatario").val());
}

function verifica_campo(){
    const uf = document.getElementById("sigla_uf");

    if(uf.value.length >1  != ""){
        $("#insere_btn").html('<button class="btn btn-success card_deal" type="submit">SALVAR</button>');
       
    }else{
        $("#insere_btn").html("<p>Preencha todos os campos!</p>");
    }
}