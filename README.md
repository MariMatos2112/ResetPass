## ResetP@ss: Sistema para Mudança de Senhas de Rede do Hospital Universitário Clemente Farias (Montes Claros - MG)

### De onde surgiu a ideia...
Tudo começou no dia em que meu chefe, Kleber, me disse: “Temos que desenvolver um sistema que recupera as senhas de rede dos usuários”. 
Logo de cara pensei no nosso queridinho da programação: o Python. <br>
E foi ele mesmo que eu usei para implementar todo o sistema.

### Tecnologias usadas... 
* Flask (Python)
* SQLite
* HTML5
* Vanilla JS
* Bootstrap
* Powershell

### Funcionamento...
O ResetP@ss é bem fácil de utilizar e é bastante intuitivo. <br>
Primeiramente, é necessário logar com seu usuário. (Obs: O mesmo deve estar cadastrado no banco de dados SQLite do sistema) <br>
Logo em seguida, uma página para pesquisar um usuário por seu login na rede é renderizada. <br>
Basta digitar o login no campo disponível, confirmar que o usuário em questão é aquele que você está procurando e pronto! <br>
A senha do user é alterada para uma senha padrão. <br> 
![image](https://user-images.githubusercontent.com/67180109/140191219-eaaa12f5-3b5f-46a9-8be0-3c5cba427814.png)

### Diferença que o ResetP@ss faz dentro do Hospital Universitário...
A recuperação das senhas de rede tornou-se um processo muito mais rápido, fácil e seguro, pois permitiu que as senhas perdidas fossem recuperadas com apenas alguns cliques e sem acesso direto ao servidor.

### Observações...
* Esse repositório não apresenta nenhum tipo de informação condifencial do Hospital Universitário Clemente de Farias;
* É necessário que o banco de dados SQLITE seja criado manualmente;
* É necessário que seja feito o comando export <i>FLASK_APP=nome_arquivo.py</i> para configurar uma variável de ambiente;
* O sistema só funcionará em ambiente de Active Directory, pois ele comunica diretamente com o mesmo.

### Rodando o programa...
Após as observações acima serem consideradas, basta executar o comando <i>flask run</i> para iniciar o sistema.


