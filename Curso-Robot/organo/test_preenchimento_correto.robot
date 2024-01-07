*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${CAMPO_NOME}    id:form-nome
${CAMPO_CARGO}    id:form-cargo
${CAMPO_IMAGEM}    id:form-imagem
${CAMPO_TIME}    class:lista-suspensa
${CAMPO_CARD}    id:form-botao
${PROGRAMACAO}    //option[contains(., 'Programação')]
${FRONT_END}    //option[contains(., 'Front-End')]
${DADOS}    //option[contains(., 'Dados')]
${DEVOPS}    //option[contains(., 'Devops')]
${UX}    //option[contains(., 'UX e Design')]
${MOBILE}    //option[contains(., 'Mobile')]
${INOVACAO}    //option[contains(., 'Inovação')]

*** Test Cases ***
Verificar se ao preencher os campos do formulário corretamente os dados são inseridos na lista e se um novo card é criado no time esperado
    Dado que eu acesse o Organo
    E preencha os campos do formulário
    E clique no botão criar card
    Então identificar o card no time esperado

*** Keywords ***
Dado que eu acesse o Organo
    Open Browser    url=http://localhost:3000/    browser=Chrome

E preencha os campos do formulário
    Input Text    ${CAMPO_NOME}     Carlos
    Input Text    ${CAMPO_CARGO}     Eqngenheiro de teste
    Input Text    ${CAMPO_IMAGEM}    https://picsum.photos/200/300
    Click Element    ${CAMPO_TIME}
    Click Element    ${PROGRAMACAO}

E clique no botão criar card
    Click Element    form-botao

Então identificar o card no time esperado
    Element Should Be Visible    class:colaborador

# ==============================================================================
# Test Preenchimento Correto
# ==============================================================================
# Verificar se ao preencher os campos do formulário corretamente os ... 
# DevTools listening on ws://127.0.0.1:58259/devtools/browser/3c93d528-d715-41d0-afd4-a56e9af87dc3
# Verificar se ao preencher os campos do formulário corretamente os ... | PASS |
# ------------------------------------------------------------------------------
# Test Preenchimento Correto                                            | PASS |
# 1 test, 1 passed, 0 failed
# ==============================================================================