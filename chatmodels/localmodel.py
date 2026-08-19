from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="HuggingFaceH4/zeyr-7b-beta",  # don't download it ,it is so bulky
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,
    ),

)

chat_model = ChatHuggingFace(llm=llm)

result = chat_model.invoke("what is ai/ml?")
print(result.content)