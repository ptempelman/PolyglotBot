import whisper

import os
import re
import os.path as osp

import openai

from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
from pydub import AudioSegment

from validate_openai_key import load_api_key, retrieve_api_key

if __name__ == "__main__":
    green_text = "\033[92m"

    api_key = retrieve_api_key()

    topic = input(
        f"{green_text}What kind of conversation would you like to simulate?\n"
    )
    language = input(f"{green_text}In what language?\n")

    conversation_memory_rep: ConversationBufferMemory = ConversationBufferMemory()
    ai: ConversationChain = ConversationChain(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo", api_key=api_key),
        memory=conversation_memory_rep,
    )

    print(
        ai.invoke(
            f"{green_text}{green_text}Someone is trying to learn {language}, by talking about {topic}. If there are two roles, simulate the more passive one (e.g. be the buyer when talking to a car salesperson), from now on respond in {language}, please start off the conversation now"
        )["response"]
    )

    while True:

        # recording =

        # model = whisper.load_model("tiny")
        # result = model.transcribe("example.wav")
        # print(result["text"])

        human_response = input()
        ai_response = ai.invoke(human_response)["response"]
        print(f"{green_text}{ai_response}")
