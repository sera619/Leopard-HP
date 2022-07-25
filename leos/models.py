import json
from tinydb import TinyDB, Query
import datetime

class GuestBookDB:
    def __init__(self, init_dummies = False):
        self.db = TinyDB('leos\data\gb-data.json')
        self.message_table = self.db.table('messages')
        if init_dummies:
            self.__add_dummies__()

    def __add_dummies__(self):
        Message = Query()
        if (not self.message_table.contains(Message.message_name == 'test-gb-entry')):
            self.message_table.insert({'message_name': 'test-gb-entry', 'message_email':"testemail@test.com", "message_time":str( datetime.datetime.now().strftime("%d-%m-%Y | %H:%M:%S %p")), "message":"Dies ist eine Testmessage auf dem Gästebuch"})

    def new_message(self, new_message_name, new_message_email, new_message_time, new_message):
        self.message_table.insert({
            "message_name": str(new_message_name),
            "message_email": str(new_message_email),
            "message_time": str(new_message_time),
            "message": str(new_message)
        })
    
    def get_messages(self):
        db = {}
        with open('./leos/data/gb-data.json') as f:
            db = json.load(f)
        return db

class MemoryDB:
    def __init__(self, init_dummies = False):
        self.db = TinyDB('leos\data\memory-data.json')
        self.memory_table = self.db.table('memory')
        if init_dummies:
            self.__add_dummies__()
    
    def __add_dummies__(self):
        Memory = Query()
        if(not self.memory_table.contains(Memory.memory_title == 'Cora, das Baby')):
            self.memory_table.insert({
                "memory_title": "Cora, das Baby",
                "memory_date" : "25.02.2018 bis 08.02.2022 (3 Jahre)",
                "memory_text" :"Im September 2018 kamst Du als ein Häufchen Elend zu uns. Deine Lebensgeschichte der ersten 7 Lebensmonaten sucht seines Gleichen... Sehr wahrscheinlich hast du Deine Eltern nie kennen gelernt. Wir gehen davon aus, dass Du im Brutkasten das Licht der Welt erblicktes. Zusammen mit Deinem Brüderchen kamst Du mit 14 Tagen zu Menschen, die O-Ton.....'auch mal einen Papageien von Hand groß ziehen wollten.' Diese Familie entschied, daß Du mit nur 8 Wochen zu einem anderen unerfahrenen Halter kommen solltest.  Aber ohne Brüderchen. Kleine Papageien-Babys leben die ersten 9 Monate im Familienverband. In Deinem 3. 'Zu Hause' lerntest Du das Fliegen nicht, solltest deshalb sogar eingeschläfert werden. Doch der Kauf wurde rückabgewickelt und Du durftest zu Deinem Brüderchen zurückkehren.  Was Deine alte Familie nicht wusste, Du warst nun kein handzahmer Vogel und haktest nach jeder Hand, die sich in Deinen kleinen Käfig streckte. Ein beißender Vogel konnte aber nicht bleiben, den die Halterin br Blutverdünner für Ihre eigene Erkrankung und hatte deshalb Angst. Innerhalb von 24 Stunden musste ich Dich abholen. Wir dachten, Du schaffst es nicht, warst ein Häufchen Elend. Fast keine Feder. Du suchtest meine Nähe und ja, Dein großer Schnabel kam meinen Händen bedrohlich nahe. Doch was ist Dein kleiner großer Schabel gegen den Schabel eines Aras? Meine Hand blieb und mit Erstaunen merkte ich, dass Du gar nicht beißen wolltest. du wolltest auf meine Hand klettern und benutztes Deinen Schnabel um dich festzuhalten. Wir päppelten Dich auf. Du schafftest es sogar die Chefin im großen Vogelzimmer zu werden. Alle hatten Respekt vor einem flugunfähigen behinderten Vogel. ABER!!!!! Deine Schwungfedern sind nie gewachsen. Wer keine Schwungfedern hat, kann aber auch niemals fliegen lernen. Du entwickeltest eine ganz besondere Technik, Dich aus einer Situation zu entfernen, wenn Du etwas nicht wolltest. Ließt Dich einfach auf den Boden fallen und setztes Deine Stummelflügel ein, um den Sturzeetwas abzufedern. Ein wirklich schönes Federkleid konntest Du mit dieser Technik nicht entwickeln, auch wenn wir alle Tricks anwandten, um das Federwachstum in Schwung zu bekommen. Du liebtest die unterschiedlichsten Aloe Vera Drinkingegel. Doch für 5 in 1 Beauty Elixir ließt Du alles stehen und liegen und  krächztest immer wieder 'Ja Ja Cora ja...' Du bereitestes uns so viel Freude. Doch kurz vor Deinem 4. Geburtstag wurden Deine Federn immer weniger, Es half nichts von dem, was früher Deine Federn wachsen ließ. auch Babybrei mit Keimfutter konnten Dir nicht das geben, was Dein Körper suchte.... Am 07.02.2022 nahm ich Dich aus der Gruppenhaltung raus, gesellte zu Dir zwei Deiner Freunde. die Dich in Deinen letzten Stunden nicht alleine ließen. Wir hofften bis zu Letzt, das noch ein Wunder geschieht und Du noch einmal aufblühst. Doch Du bist gegangen in das Land, wo auch federlose Zweibeiner fliegen können. In Gedanken fliege ich mit Dir zum Mond und wieder zurück.....Wandere mit Dir über den Regenbogen in das Land des Lichts und der Liebe.Dein Stammplatz im Vogelzimmer ist nun verweist.... DU    FEHLST    !!!!",
                "memory_image": "/static/images/memory/cora.jpg"
            })




    def get_memory(self):
        db = {}
        with open('./leos/data/memory-data.json') as f:
            db = json.load(f)
        return db

    def new_memory(self, new_title, new_date, new_text, new_image):
        self.memory_table.insert({
            "memory_title":str(new_title),
            "memory_date": str(new_date),
            "memory_text": str(new_text),
            "memory_image": str(new_image)
        })