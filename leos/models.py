from email.message import Message
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
            self.message_table.insert({'message_name': 'test-gb-entry', 'message_email':"testemail@test.com", "message_time":str( datetime.datetime.now().strftime("%d/%m/%Y | %H:%M:%S %p")), "message":"Dies ist eine Testmessage auf dem Gästebuch", 'message_status': 'False'})
            self.message_table.insert({'message_name': 'test-gb-entry2', 'message_email':"testemail@test.com", "message_time":str( datetime.datetime.now().strftime("%d/%m/%Y | %H:%M:%S %p")), "message":"Dies ist eine weitere Testmessage auf dem Gästebuch", 'message_status': 'True'})


    def new_message(self, new_message_name, new_message_email, new_message_time, new_message):
        self.message_table.insert({
            "message_name": str(new_message_name),
            "message_email": str(new_message_email),
            "message_time": str(new_message_time),
            "message": str(new_message),
            "message_status": 'False'
        })
    
    def change_message_status(self, message_name):
        Message = Query()
        edit_message = self.message_table.get(Message.message_name == str(message_name))
        if edit_message['message_status']== "True":
            edit_message['message_status'] = "False"
        else:
            edit_message['message_status']= "True"
        self.message_table.update(edit_message, Message.message_name == str(message_name))

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
        if(not self.memory_table.contains(Memory.memory_title == 'Marti, der Knutscher')):
            self.load_backup_data()

    def load_backup_data(self):
        self.memory_table.insert({
            "memory_title":"Paris",
            "memory_date":"31.05.2003 bis 21.07.2022 (19 Jahre)",
            "memory_text":".... die letzten Wochen und Monate waren SOOOO schwer, für Dich, für mich und für alle, die an Deinem Schicksal Anteil genommen haben. Du bedeutest uns SOOOO viel und der Schmerz ist unendlich groß....Ostern bist Du an einem Bandscheibenvorfall erkrankt. Du bist zwar bei mir geboren, doch gehörtet hast mir nicht. Kraft Gesetz wurdest Du und Dein Bruder Troja vererbt, doch die Familie Deines Herrchens interessiert sich nicht für Euch.  Nicht einmal der Brief, daß Du erkrankt bist und eine Entscheidung getroffen werden muß, veränderte etwas am Verhalten der Erben. Du und Dein Bruder, Ihr Zwei seit als 'HERRENLOSE RAUBKATZEN' anzusehen. Doch der deutsche Staat macht es sich leicht. Antwort vom Veterinäramt: 'Wieso herrenlos, Sie füttern sie doch...' anstelle den Erben auf die Füße zu treten, betitelte mich die Behörden als 'Zustandstörer'' (Nach OBG) und ließen uns im Stich.  Aber wie kann ich denn über Leben und Tod entscheiden, wenn Du mir nicht gehörst? Monate sind vergangen, bis eine 'Kommission' kam und entschieden hat, daß Du gehen darfst. Diese 'Kommission' hätte im April/Mai kommen müssen, als es Dir so schlecht ging, und ich Dir das Futter vor die Nase schieben musste. Jetzt, zum Schluss hattest Du gelernt mit Deiner Behinderung zu leben, warst vom Kopf her wieder Raubtier. Und genau dass ist es, was den letzten Gang von heute morgen SOOOO schwer gemacht hat Fakt ist, besser wäre es nie mehr geworden. Du bist bis zum Schluss eine Schönheit gewesen und bei meinen gestrigen letzten Streicheleinheiten zeigtest Du mir noch einmal Dein 'Schelmgesicht'. Dieses Gesicht, dass Du aufsetztest, wenn Dir ein Gedanke durch den Kopf schoss und Du an irgend  einen Blödsinn dachtest. Oder Du einfach nur meine Aufmerksamkeit testen wolltest. Erinnerst Du Dich noch, wie Du als Baby zu einem Park-Chef sagtest: 'Streck mal Deine Nase nicht zu sehr in mein Requisit, das gibt eine Kralle von mir!' Oder wie Du bei einem Kunstprojekt durch Cappuchiotassen aus Platik gerannt bist und viele dabei ganz viel Plastik umfiele. Das nannte man dann Kunst! Erinnerst Du Dich an das Fotoshooting für Panasonic beim Fotoshooting hast und Dein Herrly  Deine Zeichen nicht verstand, dass Du genug hattest?' Du hast  schon recht lieber  Paris, wer nicht hören kann, muss fühlen. Wie schön war es, Dich, auch Jahre später noch,  Europaweit auf  Werbeplakaten zu sehen.Nun hast Du diese Tierärzte gehört... und später dieser Blick... als ob Du mir sagen wolltest, 'Sei nicht traurig, es ist Zeit für mich zu gehen..... Frauly, du hast alles richtig gemacht. Hast uns Brüder 2019 'geklaut' um uns zum Tierarzt zu bringen. Mein Eckzahn tat so weh. Frauly Du bist dafür wegen Leopardendiebstahl angezeigt wurden. Dass hätte unser Herrly nicht tun dürfen. Du liebes Frauly, hast uns ein neues zu Hause gegeben und Dich mit bösen Nachbarn auseinander gesetzt. Wie gerne hätte ich mit Dir noch einmal in der Trainingsmanege gestanden, doch diese Manege durfte nicht gebaut werden. Ein Baustopp verhinderte dieses bis heute.  Dafür würde ich den Nachbarn am liebsten in den Hintern beißen. Du lieber Troja,  bekommst nun meine Gehegeseite, darfst in meiner Schlafkiste schlafen, aber nur, wenn Du Frauly keinen Ärger machst. Bleib gesund kleiner Bruder und werde mindestens so alt wie Onkel Zeus, damit sich der Bau des Geheges wenigstens gelohnt hat. ' Lieber Paris, Du bist nun auf dem Weg zu unsere Tigerin Magic, wirst Onkel Zeus, dem schwarzen Panther wieder sehen, lernst Marti und die anderen Seebären kennen, und zuletzt wird Luna unsere Showhündin Dich lautstark begrüßen. Ihr alle gemeinsam diskutiert mit Deinem Herrly in Raubtiermanier was Recht und was Unrecht ist. Ja Paris, das ist es was ich in Deinem Blick gelesen habe -  ich habe Dich verstanden. Vom Kopf her lasse ich dich gehen, doch Mein Herz, das blutet..... Ganz besonders möchte ich mich bei der Handvoll Unterstützern bedanken, die in den letzten Tagen für die Tiere finanzielle Zuwendungen geschickt haben. Die TA-Kosten sind damit hoffentlich gedeckt. Mein Dank geht auch an die Tierarztpraxis Dr. Wagner. Das Beste Team!",
            "memory_image":"/static/images/memory/paris.jpg"
        })
        self.memory_table.insert({
            "memory_title": "Cora, das Baby",
            "memory_data": "25.02.2018 bis 08.02.2022 (4 Jahre)",
            "memory_text": "Im September 2018 kamst Du als ein Häufchen Elend zu uns. Deine Lebensgeschichte der ersten 7 Lebensmonaten sucht seines Gleichen.....Sehr wahrscheinlich hast du Deine Eltern nie kennen gelernt. Wir gehen davon aus, dass Du im Brutkasten das Licht der Welt erblicktes. Zusammen mit Deinem Brüderchen kamst Du mit 14 Tagen zu Menschen, die O-Ton... 'auch mal einen Papageien von Hand groß ziehen wollten.' Diese Familie entschied, daß Du mit nur 8 Wochen zu einem anderen unerfahrenen Halter kommen solltest.  Aber ohne Brüderchen. Kleine Papageien-Babys leben die ersten 9 Monate im Familienverband. In Deinem 3. 'Zu Hause' lerntest Du das Fliegen nicht, solltest deshalb sogar eingeschläfert werden. Doch der Kauf wurde rückabgewickelt und Du durftest zu Deinem Brüderchen zurückkehren.  Was Deine alte Familie nicht wusste, Du warst nun kein handzahmer Vogel und haktest nach jeder Hand, die sich in Deinen kleinen Käfig streckte. Ein beißender Vogel konnte aber nicht bleiben, den die Halterin brauchte Blutverdünner für Ihre eigene Erkrankung und hatte deshalb Angst. Innerhalb von 24 Stunden musste ich Dich abholen. Wir dachten, Du schaffst es nicht, warst ein Häufchen Elend. Fast keine Feder. Du suchtest meine Nähe und ja, Dein großer Schnabel kam meinen Händen bedrohlich nahe. Doch was ist Dein kleiner großer Schabel gegen den Schabel eines Aras? Meine Hand blieb und mit Erstaunen merkte ich, dass Du gar nicht beißen wolltest. du wolltest auf meine Hand klettern und benutztes Deinen Schnabel um dich festzuhalten. Wir päppelten Dich auf. Du schafftest es sogar die Chefin im großen Vogelzimmer zu werden. Alle hatten Respekt vor einem flugunfähigen behinderten Vogel. ABER!!!!!Deine Schwungfedern sind nie gewachsen. Wer keine Schwungfedern hat, kann aber auch niemals fliegen lernen. Du entwickeltest eine ganz besondere Technik, Dich aus einer Situation zu entfernen, wenn Du etwas nicht wolltest. Ließt Dich einfach auf den Boden fallen und setztes Deine Stummelflügel ein, um den Sturz etwas abzufedern. Ein wirklich schönes Federkleid konntest Du mit dieser Technik nicht entwickeln, auch wenn wir alle Tricks anwandten, um das Federwachstum in Schwung zu bekommen. Du liebtest die unterschiedlichsten Aloe Vera Drinkingegel. Doch für 5 in 1 Beauty Elixir ließt Du alles stehen und liegen und  krächztest immer wieder 'Ja Ja Cora ja...'' Du bereitestes uns so viel Freude. Doch kurz vor Deinem 4. Geburtstag wurden Deine Federn immer weniger, Es half nichts von dem, was früher Deine Federn wachsen ließ. auch Babybrei mit Keimfutter konnten Dir nicht das geben, was Dein Körper suchte.... Am 07.02.2022 nahm ich Dich aus der Gruppenhaltung raus, gesellte zu Dir zwei Deiner Freunde. die Dich in Deinen letzten Stunden nicht alleine ließen. Wir hofften bis zu Letzt, das noch ein Wunder geschieht und Du noch einmal aufblühst. Doch Du bist gegangen in das Land, wo auch federlose Zweibeiner fliegen können. In Gedanken fliege ich mit Dir zum Mond und wieder zurück.....Wandere mit Dir über den Regenbogen in das Land des Lichts und der Liebe. Dein Stammplatz im Vogelzimmer ist nun verweist.... DU    FEHLST    !!!!",
            "memory_image":"/static/images/memory/cora.jpg"
        })


        self.memory_table.insert({
            "memory_title": "Marti, der Knutscher",
            "memory_date":"16.04.2021 (ca 15 Jahre)",
            "memory_text": "Fassungslosigkeit macht sich bereit, als ich von Deinem Gang über die Regenbogenbrücke erfahren habe.5 Jahre teilten wir uns eine wundervolle Showzeit. Du wurdest in Spanien bei der berühmten Duss-Family geboren. Lebtest im sonnigen Süden, bis Deine Seebärenkollegen Dir den Rang in der Gruppe streitig machten. Bei Deinem letzten Streit hattest Du mehr als Pech. Eine Verletzung führte zur Erblindung auf dem linken Auge. Als 'Einäugiger Pirat' feiertest Du trotz Deiner Einschränkung Showerfolge der Extraklasse. Selbst das Ballbalancieren bekamst Du mit dieser Einschränkung hin. In der Seebärenschule erklärtets Du den Gästen, welchen Fisch Du am liebsten magst. Die Sprotte gabst Du mir (fast) immer wieder zurück. In Deiner Soloshow zeigtest Du in mehr als 20 min ALLES, und noch viel mehr, was eine sehr gut ausgebildete Showrobbe  lernen kann. Zusammen mit meiner Moderation und Deinem clowneskes Talent brachtest Du alle Gäste zum Lachen. Selbst im 'Trainingslager der Olympischen Robbenspiele' bist Du immer als Sieger vom Platz gegangen. 3 verschiedene Shows in weniger als 5 Jahren - keine andere Robbe war jemals so eng mit mir befreundet. Bei jeder Gelegenheit knutschtest Du mich ab.... mit Fischgeruch, immer ein WAHRES ERLEBNIS! Den kleinen Mamut nahmst Du  freundlich, nein liebevoll als Gefährten auf, verteidigst ihn sogar vor Marino, dem Du mit Deiner Körpergröße Respekt lerntest. 2020 endete unsere gemeinsame Zeit. Schweren Herzens lies ich Dich zurück... Und nun... nun bist Du gegangen...",
            "memory_image": "/static/images/memory/marti.jpg"
        })
        self.memory_table.insert({
            "memory_title":"Herbert de Larott",
            "memory_date": "13.08.1951 vus 20.03.2021",
            "memory_text": "14 Jahre lebten, arbeiteten, liebten und stritten wir uns gemeinsam durch einen Teil Deines Lebens. Erlebten Höhen und Tiefen, wie es kaum ein anderer erlebt.Deine große Liebe galt jedoch der Zauberei, speziell den Illusionen mit Raubtieren. Zeus war Dein ganzer Stolz. Als er damals ging, sah ich Dich das erste und einzigste Mal in Deinem Leben weinen. Niemand konnte den Platz von unserem Zeus einnehmen. Weder unsere anderen gefleckten Showstars, noch ich als Deine Partnerin. 2012 trennten sich unsere gemeinsamen Wege und doch blieb ich bis zu Deinem Tod am stärksten mit Dir verbunden. Bis zum Schluß bestimmtest Du zu großen Teilen mein Leben und auch über den Tod hinaus wirst Du mich weiterhin begleiten und beschäftigen. Unseren beiden Leopardenjungs geht es bei mir sehr gut und ich werde auf sie aufpassen. Ich verspreche Dir hier und jetzt und für alle, die das hier lesen. Ich werde alles mir mögliche tun, daß Troja und Paris mindestens genauso alt werden wie Dein Liebling Zeus. Unsere Jungs werden ihr neues wundervolles Zuhause so lange wie möglich bei bester Pflege und Gesundheit genießen. Dafür werde ich kämpfen, dass weißt Du Herbert, auch wenn Du zum Schluss so viel zerbrochen hast, was Du nicht los lassen wolltest. Das war mehr, als Du Dir hast vorstellen können und dennoch sind wir zwei für immer VERBUNDEN!",
            "memory_image": "/static/images/memory/herbert.jpg"
        })
        self.memory_table.insert({
            "memory_title": "Herbert das viel zu kurze Glück",
            "memory_date":"Ubekannt",
            "memory_text": "Flieg mit mir kleiner Herbert, aber bitte lass dazu Deine Federn ganz.... Deine Menschen erkannten im Alter von nur 2 Jahren, daß Dir irgend etwas fehlt. Du wurdest als einzelnes Jungtier von Menschen großgezogen, weil Deine Eltern es nicht konnten oder wollten. Du hattest  nie Gesellschaft, außer die Wildvögel in Deiner schönen Voliere im Garten. Das Dir das zu wenig war, erkannte Dein Frauchen und suchte bei uns Hilfe. Sie stand ohnmächtig neben Dir, wenn Du Attackenweise Deine Federn zerstörtest. Die Tierärzte verpassten Dir für Wochen eine Halskrause, die aber das Federnreißen und abbeissen nicht verhinderte. Dein Frauchen machte alles, aber auch wirklich alles, was man Ihr empfahl. Gab Dir leckere Vitamine und Deinen heiß geliebten Vogelbabybrei. Brachte Dich zum großen TA Check und als dieser da war und die Ärzte das o.k. zur Vergesellschaftung gaben, durftest Du in der Seniorenresidenz für Showtiere einziehen. Hier wartete das große Vogelzimmer auf Dich mit vielen gefiederten Freunden. Sogar 3 artgleiche Damen lächelten Dich an. Du vergaßt das rupfen und liebtest gemeinsam mit den anderen die Vitamine zu trinken, konntest gar nicht genug davon bekommen. Wir waren so stolz auf Dich und voller Zuversicht. Doch dieses Glück dauerte nur 4 Tage. Plötzlich lagst du ohne Grund krampfend auf dem Boden. Wir kämpften um Dich, doch diesen Kampf konnten wir nicht gewinnen. Ein Blick in die Laborwerte lieferte uns die Erklärung.Flieg kleiner Freund, flieg hinauf in eine Welt ohne Schmerzen und Leiden, wo Blutwerte nicht mehr von Bedeutung sind. Gib unseren Lieben dort oben all Dein Vertrauen und Du bekommst die Kuscheleinheiten, die Dir so wichtig sind. Du freundlicher liebevoller Vogel....wir vermissen Dich!",
            "memory_image": "/static/images/memory/herbert-vogel.jpg"
            
        })
        self.memory_table.insert({
            "memory_title": "Bengaltigerin Magic",
            "memory_date": "12.05.2008 bis 01.02.2021 (13 Jahre)",
            "memory_text": "Vor 8 Jahren wurde Dir über die Regenbogenbrücke geholfen. Deine Zeit auf diesem Planeten war auf Grund Deiner Epilepsie viel zu kurz. Eigentlich wäre Dein Leben bereits im Babyalter  vorbei gewesen. Mit 6 Wochen rettete ich Dir mit Mund zu Mund Beatmung das Leben. Die menschlichen teuren Medikamente ( Luminal ) halfen Dir die Anfälle zu unterdrückten.  Damit konntest Du ein glückliches Tigerleben führen und ich durfte Dich aufwachsen sehen. Unsere Beziehung war so  eng, dass ich Dir täglich Dein MedizinStück von Hand geben durfte.Du wurdest eine Schönheit, warst ein Star in der Panther Magic Show, aber vor allem, Du wurdest über alles geliebt. Als ich Dich 2012 verlassen musste zerbrach in mir mein Herz und meine Welt. Ich suchte Dir mit Freunden einen Zooplatz, doch Dein Herrchen ließ Dich dahin nicht gehen. Er entschied, dass Dein Weg die Regenbogenbrücke sein. Erst später erfuhr ich von Deinem Tod... Mich quälte es, dass ich Dir nicht anders helfen durfte. Du hast mit Sicherheit von oben gesehen, wie ich Deinen Leoparden Freunden 2019 geholfen habe. Für sie habe ich das Zuhause geschaffen, welches Ich Dir 2013 noch nicht geben konnte. Dieses Zuhause für Troja und Paris baute ich auch damit Du mir verzeihst. Und heute weiß ich,  Du hast mir verziehen. Nun kannst Du im Regenbogenland stolz erzählen,  mit wie viel Herz und Liebe Dein Lieblingsmensch Dir das Leben so angenehm wie möglich gemacht habt.  Du bist unvergessen!!!! Ich hoffe, Du dürftest Siegfried und Roy im Regenbogenland schon sehen. Grüsse Sie bitte von mir mit dem GRUSS der zaubernden Raubkatzen SARMOTI ",
            "memory_image":"/static/images/memory/magic.jpg"
        })
        self.memory_table.insert({
            "memory_title": "Bobby, der Hackenbeißer",
            "memory_date": "Unbekannt",
            "memory_text": "Im Jahr 2002 schlüpftest Du bei einem Züchter aus dem Ei. Den Grund Deiner Handaufzucht kennen wir nicht Auch wer Dein erstes Herrchen war, ist uns unbekannt.Man erzählte uns, dass dieser verstorben sei. Ursprünglich wollte die Witwe Dich weiterhin als Solovogel halten, doch Deiner Art entsprechend, sich nur einem Menschen anzuschließen, hast Du Dich verhalten und wurdest schließlich in eine Zoohandlung abgegeben. Ausländische Mittbürger verliebten sich in Dich. Kein Wunder. Denn alle Weißbauchpapageien sind ihrem Wesen nach kleine Clowns. Was sie nicht wußten, sind Eure angeborenen Charakterzüge. Schnell hattest Du den Namen „ Bobby, der Hackenbeißer“ weg. Bei unserer ersten Begegnung am 13.01.2019 machtest Du Dich riesig groß und meintest: „Na bin ich nicht ein toller Kerl für Deine Zaza (Gabor). Du attackiertest alles, was Dir zu nahe kam. Wer den Finger rein steckte, musste die SOS Notfallbox parat stehen haben. Zaza hatte bei Dir nicht viel zu sagen,  doch ein Paar wurdet ihr nie. Sie war einfach zu jung. Eine Vergesellschaftung im großen Vogelzimmer mit dem Rest der Geierbande scheiterte, was aber bei der Gattung der Weißbäuche fast schon ein ungeschriebenes Gesetz ist. Es blieb Dir Zaza und der  Sicht und Rufkontakt als Gesellschaft. Ich versprach Dir einen Platz auf Lebenszeit, dafür zeigtest Du mir Deine Zuneigung , suchtest öfters den Kontakt zu mir, aber vertrauen tat ich Dir nie. Gestern warst Du noch fit, verhieltst Dich wie immer. Aber heute am 15.02.2021 hingst Du kraftlos am Gitter, ließt Dich von mir weg pflücken, machtest bereitwillig noch den Schnabel für die ersten Hilfe Maßnahmen auf, doch den Kampf verloren wir nur wenige Stunden später. Flieg Bobby flieg oder besser Lauf in Deinem Watschelgang über die Brücke des Lichtes ins schöne Regenbogenland. Nimm unsere Grüße dorthin mit und lerne die Freunde von uns kennen, die Du hier nicht erleben konntest…. Und vielleicht, ja vielleicht wartet dort Dein erstes Herrchen auf Dich! Love Bobby!",
            "memory_image": "/static/images/memory/bobby.jpg"
        })
        self.memory_table.insert({
            "memory_title":"Luna, der Notruf",
            "memory_date": "Unbekannt",
            "memory_text":"Kleine Luna, wir kannten uns nicht, doch ich hatte Dich SCHON nach ein paar wenigen Minuten in mein Herz geschlossen.... Das Schicksal entschied, dass Du nun doch schon gehen musstest und wir Dir nicht helfen konnten / durften. In Gedanken gehörst Du genauso zu unseren Lieblingen.... Deine Geschichte erinnert mich an meine geliebte Tigern Magic.... So wie Dir, durfte ich ihr damals auch nicht mehr helfen. Du läufst gerade über die Brücke, über die wir alle irgendwann gehen und wenn es bei mir mal soweit ist, dann darf ich Dir in die Augen sehen. Bis dahin wirst Du mit meiner  Luna dort oben auf unsere Freunde aufpassen und nimmst unseren Grüße an alle mit.... SARMOTI (08.03.2021) (zum Hintergrund: Mit 4 Jahren musste Luna zum Wesenstest. Herrchen war übrfordert und total nervös und somit war es Luna auch. Die Ämter machten in dieser situation Druck und somit ging man den letzten Weg, ohne Luna mit einem zweiten Test eine Chance zu geben. Dieser hätte ihr zugestanden und eine andere Prüferin war auch schon gefunden. Wenn Ämter Druck mit falschen Informationen machen, sind die Tierhalter überfordert und wissen nicht ob sie wirklich richtig handeln.... Ein guter Rat, nehmt Euch Zeit für so eine Entscheidung nicht nur über ein Wochenende..... kommt Zeit kommt Rat..... kommen neue Erkenntnisse....kann Hilfe kommen.....)",
            "memory_image": "/static/images/memory/luna.jpg"
        })
        self.memory_table.insert({
            "memory_title":"Bordercollie Luna",
            "memory_date": "06.06.2009 bis 20.10.2020 (11 Jahre)",
            "memory_text": " Am 06.09. 2009 erblicktest du das Licht der Welt. Du wurdest von Carmen adoptiert und erlerntes alles, was ein Showhund können muss. Deine Spezialität war das Laufen auf zwei Beinen inkl. im Hübsch sitzen und danach wieder laufen.  Und das mehrfach in der Wiederholung. Deine Hundefamilie war nicht immer nett zu dir. Deine  Menschen gaben dich am 19.07.2015  zu mir und du durftest weiter deine Kunst zeigen. Du kuscheltest mit Rio dem Glücksschweinchen. Du sagtest den Ziegen, wann sie ihren Trick machen dürfen und wann nicht... Du nahmst das Baby Bandit vor 4 Jahren in deine Ausbildung und zeigtest ihm, wie man ein toller Showhund wird. Die Seebären waren dir unheimlich, aber dafür hast Du in jeder Show auf alle Papageien aufgepasst. Heute am 20.10.2020 bist du nach kurzer schwerer Krankheit von uns gegangen. Unser Ärzteteam konnte Dir nicht mehr helfen. Wir hätten gerne noch ein paar Jahre miteinander gehabt. Du, liebe Luna, bist jetzt da, wo bereits Zeus, Hera, Ares, Chronus und Magic sind... im Herzen bleibst Du bei mir und somit  immer unvergessen. LOVE LUNA LOVE ",
            "memory_image":"/static/images/memory/luna-collie.jpg"
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