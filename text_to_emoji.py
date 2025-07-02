from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class GetText(BaseModel):
    text: str

emoji_list = {
    "happy": "😊",
    "sad": "😢",
    "love": "❤️",
    "angry": "😡",
    "tired": "😴",
    "cool": "😎",
    "surprised": "😲",
    "crying": "😭",
    "laugh": "😂",
    "confused": "😕",
}


@app.post("/")
async def text(req:GetText):
    words = req.text.split()

    new = []

    for word in words:
        key = word.lower().strip(",.?!")
        emoji = emoji_list.get(key,"")
        new.append(word + (f"{emoji}" if emoji else ""))

    return {
        "Output": " ".join(new)
    }