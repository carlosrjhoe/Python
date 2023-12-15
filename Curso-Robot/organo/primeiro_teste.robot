*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Abrir navegador e acessar o site do organo
    Open Browser    url=http://localhost:3000/    browser=Chrome

Preencher os campos do formulário
    Input Text    id:form-nome      Carlos
    Input Text    id:form-cargo     Eqngenheiro de teste
    Input Text    id:form-imagem    https://picsum.photos/200/300
    Click Element    class:lista-suspensa
    Click Element    //option[contains(., 'Programação')]
    sleep    10s
    Click Element    form-botao
    Element Should Be Visible    class:colaborador
    sleep    10s
