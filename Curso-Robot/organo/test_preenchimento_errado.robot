*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Verificar se ao preencher os campos do formulário corretamente os dados são inceridos na lista e se um novo card é criado no time esperado
    Dado que eu acesse o Organo
    E preencha os campos do formulário
    E clique no botão criar card
    Então identificar o card no time esperado

*** Keywords ***
Dado que eu acesse o Organo
    Open Browser    url=http://localhost:3000/    browser=Chrome

E não preencha os campos do formulário
    Input Text    ${CAMPO_NOME}     Carlos
    Input Text    ${CAMPO_CARGO}     Eqngenheiro de teste
    Input Text    ${CAMPO_IMAGEM}    https://picsum.photos/200/300
    Click Element    ${CAMPO_TIME}
    Click Element    ${PROGRAMACAO}

E clique no botão criar card
    Click Element    form-botao

Então identificar o card no time esperado
    Element Should Be Visible    class:colaborador