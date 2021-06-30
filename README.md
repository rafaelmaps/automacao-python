# automacao-python
O script python existente nesse repositório, foi desenvolvido para um Caso de Uso da empresa Shopper.com.br

O cenário tratado é o seguinte:
Um usuário previamente cadastrado na plataforma da Shopper deseja comprar a quantidade maxima de um determinado produto. 
No passo para efetuação do pagamento, serão inseridos dados inválidos de cartão de crédito e a plataforma deve barrar a compra notificando o usuário sobre tal inconsistência.

Premissas para execução do teste:<br/>
  Necessário instalação do driver do Mozila Firefox para que o selenium possa ser executado(https://github.com/mozilla/geckodriver/releases).
  o diretório onde a instalação for realizada precisa ser referenciado na variavel de ambiente 'path' do windows.
  
  No diretório de usuário onde o script irá ser executado, deve existir um arquivo de texto denominado "shopper_acesso.txt" com o seguinte contéudo:
  <br>[CREDENCIAIS]<br>
  email=<email_do_usuario><br>
  senha=<senha_do_usuario><br>

