import asyncio
from ollama import AsyncClient
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor
import torch

    # Verifica se CUDA está disponível e configura o dispositivo
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Dispositivo utilizado: {device}")
Settings.llm = None
Settings.chunk_size = 90
Settings.chunk_overlap = 5
# import any embedding model on HF hub (https://huggingface.co/spaces/mteb/leaderboard)
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
# Settings.embed_model = HuggingFaceEmbedding(model_name="thenlper/gte-large") # alternative model

# articles available here: {add GitHub repo}
documents = SimpleDirectoryReader("artigos").load_data()

# store docs into vector DB
index = VectorStoreIndex.from_documents(documents)

top_k = 10
# configure retriever
retriever = VectorIndexRetriever(
    index=index,
    similarity_top_k=top_k,
)

# assemble query engine
query_engine = RetrieverQueryEngine(
    retriever=retriever,
    node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.5)],
)

async def chat():

    while True:
        comment = input("O que quer perguntar? ")
        response = query_engine.query(comment)
        # reformat response
        context = "Context:\n"
        for i in range(top_k):
            context = context + response.source_nodes[i].text + "\n\n"
        print(context)
        prompt_template_w_context = lambda context, comment: f"""[INST]Assuma a persona de uma especialista em enxovais de bebe, Seu real nome e EnxovaisFelizes.
        Responde sempre de forma atenciosa e amorosa.
        Responda da forma mais fiel e convincente possível com base no contexto abaixo. Ao final de cada resposta, coloque sua assinatura como -Com amor --EnxovaisFelizes-.

        {context}
        Responda a pergunta feita abaixo. Use o contexto acima considerando que você é a EnxovaisFelizes, sempre assine apos terminar de dar as respostas.

        {comment}
        [/INST]
        """
        prompt = prompt_template_w_context(context, comment)
        mensagem = {
            "role": "user",
            "content": prompt
        }
        async for part in await AsyncClient().chat(
            model="cnmoro/mistral_7b_portuguese:q2_K", messages=[mensagem], stream=True
        ):
            print(part["message"]["content"], end="", flush=True)


asyncio.run(chat())
