from django.shortcuts import render, redirect
from .models import Todo
from random import choice

listofemojies = {
   "Grinning 😃",
   "Smile 😄",
   "Grin 😁",
   "laughing 😆",
   "Sweat Smile 😅",
   "LOL 🤣",
   "Joy 😂",
   "Ironic Smile 🙂",
   "Sarcasm 🙃",
   "Melt 🫠",
   "Wink 😉",
   "Blush 😊",
   "Angel 😇",
   "Love 🥰",
   "Heart Eye 😍",
   "Star Eye 🤩",
   "Kiss 😘",
   "Kiss 😗",
   "Kissy 😚",
   "Smoochm 😙",
   "In Pain 🥲",
   "Yum 😋",
   "Tongue Out 😛",
   "Crazy 😜",
   "Mad 🤪",
   "Idiot 😝",
   "Ching-Ching 🤑",
   "Hug 🤗",
   "Blushing Smile 🤭",
   "Ooh 🫢",
   "Shy 🫣",
   "Silent 🤫",
   "Thinking 🤔",
   "Salute 🫡",
   "Lip Sealed 🤐",
   "Sus 🤨",
   "No Intrest 😐",
   "Not Intrested 😑",
   "No Words 😶",
   "Foggy 🌫️",
   "Mmm 😏",
   "Sad 😒",
   "No Idea 🙄",
   "Displeasure 😬",
   "Shocked 😮",
   "Gas 💨",
   "Lier 🤥",
   "Peace 😌",
   "Demotivated 😔",
   "Sleepy 😪",
   "Hungry 🤤",
   "Sleep 😴",
   "Mask 😷",
   "Ill 🤒",
   "ICU 🤕",
   "Disgusting 🤢",
   "Vomit 🤮",
   "Sneez 🤧",
   "Hot 🥵",
   "Cool 🥶",
   "Drowsy 🥴",
   "Dead 😵",
   "Wish ‍💫",
   "Mind Blow 🤯",
   "Dashing 😎",
   "Nerd 🤓",
   "Detective 🧐",
   "Please 🥺",
   "Happy Tears 🥹",
   "Scared 😨",
   "Tensed 😰",
   "Emotional 😢",
   "Weeping 😭",
   "Shocking 😱",
   "Angry 😡",
   "Cursing 🤬",
   "Happy Devil 😈",
   "Angry Devil 👿",
   "Skull 💀",
   "RIP ☠️",
   "Shit 💩",
   "Joker 🤡",
   "Oger 👹",
   "Goblin 👺",
   "Ghost 👻",
   "Alien 👽",
   "Monster 👾",
   "Robo 🤖",
   "Cat 😺",
   "Cat Laughting 😹",
   "Cat Love 😻",
   "Cat YES 😼",
   "Cat Kiss 😽",
   "Not See 🙈",
   "Not Listen 🙉",
   "Shush 🙊",
   "KISS 💋",
   "Love Letter 💌",
   "Heart Beat 💓",
   "Heart Break 💔",
   "Heart Red ❤️",
   "Fire 🔥",
   "Heart Orange 🧡",
   "Heart Yellow 💛",
   "Heart Green 💚",
   "Heart Blue 💙",
   "Heart Purple 💜",
   "Heart Brown 🤎",
   "Heart Black 🖤",
   "Heart White 🤍",
   "100% 💯",
   "Blash 💥",
   "Filthy 💦",
   "Bomb 💣",
}


# Create your views here.
def index(request):
    todos = Todo.objects.all()
    if request.method == "POST" and request.POST["title"] != "":
        description = request.POST["description"]
        
        if description == "":
            description = "no description"
        mood = request.POST["mood"]
        new_todo = Todo(
            title=(mood[-1:] + request.POST["title"]),
            description=description,
        )
        new_todo.save()
        return redirect("/")
    return render(request, "index.html", {"todos": todos, "emojies": listofemojies})


def delete(request, pk):
    myObjectRef = Todo.objects.get(id=pk)
    myObjectRef.delete()
    return redirect("/")


def description(request, pk):
    myobj = Todo.objects.get(id=pk)
    return render(request, "description.html", {"todo": myobj})
