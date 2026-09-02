from .database import SessionLocal
from .models import Question, Answer


questions = [
    {
        "question": "Koji je glavni grad Hrvatske?",
        "answers": [
            {"answer": "Zagreb", "is_correct": True},
            {"answer": "Split", "is_correct": False},
            {"answer": "Rijeka", "is_correct": False},
            {"answer": "Osijek", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najduža hrvatska rijeka?",
        "answers": [
            {"answer": "Sava", "is_correct": True},
            {"answer": "Dunav", "is_correct": False},
            {"answer": "Drava", "is_correct": False},
            {"answer": "Kupa", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najviši vrh u Hrvatskoj?",
        "answers": [
            {"answer": "Dinara", "is_correct": True},
            {"answer": "Biokovo", "is_correct": False},
            {"answer": "Velebit", "is_correct": False},
            {"answer": "Risnjak", "is_correct": False},
        ],
    },
    {
        "question": "Koje more graniči s Hrvatskom na zapadu?",
        "answers": [
            {"answer": "Jadransko more", "is_correct": True},
            {"answer": "Sredozemno more", "is_correct": False},
            {"answer": "Crno more", "is_correct": False},
            {"answer": "Baltičko more", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najveći hrvatski otok po površini?",
        "answers": [
            {"answer": "Cres", "is_correct": True},
            {"answer": "Krk", "is_correct": False},
            {"answer": "Brač", "is_correct": False},
            {"answer": "Hvar", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najveća hrvatska županija po površini?",
        "answers": [
            {"answer": "Ličko-senjska", "is_correct": True},
            {"answer": "Splitsko-dalmatinska", "is_correct": False},
            {"answer": "Istarska", "is_correct": False},
            {"answer": "Zagrebačka", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Slovenije?",
        "answers": [
            {"answer": "Ljubljana", "is_correct": True},
            {"answer": "Maribor", "is_correct": False},
            {"answer": "Celje", "is_correct": False},
            {"answer": "Kranj", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Italije?",
        "answers": [
            {"answer": "Rim", "is_correct": True},
            {"answer": "Milano", "is_correct": False},
            {"answer": "Napulj", "is_correct": False},
            {"answer": "Torino", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Španjolske?",
        "answers": [
            {"answer": "Madrid", "is_correct": True},
            {"answer": "Barcelona", "is_correct": False},
            {"answer": "Valencia", "is_correct": False},
            {"answer": "Sevilla", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Portugala?",
        "answers": [
            {"answer": "Lisabon", "is_correct": True},
            {"answer": "Porto", "is_correct": False},
            {"answer": "Coimbra", "is_correct": False},
            {"answer": "Faro", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Njemačke?",
        "answers": [
            {"answer": "Berlin", "is_correct": True},
            {"answer": "München", "is_correct": False},
            {"answer": "Hamburg", "is_correct": False},
            {"answer": "Köln", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Poljske?",
        "answers": [
            {"answer": "Varšava", "is_correct": True},
            {"answer": "Krakov", "is_correct": False},
            {"answer": "Gdanjsk", "is_correct": False},
            {"answer": "Wrocław", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Mađarske?",
        "answers": [
            {"answer": "Budimpešta", "is_correct": True},
            {"answer": "Debrecen", "is_correct": False},
            {"answer": "Szeged", "is_correct": False},
            {"answer": "Pécs", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Austrije?",
        "answers": [
            {"answer": "Beč", "is_correct": True},
            {"answer": "Graz", "is_correct": False},
            {"answer": "Salzburg", "is_correct": False},
            {"answer": "Innsbruck", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Švicarske?",
        "answers": [
            {"answer": "Bern", "is_correct": True},
            {"answer": "Zürich", "is_correct": False},
            {"answer": "Ženeva", "is_correct": False},
            {"answer": "Basel", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Belgije?",
        "answers": [
            {"answer": "Bruxelles", "is_correct": True},
            {"answer": "Antwerpen", "is_correct": False},
            {"answer": "Brugge", "is_correct": False},
            {"answer": "Liège", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Nizozemske?",
        "answers": [
            {"answer": "Amsterdam", "is_correct": True},
            {"answer": "Rotterdam", "is_correct": False},
            {"answer": "Haag", "is_correct": False},
            {"answer": "Utrecht", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Danske?",
        "answers": [
            {"answer": "Kopenhagen", "is_correct": True},
            {"answer": "Aarhus", "is_correct": False},
            {"answer": "Odense", "is_correct": False},
            {"answer": "Aalborg", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Norveške?",
        "answers": [
            {"answer": "Oslo", "is_correct": True},
            {"answer": "Bergen", "is_correct": False},
            {"answer": "Trondheim", "is_correct": False},
            {"answer": "Stavanger", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Švedske?",
        "answers": [
            {"answer": "Stockholm", "is_correct": True},
            {"answer": "Göteborg", "is_correct": False},
            {"answer": "Malmö", "is_correct": False},
            {"answer": "Uppsala", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Finske?",
        "answers": [
            {"answer": "Helsinki", "is_correct": True},
            {"answer": "Tampere", "is_correct": False},
            {"answer": "Turku", "is_correct": False},
            {"answer": "Oulu", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Islanda?",
        "answers": [
            {"answer": "Reykjavik", "is_correct": True},
            {"answer": "Akureyri", "is_correct": False},
            {"answer": "Keflavik", "is_correct": False},
            {"answer": "Hafnarfjörður", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Irske?",
        "answers": [
            {"answer": "Dublin", "is_correct": True},
            {"answer": "Cork", "is_correct": False},
            {"answer": "Limerick", "is_correct": False},
            {"answer": "Galway", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Ujedinjenog Kraljevstva?",
        "answers": [
            {"answer": "London", "is_correct": True},
            {"answer": "Birmingham", "is_correct": False},
            {"answer": "Manchester", "is_correct": False},
            {"answer": "Glasgow", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Francuske?",
        "answers": [
            {"answer": "Pariz", "is_correct": True},
            {"answer": "Lyon", "is_correct": False},
            {"answer": "Marseille", "is_correct": False},
            {"answer": "Toulouse", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Rusije?",
        "answers": [
            {"answer": "Moskva", "is_correct": True},
            {"answer": "Sankt Peterburg", "is_correct": False},
            {"answer": "Novosibirsk", "is_correct": False},
            {"answer": "Jekaterinburg", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Kine?",
        "answers": [
            {"answer": "Peking", "is_correct": True},
            {"answer": "Šangaj", "is_correct": False},
            {"answer": "Hong Kong", "is_correct": False},
            {"answer": "Guangzhou", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Japana?",
        "answers": [
            {"answer": "Tokio", "is_correct": True},
            {"answer": "Osaka", "is_correct": False},
            {"answer": "Yokohama", "is_correct": False},
            {"answer": "Nagoya", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Indije?",
        "answers": [
            {"answer": "New Delhi", "is_correct": True},
            {"answer": "Mumbai", "is_correct": False},
            {"answer": "Kolkata", "is_correct": False},
            {"answer": "Bengaluru", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad SAD-a?",
        "answers": [
            {"answer": "Washington D.C.", "is_correct": True},
            {"answer": "New York", "is_correct": False},
            {"answer": "Los Angeles", "is_correct": False},
            {"answer": "Chicago", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Kanade?",
        "answers": [
            {"answer": "Ottawa", "is_correct": True},
            {"answer": "Toronto", "is_correct": False},
            {"answer": "Vancouver", "is_correct": False},
            {"answer": "Montreal", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Meksika?",
        "answers": [
            {"answer": "Mexico City", "is_correct": True},
            {"answer": "Guadalajara", "is_correct": False},
            {"answer": "Monterrey", "is_correct": False},
            {"answer": "Puebla", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Brazila?",
        "answers": [
            {"answer": "Brasilia", "is_correct": True},
            {"answer": "Rio de Janeiro", "is_correct": False},
            {"answer": "São Paulo", "is_correct": False},
            {"answer": "Salvador", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Argentine?",
        "answers": [
            {"answer": "Buenos Aires", "is_correct": True},
            {"answer": "Córdoba", "is_correct": False},
            {"answer": "Rosario", "is_correct": False},
            {"answer": "Mendoza", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Čilea?",
        "answers": [
            {"answer": "Santiago", "is_correct": True},
            {"answer": "Valparaíso", "is_correct": False},
            {"answer": "Concepción", "is_correct": False},
            {"answer": "Viña del Mar", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Perua?",
        "answers": [
            {"answer": "Lima", "is_correct": True},
            {"answer": "Arequipa", "is_correct": False},
            {"answer": "Cusco", "is_correct": False},
            {"answer": "Trujillo", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Kolumbije?",
        "answers": [
            {"answer": "Bogotá", "is_correct": True},
            {"answer": "Medellín", "is_correct": False},
            {"answer": "Cali", "is_correct": False},
            {"answer": "Barranquilla", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Venecuele?",
        "answers": [
            {"answer": "Caracas", "is_correct": True},
            {"answer": "Maracaibo", "is_correct": False},
            {"answer": "Valencia", "is_correct": False},
            {"answer": "Barquisimeto", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Australije?",
        "answers": [
            {"answer": "Canberra", "is_correct": True},
            {"answer": "Sydney", "is_correct": False},
            {"answer": "Melbourne", "is_correct": False},
            {"answer": "Brisbane", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Novog Zelanda?",
        "answers": [
            {"answer": "Wellington", "is_correct": True},
            {"answer": "Auckland", "is_correct": False},
            {"answer": "Christchurch", "is_correct": False},
            {"answer": "Hamilton", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Južnoafričke Republike?",
        "answers": [
            {"answer": "Pretoria", "is_correct": True},
            {"answer": "Cape Town", "is_correct": False},
            {"answer": "Johannesburg", "is_correct": False},
            {"answer": "Durban", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Egipta?",
        "answers": [
            {"answer": "Kairo", "is_correct": True},
            {"answer": "Aleksandrija", "is_correct": False},
            {"answer": "Giza", "is_correct": False},
            {"answer": "Luxor", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Nigerije?",
        "answers": [
            {"answer": "Abuja", "is_correct": True},
            {"answer": "Lagos", "is_correct": False},
            {"answer": "Kano", "is_correct": False},
            {"answer": "Ibadan", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Kenije?",
        "answers": [
            {"answer": "Nairobi", "is_correct": True},
            {"answer": "Mombasa", "is_correct": False},
            {"answer": "Kisumu", "is_correct": False},
            {"answer": "Nakuru", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Maroka?",
        "answers": [
            {"answer": "Rabat", "is_correct": True},
            {"answer": "Casablanca", "is_correct": False},
            {"answer": "Fes", "is_correct": False},
            {"answer": "Marrakech", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Turske?",
        "answers": [
            {"answer": "Ankara", "is_correct": True},
            {"answer": "Istanbul", "is_correct": False},
            {"answer": "Izmir", "is_correct": False},
            {"answer": "Bursa", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Irana?",
        "answers": [
            {"answer": "Teheran", "is_correct": True},
            {"answer": "Isfahan", "is_correct": False},
            {"answer": "Shiraz", "is_correct": False},
            {"answer": "Tabriz", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Iraka?",
        "answers": [
            {"answer": "Bagdad", "is_correct": True},
            {"answer": "Basra", "is_correct": False},
            {"answer": "Mosul", "is_correct": False},
            {"answer": "Erbil", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Saudijske Arabije?",
        "answers": [
            {"answer": "Rijad", "is_correct": True},
            {"answer": "Džeda", "is_correct": False},
            {"answer": "Meka", "is_correct": False},
            {"answer": "Medina", "is_correct": False},
        ],
    },
    {
        "question": "Koji je glavni grad Izraela?",
        "answers": [
            {"answer": "Jeruzalem", "is_correct": True},
            {"answer": "Tel Aviv", "is_correct": False},
            {"answer": "Haifa", "is_correct": False},
            {"answer": "Beer Ševa", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najduža rijeka u Europi?",
        "answers": [
            {"answer": "Volga", "is_correct": True},
            {"answer": "Dunav", "is_correct": False},
            {"answer": "Dnjepar", "is_correct": False},
            {"answer": "Don", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najduža rijeka u Africi?",
        "answers": [
            {"answer": "Nil", "is_correct": True},
            {"answer": "Kongo", "is_correct": False},
            {"answer": "Niger", "is_correct": False},
            {"answer": "Zambezi", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najduža rijeka u Aziji?",
        "answers": [
            {"answer": "Yangtze (Chang Jiang)", "is_correct": True},
            {"answer": "Huang He", "is_correct": False},
            {"answer": "Mekong", "is_correct": False},
            {"answer": "Indus", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najduža rijeka u Južnoj Americi?",
        "answers": [
            {"answer": "Amazon", "is_correct": True},
            {"answer": "Paraná", "is_correct": False},
            {"answer": "Orinoco", "is_correct": False},
            {"answer": "São Francisco", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najduža rijeka u Sjevernoj Americi?",
        "answers": [
            {"answer": "Mississippi-Missouri", "is_correct": True},
            {"answer": "Rio Grande", "is_correct": False},
            {"answer": "Yukon", "is_correct": False},
            {"answer": "Mackenzie", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najviši vrh u Europi?",
        "answers": [
            {"answer": "Elbrus", "is_correct": True},
            {"answer": "Mont Blanc", "is_correct": False},
            {"answer": "Matterhorn", "is_correct": False},
            {"answer": "Zugspitze", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najviši vrh u Africi?",
        "answers": [
            {"answer": "Kilimanjaro", "is_correct": True},
            {"answer": "Mount Kenya", "is_correct": False},
            {"answer": "Mount Cameroon", "is_correct": False},
            {"answer": "Ras Dashen", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najviši vrh u Aziji?",
        "answers": [
            {"answer": "Mount Everest", "is_correct": True},
            {"answer": "K2", "is_correct": False},
            {"answer": "Kangchenjunga", "is_correct": False},
            {"answer": "Lhotse", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najviši vrh u Sjevernoj Americi?",
        "answers": [
            {"answer": "Denali (McKinley)", "is_correct": True},
            {"answer": "Mount Logan", "is_correct": False},
            {"answer": "Mount Whitney", "is_correct": False},
            {"answer": "Mount Elbert", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najviši vrh u Južnoj Americi?",
        "answers": [
            {"answer": "Aconcagua", "is_correct": True},
            {"answer": "Ojos del Salado", "is_correct": False},
            {"answer": "Huascarán", "is_correct": False},
            {"answer": "Monte Pissis", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najviši vrh u Australiji (kontinent)?",
        "answers": [
            {"answer": "Mount Kosciuszko", "is_correct": True},
            {"answer": "Mount Cook", "is_correct": False},
            {"answer": "Mount Wilhelm", "is_correct": False},
            {"answer": "Puncak Jaya", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najveća pustinja u Africi?",
        "answers": [
            {"answer": "Sahara", "is_correct": True},
            {"answer": "Kalahari", "is_correct": False},
            {"answer": "Namib", "is_correct": False},
            {"answer": "Danakil", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najveća pustinja u Aziji?",
        "answers": [
            {"answer": "Arapska pustinja", "is_correct": True},
            {"answer": "Gobi", "is_correct": False},
            {"answer": "Takla Makan", "is_correct": False},
            {"answer": "Karakum", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najveća pustinja u Australiji?",
        "answers": [
            {"answer": "Great Victoria", "is_correct": True},
            {"answer": "Simpson", "is_correct": False},
            {"answer": "Gibson", "is_correct": False},
            {"answer": "Tanami", "is_correct": False},
        ],
    },
    {
        "question": "Koje je najveće slatkovodno jezero po površini?",
        "answers": [
            {"answer": "Superior", "is_correct": True},
            {"answer": "Bajkal", "is_correct": False},
            {"answer": "Viktorijino jezero", "is_correct": False},
            {"answer": "Huron", "is_correct": False},
        ],
    },
    {
        "question": "Koje je najdublje jezero na svijetu?",
        "answers": [
            {"answer": "Bajkal", "is_correct": True},
            {"answer": "Tanganjika", "is_correct": False},
            {"answer": "Kaspijsko", "is_correct": False},
            {"answer": "Superior", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najveći zaljev na svijetu?",
        "answers": [
            {"answer": "Bengalski zaljev", "is_correct": True},
            {"answer": "Meksički zaljev", "is_correct": False},
            {"answer": "Hudsonov zaljev", "is_correct": False},
            {"answer": "Perzijski zaljev", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najveći poluotok na svijetu?",
        "answers": [
            {"answer": "Arapski poluotok", "is_correct": True},
            {"answer": "Indijski poluotok", "is_correct": False},
            {"answer": "Skandinavski poluotok", "is_correct": False},
            {"answer": "Iberijski poluotok", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najveća država u Južnoj Americi po površini?",
        "answers": [
            {"answer": "Brazil", "is_correct": True},
            {"answer": "Argentina", "is_correct": False},
            {"answer": "Peru", "is_correct": False},
            {"answer": "Kolumbija", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najveća država u Africi?",
        "answers": [
            {"answer": "Alžir", "is_correct": True},
            {"answer": "DR Kongo", "is_correct": False},
            {"answer": "Sudan", "is_correct": False},
            {"answer": "Libija", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najmanja država u Europi?",
        "answers": [
            {"answer": "Vatikan", "is_correct": True},
            {"answer": "Monako", "is_correct": False},
            {"answer": "San Marino", "is_correct": False},
            {"answer": "Lihtenštajn", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najmanja država u Aziji?",
        "answers": [
            {"answer": "Maldivi", "is_correct": True},
            {"answer": "Singapur", "is_correct": False},
            {"answer": "Bahrein", "is_correct": False},
            {"answer": "Brunej", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najnaseljeniji grad na svijetu (metropolitansko područje)?",
        "answers": [
            {"answer": "Tokio", "is_correct": True},
            {"answer": "Šangaj", "is_correct": False},
            {"answer": "Delhi", "is_correct": False},
            {"answer": "Mexico City", "is_correct": False},
        ],
    },
    {
        "question": "Koja država ima najveću gustoću naseljenosti?",
        "answers": [
            {"answer": "Monako", "is_correct": True},
            {"answer": "Singapur", "is_correct": False},
            {"answer": "Bahrein", "is_correct": False},
            {"answer": "Maldivi", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najveći arhipelag na svijetu?",
        "answers": [
            {"answer": "Indonezija", "is_correct": True},
            {"answer": "Filipini", "is_correct": False},
            {"answer": "Japan", "is_correct": False},
            {"answer": "Maldivi", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najduži planinski lanac na svijetu?",
        "answers": [
            {"answer": "Ande", "is_correct": True},
            {"answer": "Himalaja", "is_correct": False},
            {"answer": "Kordiljeri", "is_correct": False},
            {"answer": "Alpe", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najduži planinski lanac u Europi?",
        "answers": [
            {"answer": "Skandinavske planine", "is_correct": True},
            {"answer": "Alpe", "is_correct": False},
            {"answer": "Karpate", "is_correct": False},
            {"answer": "Dinaridi", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najveća država u Oceaniji?",
        "answers": [
            {"answer": "Australija", "is_correct": True},
            {"answer": "Novi Zeland", "is_correct": False},
            {"answer": "Papua Nova Gvineja", "is_correct": False},
            {"answer": "Fidži", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najveća država u Sjevernoj Americi?",
        "answers": [
            {"answer": "Kanada", "is_correct": True},
            {"answer": "SAD", "is_correct": False},
            {"answer": "Meksiko", "is_correct": False},
            {"answer": "Grenland", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najveća država u Europi (uključujući azijski dio)?",
        "answers": [
            {"answer": "Rusija", "is_correct": True},
            {"answer": "Ukrajina", "is_correct": False},
            {"answer": "Francuska", "is_correct": False},
            {"answer": "Španjolska", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najveći otok u Mediteranu?",
        "answers": [
            {"answer": "Sicilija", "is_correct": True},
            {"answer": "Sardinija", "is_correct": False},
            {"answer": "Cipar", "is_correct": False},
            {"answer": "Kreta", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najveći otok u Jadranu?",
        "answers": [
            {"answer": "Cres", "is_correct": True},
            {"answer": "Krk", "is_correct": False},
            {"answer": "Brač", "is_correct": False},
            {"answer": "Hvar", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najveći grad u Hrvatskoj?",
        "answers": [
            {"answer": "Zagreb", "is_correct": True},
            {"answer": "Split", "is_correct": False},
            {"answer": "Rijeka", "is_correct": False},
            {"answer": "Osijek", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najveća luka u Hrvatskoj?",
        "answers": [
            {"answer": "Rijeka", "is_correct": True},
            {"answer": "Split", "is_correct": False},
            {"answer": "Ploče", "is_correct": False},
            {"answer": "Šibenik", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najveći nacionalni park u Hrvatskoj?",
        "answers": [
            {"answer": "Plitvička jezera", "is_correct": True},
            {"answer": "Kornati", "is_correct": False},
            {"answer": "Krka", "is_correct": False},
            {"answer": "Paklenica", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najduža rijeka u Hrvatskoj koja se ulijeva u Jadransko more?",
        "answers": [
            {"answer": "Neretva", "is_correct": True},
            {"answer": "Zrmanja", "is_correct": False},
            {"answer": "Krka", "is_correct": False},
            {"answer": "Cetina", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najveći grad na Jadranskom moru?",
        "answers": [
            {"answer": "Bari", "is_correct": True},
            {"answer": "Split", "is_correct": False},
            {"answer": "Trst", "is_correct": False},
            {"answer": "Ancona", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najveći otok u Atlantskom oceanu?",
        "answers": [
            {"answer": "Grenland", "is_correct": True},
            {"answer": "Island", "is_correct": False},
            {"answer": "Velika Britanija", "is_correct": False},
            {"answer": "Nova Fundlandija", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najveća delta u Europi?",
        "answers": [
            {"answer": "delta Dunava", "is_correct": True},
            {"answer": "delta Rone", "is_correct": False},
            {"answer": "delta Poa", "is_correct": False},
            {"answer": "delta Ebra", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najveća rijeka u svijetu po protoku?",
        "answers": [
            {"answer": "Amazon", "is_correct": True},
            {"answer": "Kongo", "is_correct": False},
            {"answer": "Yangtze", "is_correct": False},
            {"answer": "Mississippi", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najveća visoravan na svijetu?",
        "answers": [
            {"answer": "Tibet", "is_correct": True},
            {"answer": "Iranska visoravan", "is_correct": False},
            {"answer": "Anadolska visoravan", "is_correct": False},
            {"answer": "Dekanska visoravan", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najveći kanjon na svijetu?",
        "answers": [
            {"answer": "Grand Canyon", "is_correct": True},
            {"answer": "Fish River Canyon", "is_correct": False},
            {"answer": "Kali Gandaki", "is_correct": False},
            {"answer": "Colca", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najveći slap na svijetu?",
        "answers": [
            {"answer": "Angelov slap", "is_correct": True},
            {"answer": "Victoria", "is_correct": False},
            {"answer": "Niagara", "is_correct": False},
            {"answer": "Iguazu", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najveća država u Srednjoj Americi?",
        "answers": [
            {"answer": "Nikaragva", "is_correct": True},
            {"answer": "Honduras", "is_correct": False},
            {"answer": "Gvatemala", "is_correct": False},
            {"answer": "Panama", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najveći grad u Africi?",
        "answers": [
            {"answer": "Kairo", "is_correct": True},
            {"answer": "Lagos", "is_correct": False},
            {"answer": "Kinshasa", "is_correct": False},
            {"answer": "Johannesburg", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najveći poluotok u Europi?",
        "answers": [
            {"answer": "Skandinavski", "is_correct": True},
            {"answer": "Iberijski", "is_correct": False},
            {"answer": "Apeninski", "is_correct": False},
            {"answer": "Balkanski", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najveća otočna država na svijetu?",
        "answers": [
            {"answer": "Indonezija", "is_correct": True},
            {"answer": "Filipini", "is_correct": False},
            {"answer": "Japan", "is_correct": False},
            {"answer": "Madagaskar", "is_correct": False},
        ],
    },
    {
        "question": "Koja je najveća država u Europi bez izlaza na more?",
        "answers": [
            {"answer": "Bjelorusija", "is_correct": True},
            {"answer": "Kazahstan", "is_correct": False},
            {"answer": "Mađarska", "is_correct": False},
            {"answer": "Švicarska", "is_correct": False},
        ],
    },
    {
        "question": "Koji je najveći grad u Europi?",
        "answers": [
            {"answer": "Moskva", "is_correct": True},
            {"answer": "London", "is_correct": False},
            {"answer": "Pariz", "is_correct": False},
            {"answer": "Istanbul", "is_correct": False},
        ],
    }
]


def seed_database():
    db = SessionLocal()

    try:
        existing_questions = db.query(Question).count()

        if existing_questions > 60:
            print(
                f"Baza već sadrži {existing_questions} pitanja."
            )
            return

        for question_data in questions:
            question = Question(
                question=question_data["question"]
            )

            for answer_data in question_data["answers"]:
                answer = Answer(
                    answer=answer_data["answer"],
                    is_correct=answer_data["is_correct"]
                )

                question.answers.append(answer)

            db.add(question)

        db.commit()

        print(
            f"Ubačeno {len(questions)} pitanja."
        )

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()