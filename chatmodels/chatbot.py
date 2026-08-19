from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

model = ChatMistralAI(
    model = "mistral-small-2603", 
    temperature=0.9, max_tokens=20
)

messages = [
    SystemMessage(content="you are a funny agent")
]

print("------------ Welcome type 0 to exist the applicaton -------------------")


print("choose your AI Model")
print("press 1 for angry mode")
print("press 2 for funny mode")

choice = int(input("tell your response"))

if choice == 1:
    mode = "you are an angry agent. you response aggressively and impatiently"
elif choice == 2:
    mode = "you are a very funny model . you response with humat and jokes"   


while True:
    prompt = input("You : ")
    messages.append(HumanMessage(content=prompt))
    if prompt == "0" :
        break;
    
    
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))

    print("Bot : " ,response.content)