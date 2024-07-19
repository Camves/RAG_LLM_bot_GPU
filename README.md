# Projeto de Consulta Automatizada através da aplicação do método RAG a LLM's

Este projeto implementa um sistema de consulta automatizada usando modelos de linguagem e embeddings. A persona utilizada nas respostas é a EnxovaisFelizes, uma especialista atenciosa e amorosa em enxovais de bebê.

## Pré-requisitos

- Python 3.8+
- Biblioteca `ollama`
- Biblioteca `llama_index`
- Biblioteca `torch`
- Biblioteca `asyncio`
- CUDA (opcional, para aceleração com GPU)

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Instale as dependências:

    ```bash
    pip install ollama llama_index torch
    ```

## Configuração

Certifique-se de que os artigos estão disponíveis na pasta `artigos`. O script lê os documentos dessa pasta para armazená-los no banco de dados vetorial.

## Uso

Execute o script para iniciar a consulta:

```bash
python seu_script.py
```
Durante a execução, você será solicitado a inserir uma pergunta. A EnxovaisFelizes responderá com base no contexto dos artigos disponíveis.

Exemplo de Pergunta
```
O que quer perguntar?
```
```
Qual é o melhor tecido para enxovais de bebê?
```
A resposta será gerada pela EnxovaisFelizes, incluindo a assinatura:

```
[Resposta da EnxovaisFelizes com base no contexto]
-Com amor --EnxovaisFelizes-
```

## Estrutura do Código
- device: Verifica se CUDA está disponível e configura o dispositivo.
- Settings: Configurações para o modelo de linguagem e embedding.
- SimpleDirectoryReader: Lê os documentos da pasta artigos.
 -VectorStoreIndex: Armazena os documentos em um banco de dados vetorial.
- VectorIndexRetriever: Configura o recuperador para obter os documentos mais similares.
- RetrieverQueryEngine: Monta o motor de consulta que processa as perguntas.
- chat(): Função assíncrona que lida com as interações do usuário e gera respostas.

## Contribuição
Sinta-se à vontade para fazer um fork do projeto, abrir issues ou pull requests.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
