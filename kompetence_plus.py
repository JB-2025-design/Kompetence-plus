# kompetence_plus.py

import streamlit as st

# -----------------------
# KONFIGURACE APLIKACE
# -----------------------

st.set_page_config(
    page_title="kompetence+",
    page_icon="📊",
    layout="wide",
)


# -----------------------
# DATA – číselníky
# -----------------------



# Pořadí témat – první je „Změna paradigmatu“
TOPICS = {
    "Změna paradigmatu": "Změna paradigmatu",
    "Systémová chyba": "Systémová chyba",
    "Kompetenčně-znalostní model": "Kompetenčně-znalostní model",
    "Funkční gramotnost": "Funkční gramotnost",
    "Kompetence plus": "Kompetence plus",
    "Rodiče": "Rodiče",    
    "Učitelé": "Učitelé",
    "Žáci a studenti": "Žáci a studenti",     
    "Škola a zřizovatel": "Škola a zřizovatel",
    "Systém (MŠMT, NPI)": "Systém (MŠMT, NPI)",
    
}

# -----------------------
# CONTENT – texty podle TÉMATU (nezávislé na cílové skupině)
# -----------------------

CONTENT = {
        "Změna paradigmatu": """
### Změna paradigmatu: proč školství potřebuje nový rámec pro 21. století

České vzdělávání stojí na historické křižovatce. Společnost se mění rychleji, než škola stíhá reagovat, technologie zasahují do každé oblasti života a dříve samozřejmé jistoty se rozplývají. Naše školství však stále stojí jednou nohou v minulém století — v době, kdy znalosti byly vzácné, učebnice byla hlavním zdrojem informací a škola byla jediným místem, kde se děti učily orientovat ve světě.

Dnes už tomu tak není. Informací je přebytek, technologie jsou všudypřítomné a umělá inteligence dokáže během sekund produkovat texty, výpočty i analýzy, které by ještě nedávno byly doménou univerzit. Tato změna není kosmetická — je to tektonický posun, který mění způsob, jakým lidé pracují, přemýšlejí i komunikují. A zároveň mění to nejdůležitější: co má škola učit a jak má učit.

Je proto nutné udělat krok, kterému se většina vzdělávacích systémů dlouho vyhýbala: přiznat, že původní model založený buď na znalostech, nebo na kompetencích, je překonaný. Ani jeden z nich nestačí, pokud stojí osamoceně. Nestačí učit encyklopedické vědomosti bez pochopení. Nestačí učit kompetence bez pevného obsahového rámce. Nestačí spoléhat na intuici učitelů bez jasných standardů. A už vůbec nestačí předpokládat, že děti si „všechno vygooglují“ nebo že jim umělá inteligence nahradí práci, kterou potřebují udělat samy.

Změna paradigmatu znamená nové vyvážení: **znalosti → gramotnosti → kompetence → komplexita**.  
Tato posloupnost je základní podmínkou vzdělávání v 21. století:

- Znalosti poskytují orientační bod.  
- Gramotnosti umožňují vědomosti použít v praxi.  
- Kompetence dávají rámec tomu, jak s nimi pracujeme.  
- Komplexní myšlení staví na všem předchozím a umožňuje žákovi jednat v situacích, kde neexistuje jediná správná odpověď.

Problém současného českého modelu je dvojí:
- učíme kompetence, ale hodnotíme znalosti,
- a zároveň očekávané výsledky (RVP) jsou příliš vágní, než aby poskytly stabilní základ pro učení, hodnocení i rovnost příležitostí.

Výsledkem je nespokojenost všech: učitelů, rodičů i žáků. A také systémová nerovnost, která nutí rodiče platit přípravy na přijímačky, protože právě ty jako jediné poskytují jasná očekávání. Školství, které má být veřejnou službou, se fragmentuje na paralelní placený sektor mimo školu, což podrývá důvěru v základní školy i ve spravedlnost systému.

Změna paradigmatu však není o kosmetickém upravení RVP. Je to zásadní rekonstrukce myšlení o škole, která musí vycházet z těchto principů:

- Bez znalostí nevznikne porozumění.  
- Bez gramotností nelze poznání použít.  
- Bez kompetencí nelze řešit složité situace.  
- Bez učitele nelze postavit ani jeden z těchto pilířů.

Učitelé jsou architekti této změny – nikoli její vykonavatelé. Jsou to oni, kdo budují pracovní návyky, čtenářské a matematické minimum, schopnost kritického úsudku, odolnost, soustředění i přesnost. Bez těchto dovedností se nelze pohybovat v digitálním světě, kde jsou informace rychlé, ale často nepřesné. Umělá inteligence může ulehčit práci, ale nenaučí děti myslet. To dokáže jen učitel, který dítě provází a ukazuje mu, jak strukturovat myšlenky, ověřovat informace, rozumět chybám a růst.

Změna paradigmatu je tedy mnohem více než reforma kurikula. Je to přesun od školy, která pouze přenáší obsah, ke škole, která navíc formuje a vede k porozumění. Od školy, která nejen trénuje paměť, ke škole, která navíc buduje myšlení. Od školy, kde se děti učí náhodně a nerovnoměrně, ke škole, kde mají pevný základ a jasnou trajektorii růstu.

Pokud chceme, aby české školství uspělo v éře digitální komplexity, musíme začít právě zde: v pochopení, že vzdělávání není spor mezi znalostmi a kompetencemi, ale jejich propojením do jednoho celku. A že tato změna není hrozbou, ale největší příležitostí za posledních třicet let.

**To je podstata změny paradigmatu.**
""",
    "Systémová chyba":
    """
### Systémová chyba českého školství: proč si veřejně financované vzdělávání rodiče musí znovu „kupovat“

České školství stojí před paradoxem, který má hluboké systémové kořeny: rodiče financují základní vzdělávání prostřednictvím daní, ale přesto se masově uchylují k úniku na víceletá gymnázia a k placené přípravě na státní přijímací zkoušky. Tento „dvojí účet“ je symptomem širšího problému: ztráty důvěry v rovnoměrnou kvalitu základních škol a nejasného směru kurikulární politiky, která hlásá kompetence, ale hodnotí výhradně znalosti.

## 1. Důvěra rodičů slábne – a systém na to nereaguje

Rodiče neočekávají po základní škole přemíru abstraktních kompetencí.  
Očekávají pevné základy: čtení s porozuměním, jistotu v matematice, psaní, pracovní návyky a systematickou výuku.

Tam, kde to nevidí, hledají alternativu – nejčastěji gymnázia.

Víceletá gymnázia byla původně výjimečnou větví vzdělávací soustavy.  
Dnes se stala únikovým ventilem pro střední třídu. Tento tlak není projevem ambiciózních rodičů, ale nedůvěry v rovnoměrnou kvalitu základního vzdělávání, zejména na 2. stupni.

Stát tak vytváří situaci, ve které:

- z veřejných prostředků financuje povinnou školní docházku,
- ale rodiče reálně platí další „školné“ — přípravy, kurzy, doučování, testy nanečisto.

Jde o typickou systémovou chybu, nikoli o individuální selhání rodičů nebo škol.

## 2. Kompetence se učí, znalosti se testují: nevyřešený kurikulární konflikt

České školy mají podle RVP vyučovat kompetenčně: žák se má učit spolupracovat, řešit problémy, zkoumat, tvořit, přemýšlet v souvislostech.

Přijímací zkoušky CERMATu však fungují opačně:  
v časově omezeném režimu testují znalosti, přesnost a rychlost — nikoli kompetence.

Tato dualita působí škodlivě:

- školy učí něco jiného, než co se zkouší,
- rodiče vidí, že kompetence nepomohou u přijímaček,
- a logicky investují do znalostní přípravy, protože ta je faktorem úspěchu v systému.

Tím vzniká paralelní vzdělávací trh, který:

- vybírá peníze od rodičů,
- zvyšuje nerovnosti,
- posiluje přesvědčení, že veřejná škola nestačí.

## 3. Placené přípravy: symptomy, nikoli řešení

Placené přípravné kurzy, testy nanečisto, komerční učebnice a individuální doučování nejsou projevem „přehnaných ambicí rodičů“.  
Jsou projevem nedostatečné systémové podpory a chybějících standardů.

Rodič platí za to, co má být součástí systému:

- jasné očekávání, co má dítě umět,
- systematickou přípravu v rámci běžné výuky,
- jednotné standardy,
- rovné šance,
- spolehlivé hodnocení výsledků.

Dnešní realita je opačná:  
kompetenční kurikulum neobsahuje dostatečně přesné znalostní výstupy, školy mají příliš široký interpretační prostor, učitelé nemají jasné standardy a přijímačky jsou jediným „pevnějším bodem“.

Proto rodiče platí.  
Ne protože chtějí, ale protože musí, mají-li jejich děti uspět.

## 4. Proč je to systémová chyba, nikoli „přirozený vývoj“

Systémová chyba vzniká tam, kde:

- veřejná služba deklaruje jedno, ale v praxi vyžaduje druhé,
- rodiče musí platit dvakrát za totéž,
- nerovnosti nejsou důsledkem schopností, ale ekonomických možností,
- kurikulum není sladěno s hodnocením,
- absence znalostních standardů vede k chaosu.

České školství se ocitlo přesně v této situaci:  
výuka směřuje k abstraktním kompetencím, ale hodnotí se čistá znalost.

Rodiče platí za veřejnou školu z daní, ale aby jejich dítě uspělo, musí platit znovu.  
Tento nesoulad dlouhodobě narušuje důvěru v systém.

## 5. Co zřizovatelé a stát mohou udělat pro nápravu

Systémovou chybu lze odstranit pouze systémově. To znamená:

- zavést jasné **znalostní standardy** pro každý ročník (ne vágní popisy typu „orientuje se“),
- provázat kompetence s konkrétním učivem (**kompetenčně–znalostní model**),
- sjednotit výuku s tím, co se ověřuje,
- posílit **gramotnosti** jako druhou dimenzi kurikula,
- umožnit školám systematicky diagnostikovat stav dovedností,
- podpořit učitele v **elementární didaktice** (čtení, psaní, počítání),
- snížit tlak na rodiče vytvářením podpůrných mechanismů ve školách,
- zrevidovat roli **víceletých gymnázií**, aby nefungovala jako únikový ventil.

Změna není otázkou jednoho opatření, ale celkové změny paradigmatu.

## 6. Závěr: Děti nepotřebují další kurzy. Potřebují systém, který funguje.

Příprava na přijímací testy se stala **stínovým vzdělávacím sektorem**.  
Ne proto, že by rodiče odmítali veřejné školství, ale protože se v něm necítí jistě.

Placená příprava je signálem, že systém nenabízí to, co slibuje:  
rovné šance a kvalitní vzdělání pro všechny.

Kompetence jsou důležité.  
Znalosti jsou nezbytné.  
Ale české školství potřebuje jejich propojení, jasný rámec a stabilní standardy.

Teprve pak přestane být přijímací řízení bojem o přípravy a stane se tím, čím by být mělo:  
**spravedlivým ověřením toho, co se děti skutečně naučily ve škole, kterou platíme společně.**
""",
"Kompetenčně-znalostní model":
"""
### Od kompetencí ke kompetenčně-znalostnímu modelu: nutná změna paradigmatu v českém vzdělávání

Současná debata o podobě českého kurikula se již několik let opírá o kompetenční model vzdělávání, který se stal východiskem rámcových vzdělávacích programů i návrhů jejich revizí. Kompetence jsou zásadní pro přípravu žáků na proměnlivý svět: mají podporovat samostatné myšlení, řešení problémů, komunikaci, spolupráci, digitální gramotnost a schopnost učit se. Tyto požadavky odpovídají globálním trendům i potřebám společnosti založené na informacích.

Nicméně praxe ukazuje, že čistě kompetenční přístup není v českém systému dlouhodobě udržitelný, a to ze dvou hlavních důvodů:

1. kompetence nejsou měřitelné bez jasného obsahového ukotvení,  
2. žáci potřebují pevné znalostní základy, aby kompetence vůbec mohli uplatňovat.

Problém tedy není v samotných kompetencích, ale v jejich neúplnosti, pokud nejsou spojeny s přesně definovanými očekávanými znalostmi a gramotnostmi. Z dostupných analýz (ČŠI, OECD, NÚV/NPI, odborné studie) vyplývá, že přechod k **kompetenčně-znalostnímu modelu** je nezbytný. Tento model je zároveň kompatibilní s evropskými přístupy, zejména rakouským systémem iKM PLUS, německými Bildungsstandards a finským pojetím „knowledge-based competencies“.

## Kompetence bez měřitelné znalostní báze vedou k vágnosti výstupů

Kompetenční formulace v aktuálním RVP (např. „žák volí vhodné postupy“, „využívá poznatků“, „řeší situace“) neobsahují dostatečně přesné popisy toho, jaké konkrétní dovednosti a znalosti má žák prokázat. Formulace jsou deklarativní, nikoli operacionalizované; nelze z nich snadno odvodit hodnoticí kritéria.

To vede k několika zásadním problémům:

- rozdílným interpretacím mezi školami,  
- neschopnosti systematicky měřit pokrok žáků,  
- obtížím při tvorbě přijímacích a maturitních testů,  
- přetížení učitelů, kteří nemají jednotná kritéria,  
- nejednotnosti ve výstupech absolventů mezi školami.

Ve výsledku se český systém ocitá v paradoxu:  
**učíme kompetenčně, ale hodnotíme převážně znalostně**, protože pouze znalosti lze testovat spolehlivě.

Tento paradox není řešitelný bez doplnění druhé dimenze — **obsahové (znalostní) a gramotnostní**.

## Kompetence nejsou alternativou ke znalostem, ale vyšším patrem nad nimi

Aktuální výzkumy ukazují, že schopnosti vyššího řádu (kritické myšlení, práce s informacemi, kreativita) nevznikají izolovaně. Jsou výsledkem stabilního kognitivního základu — znalostí a mentálních schémat, která žák používá.

Bez znalostí není možné rozvíjet kompetence.

- Student nemůže porovnávat údaje, pokud nerozumí jednotkám.  
- Nemůže interpretovat graf, pokud nechápe vztahy mezi veličinami.  
- Nemůže argumentovat, pokud nezná pojmy, které argument vytvářejí.  
- A nemůže korigovat umělou inteligenci, pokud nemá vlastní referenční rámec.

To platí zvlášť v době, kdy AI generuje odpovědi přesvědčivým jazykem, ale s rizikem faktických chyb. **Znalostní minimum je nezbytným korektivem technologií.**

## Změna paradigmatu: od znalostí k komplexitě — ale s pevnou bází

České vzdělávání musí přijmout zásadní skutečnost: svět informací se změnil. Už není možné stavět vzdělání pouze na objemu vědomostí. To, co však potřebujeme, není „méně znalostí“, nýbrž **jiný typ znalostí** — znalosti, které umožňují chápat vztahy, struktury, postupy a logiku oborů.

**Komplexita nemůže vzniknout bez základů.  
Je výsledkem znalostí, nikoli jejich náhradou.**

Tento posun je třeba formalizovat do kurikula, a to právě modelem, který propojuje:

- kompetence (proces),  
- znalosti / gramotnosti (obsah),  
- komplexní úlohy (aplikace).

Tak vzniká trojrozměrný rámec, který odpovídá potřebám současné společnosti.

## Inspirace: rakouský model iKM PLUS a jeho relevance pro ČR

Rakousko úspěšně implementovalo systém, který:

- definuje jasné obsahové oblasti (čísla, algebra, geometrie, data),  
- rozlišuje čtyři procesní kompetence (modelování, počítání, interpretace, argumentace),  
- a testuje jejich propojení v konkrétních úlohách.

Výsledkem je **standardizovatelné, měřitelné, přehledné a spravedlivé hodnocení**.

Přenos tohoto principu do ČR je možný skrze využití existujících českých kategorií:

- **klíčové kompetence** jako procesní osa,  
- **gramotnosti** jako obsahová osa,  
- **očekávané výstupy RVP** jako konkrétní indikátory.

Tím lze dosáhnout kompatibility se stávající dokumentací a zároveň zvýšit kvalitu měřitelnosti.


## Role učitele jako garanta kvality a nositele změny

Učitel v tomto systému není pouhým facilitátorem učení. Je:

- garantem přesného výkladu pojmů,  
- odborníkem, který buduje znalostní minimum,  
- tvůrcem prostředí, kde vznikají pracovní návyky, trpělivost a pečlivost,  
- korektorem chyb generovaných AI,  
- klíčovým aktérem při přechodu od jednoduchého k komplexnímu myšlení.

Podceňování elementárních dovedností (čtení, psaní, počítání) vede k oslabení soustředění a pracovních návyků, což se později negativně projevuje ve všech oblastech vzdělávání.  
**Elementarista či elementaristka nevychovává „jen pro 1. stupeň“ — vytváří celou budoucí trajektorii žákova učení.**

## Doporučení pro systémové změny

Aby mohl kompetenčně-znalostní model fungovat, je potřeba jasně definovat:

1. měřitelné znalostní standardy pro jednotlivé ročníky,  
2. propojení kompetencí s obsahovými oblastmi (matice),  
3. model komplexních úloh, které propojují proces a obsah,  
4. odbornou podporu učitelům, kteří budou moci model aplikovat,  
5. digitální nástroje, které umožní cílené procvičování a diagnostiku.

Tyto kroky zajistí, že kompetence nebudou odděleným ideálem, ale praktickou, měřitelnou součástí vzdělávání.

## Závěr

České školství nestojí před otázkou **„kompetence nebo znalosti“**.  
Stojí před úkolem propojit obojí do uceleného a měřitelného rámce, který umožní rozvíjet hluboké porozumění, podpoří kvalitu výuky a umožní žákům obstát v prostředí digitální komplexity.

Klíčová není samotná změna kurikula, ale **změna paradigmatu**, v níž přecházíme:

- od objemu znalostí k jejich strukturálnímu využití,  
- od kompetencí bez obsahu ke kompetenčně-znalostnímu modelu,  
- od jednostranného hodnocení ke komplexnímu ověřování,  
- od izolované výuky k propojenému učení,  
- od „učitelského přenosu“ k profesně vedené podpoře porozumění.

Tato změna umožní českému vzdělávání vystoupit z dlouhodobého paradoxu a vytvořit systém, který je spravedlivý, měřitelný a zároveň moderní —  
systém, který připraví žáky na svět, kde znalost a kompetence nejsou protiklady, ale dvě strany téhož procesu.
""",
    
    "Funkční gramotnost":
"""
### Co přesně znamená funkční gramotnost a proč je klíčová pro naše články i pro moderní vzdělávání

V českém prostředí se pojem *gramotnost* často zaměňuje s „umět číst“, „umět psát“ nebo „umět počítat“. Na mezinárodní úrovni však slovo **gramotnost (literacy)** znamená mnohem víc. Označuje schopnost **používat znalosti a dovednosti v reálných situacích**, ne pouze schopnost zvládnout učivo.

Tento širší význam se používá v PISA, OECD, EU, UNESCO a také v českých kurikulárních materiálech (gramotnosti RVP ZV).

**Funkční gramotnost tedy není „doplňková dovednost“.  
Je to schopnost fungovat v moderní společnosti, řešit problémy, porozumět informacím a činit rozhodnutí.**

Proto tvoří klíčový prvek změny paradigmatu, kterou v našich článcích popisujeme.

## 1. Funkční gramotnost = použití znalostí v praxi

Zjednodušeně řečeno:

**Funkční gramotnost = schopnost použít znalosti, dovednosti a porozumění v reálných situacích tak, aby člověk dokázal úkol splnit, vyřešit problém nebo porozumět informaci.**

Nejde tedy o to, „co si dítě zapamatuje“, ale o to:

- zda dokáže číst s porozuměním i delší text, návod, jízdní řád, smlouvu,  
- zda rozumí grafu, tabulce, mapě, cenám, údajům, statistikám,  
- zda dokáže propojit informace a vytvořit si z nich vlastní závěr,  
- zda umí ověřit, zda je výsledek realistický,  
- zda umí rozpoznat chybu (včetně chyby, kterou vyrobí AI),  
- zda použije matematiku či jazykové dovednosti jako nástroj – nikoli samoúčelně.

**Funkční gramotnost je tedy měřitelná dovednost, nikoli abstraktní kompetence.**

## 2. Funkční gramotnost není totéž co „kompetence“

Kompetence se týkají způsobů práce – jak žák přemýšlí, spolupracuje, řeší problémy, komunikuje.

Funkční gramotnost naproti tomu říká, *zda umí pracovat s obsahem*, například:

- přečíst text a něco z něj vyvodit,  
- vyřešit matematickou situaci,  
- porozumět grafu,  
- zvládnout vědecký postup,  
- využít digitální nástroje k řešení úkolu.

Proto je **funkční gramotnost obsahová osa**, zatímco **kompetence jsou procesní osa**.

Obojí je nezbytné – a dohromady tvoří přesně to, co popisujeme jako **kompetenčně-znalostní model**.

## 3. Funkční gramotnosti podle OECD (a jejich význam pro ČR)

### a) Čtenářská gramotnost  
Schopnost pracovat s texty všech typů. Nejde o rychlost čtení, ale o porozumění, analýzu, interpretaci a kritickou práci s informacemi.

### b) Matematická gramotnost  
Schopnost používat matematiku k řešení problémů – převádět situace na modely, počítat, interpretovat výsledek, pracovat s mírou, rizikem a pravděpodobností.

### c) Přírodovědná gramotnost  
Schopnost chápat přírodní jevy, vyvozovat závěry z dat, používat vědecké postupy, porozumět grafům a měřením.

### d) Digitální gramotnost  
Schopnost orientovat se v digitálních prostředích, vyhledávat a ověřovat informace, pracovat s nástroji, chránit data, tvořit obsah.

Tyto gramotnosti nejsou „moderní móda“.  
Jsou to základní podmínky fungování člověka ve společnosti, kde se všechno mění rychleji, než škola stíhá reagovat.

## 4. Proč je funkční gramotnost klíčová?

**Kompetence bez měřitelné obsahové báze jsou prázdné.  
Znalosti bez použití jsou neživotné.  
Funkční gramotnost spojuje obojí.**

Je to právě funkční gramotnost, která:

- vysvětluje rozpor mezi tím, co školy učí (kompetence), a tím, co se ověřuje (znalosti),  
- umožňuje zavést standardy, které nejsou vágní, ale měřitelné,  
- je protikladem k neustálému přezkušování faktů bez porozumění,  
- dává logický rámec přijímacím zkouškám i CERMAT testům,  
- odhaluje, proč rodiče investují do příprav navíc,  
- vysvětluje, proč AI mění požadavky na vzdělávání, ale nezrušila potřebu znalostí,  
- propojuje výuku na základních školách se strategickými potřebami regionů.

Funkční gramotnost je zároveň jediná skutečně mezinárodně srovnatelná metrika,  
která umí ukázat kvalitu vzdělávání v čase (PISA, PIRLS, PIAAC).

## 5. A konečně: funkční gramotnost je podmínkou pro kontrolu umělé inteligence

Toto je nové, ale zásadní:

**Aby dítě poznalo, že AI udělala chybu, musí mít vlastní znalostní a gramotnostní rámec.  
Bez něj je žák – i vysokoškolák – zcela bezbranný.**

Tím se funkční gramotnost stává nejen cílem vzdělávání, ale **základním bezpečnostním prvkem života v 21. století**.
""",
"Kompetence plus":
"""
### Kompetence plus

## 1. Význam slova „kompetence“

Slovo *kompetence* má původ v latinském **competere**, které znamenalo:

- setkávat se, shodovat se,  
- patřit k něčemu,  
- být způsobilý (mít oprávnění či schopnost) něco vykonat.

V pozdní latině a středověké správě znamenala *compententia*:

- příslušnost k pravomoci, tedy „co někomu náleží“ (kompetence úřadu),  
- a postupně způsobilost konat určitou činnost správně a účinně.

Moderní pedagogické užití navazuje na oba významy:

- **kompetence jako způsobilost** (žák něco umí udělat),  
- **kompetence jako příslušnost** k určité činnosti (patří do portfolia vzdělaného člověka).

Zásadní je, že kompetence **nikdy nebyla synonymem obsahu**.  
Obsah (knowledge) a kompetence (competence) jsou v mezinárodních přístupech **dvě různé, ale propojené dimenze**.

## 2. Původní československé osnovy – dovednosti, vědomosti, návyky

Tradiční československé osnovy měly jasnou logiku, která vycházela z didaktiky 20. století:

### **1) Vědomosti – co má žák znát**  
Fakta, pojmy, vztahy, postupy, pravidla – od vět „naučit se vyjmenovaná slova“ po „umět početní výkony“.  
Znalostní minimum bylo obsahem kurikula.

### **2) Dovednosti – co má žák umět udělat**  
Aplikace vědomostí do praxe: číst plynule, počítat příklady, řešit slovní úlohy, psát sloh, kreslit mapu.

### **3) Návyky – jak má žák pracovat**  
Pracovní postupy, soustředění, systematičnost, píle, přesnost, opakování, řád, pečlivost.

Tato trojice **vědomosti–dovednosti–návyky** byla nesmírně praktická:

- učitel přesně věděl, *co se má učit* (obsah),  
- věděl, *jak se to má učit* (postupy),  
- a věděl, *k čemu směruje* (dovednosti a návyky).

Osnovy tedy poskytovaly pevnou oporu pro **tvorbu učebnic**, **plánování výuky** i **hodnocení**.  
Škola nebyla postavena na abstraktních cílech, ale na **konkrétních výstupech**, které byly společné pro všechny.

## 3. Přechod ke klíčovým kompetencím – evropský trend, česká implementace

Po roce 2005 se Česká republika rozhodla následovat evropský trend kompetenčně orientovaného kurikula.  
Vznikly **RVP ZV, RVP G, RVP SOV**, které obsahovaly šest klíčových kompetencí:

- k učení,  
- k řešení problémů,  
- komunikativní,  
- sociální a personální,  
- občanské,  
- pracovní.

### Problém však nastal ve způsobu implementace:

**Klíčové kompetence byly do RVP vloženy bez pevné vazby na obsah (učivo).**

Zatímco ve Finsku, Rakousku, Irsku či Německu kompetence fungují jako **procesní osa**, která se pojí k jasně definovaným obsahovým standardům, v české verzi:

- byly ponechány nekonkrétní, vágní („žák volí vhodné způsoby…“, „spolupracuje…“, „řeší problémy…“),  
- nebyly provázány s učivem jednotlivých ročníků,  
- nebyly doplněny měřitelnými znalostními standardy,  
- zůstaly oddělené od očekávaných výstupů.

Tím vzniklo prostředí, kde:

- učitelé nevědí přesně, *co mají učit*,  
- školy mají široký interpretační prostor,  
- učebnice nemají jednotnou strukturu,  
- a hodnocení se vrací ke znalostem (CERMAT), protože ty jsou jediné měřitelné.

Jinými slovy:

**Kompetence byly přidány, ale obsah byl rozpuštěn.**  
Výsledkem je dualita: školství deklarativně učí kompetence, ale reálně hodnotí znalosti.

## 4. Problém tvorby učebnic bez pevných osnov

Učebnice jsou nástroj závislý na kurikulu.  
Když nejsou pevné osnovy, nastává několik zásadních problémů:

### **a) Učebnice nejsou kompatibilní mezi sebou**  
Některé začínají jiným pořadím témat, jiné vynechají důležité pojmy, další přidají jiné.

### **b) Učitel je nucen tvořit vlastní kurikulum**  
Namísto výuky tráví obrovské množství času plánováním, *co se má učit*.

### **c) Výstupy žáků jsou nerovnoměrné**  
Učebnice určují, co se děti naučí — ale nejsou jednotné.  
Tím vznikají rozdíly mezi školami, třídami i regiony.

### **d) Neexistuje horizontální návaznost mezi ročníky**  
Protože obsah není závazný, logická návaznost se ztrácí.

### **e) Kompetence učebnici nenahradí**  
Kompetence popisují *jak žák pracuje*, ale ne *s čím pracuje*.  
**Bez obsahu nemá kompetence co rozvíjet.**

## 5. Shrnutí: proč je kompetenčně-znalostní model nutný

Původní osnovy fungovaly, protože poskytovaly:

- jasný obsah,  
- jasné očekávání,  
- jednotnou strukturu,  
- oporu pro učebnice,  
- rovnost mezi školami.

Klíčové kompetence jsou užitečné, ale česká implementace je neúplná, protože:

- není provázána s obsahem,  
- chybí znalostní standardy,  
- vyvolává nerovnosti,  
- neumožňuje systematické měření.

### **Řešením není návrat k osnovám ani čistý kompetenční model, ale propojení obojího:**

**kompetence (proces)**  
**znalosti a gramotnosti (obsah)**  
**komplexní úlohy (aplikace)**

Takový rámec používají Rakousko (iKM+), Německo, Kanada, Singapur i Finsko.  
**A právě tímto směrem míří koncept **Kompetence plus.**

""",
"Rodiče":
"""
### Proč děti potřebují pevné základy: role rodiče a učitele v době umělé inteligence

Dnes se často říká, že děti už nepotřebují tolik vědomostí jako dřív. Všechno si přece mohou najít na internetu, většinu příkladů spočítá mobil a složitější věci vysvětlí umělá inteligence. Je proto snadné nabýt dojmu, že školní „drezura“ znalostí už nemá smysl a že bychom měli učit hlavně kreativitu, komunikaci a spolupráci.

Jenže skutečnost je úplně jiná. **Právě v době umělé inteligence děti potřebují pevný základ víc než kdykoliv předtím.**

## Proč nestačí, že „to najdou na internetu“

Umělá inteligence umí napsat úkol, vysvětlit příklad nebo vymyslet projekt. Umí to rychle, sebevědomě a na první pohled správně. Jenže má jednu zásadní slabinu: **občas udělá chybu**. Takovou, kterou pozná jen člověk, který opravdu rozumí tomu, co čte nebo počítá.

Dítě, které nemá jistotu v základním čtení, psaní nebo počítání, nemůže poznat, že mu AI podstrčila nesmysl. Nemá podle čeho. A právě proto jsou základní znalosti ještě důležitější než dřív.

**Základy nejsou přežitek. Jsou podmínkou samostatnosti.**

Číst s porozuměním, psát čitelně a bez velkých chyb, počítat tak, aby si dítě bylo jisté výsledkem — to není „staromódní škola“. To je základ všeho ostatního.

Bez toho se dítě:

- nedokáže učit samo,  
- nedokáže posoudit správnost informace,  
- nedokáže se orientovat v dnešním světě plném textů, dat a tvrzení.

Stejně jako dům potřebuje základy, potřebuje je i vzdělání.

## Proč jsou pracovní návyky důležitější než kdy dřív

V posledních letech přibývá myšlenka, že hlavní je „umět řešit problémy“. Ano, ale **dítě, které se nenaučilo soustředit, dokončit úkol, napsat větu pečlivě nebo spočítat příklad bez spěchu**, těžko zvládne komplexní úlohy, které budou na druhém stupni nebo střední škole.

Pečlivost, soustředěnost a jistota nejsou vrozené vlastnosti. Jsou to **návyky**. A ty se budují právě na jednoduchých úkolech:

- čtení,  
- psaní,  
- počítání,  
- rýsování,  
- měření,  
- procvičování.

**Zrychlení přeskočit nelze.**  
Kdo přeskočí základy, ten se později ztratí.

## Učitel není jen průvodce. Je to člověk, který vede k jistotě.

Dobrá elementaristka nebo dobrý elementarista má obrovskou roli. Ukazuje dětem, jak pracovat s jednoduchými nástroji, jak si kontrolovat výsledek, jak se nebát chyby a jak se postupně zlepšovat.

Učitel vede dítě krok za krokem — od prvních písmenek až k tomu, že si umí samo přečíst a pochopit úkol.

- Učí ho, jak si výsledek ověřit.  
- Učí ho, jak dokončit práci.  
- A hlavně: **učí ho věřit si**.

Umělá inteligence může hodně věcí nahradit, ale tento lidský proces učení nahradit neumí.

## Komplexita přijde. Ale až potom.

Je jasné, že děti budou v budoucnu potřebovat umět přemýšlet v souvislostech, řešit složitější úkoly a používat digitální technologie. To je nezbytné a je správné, že škola na to myslí.

Ale **komplexitu se dítě nenaučí „místo základů“. Naučí se ji navíc k nim.**

Teprve když dítě:

- umí číst,  
- umí psát,  
- umí počítat,

dokáže pochopit graf, porozumět delšímu textu, poznat chybu, ověřit výsledek a kriticky pracovat s informacemi.

**Komplexita není začátek. Je to vrchol.**

## Co z toho vyplývá pro nás rodiče

Role rodiny je jednoduchá, ale nesmírně důležitá:

- podporovat dítě v dokončování práce,  
- chválit ho za úsilí, ne za rychlost,  
- oceňovat pečlivost,  
- motivovat ke čtení,  
- vytvářet podmínky pro soustředění,  
- vést dítě k tomu, že chyba je normální součást učení.

Škola může udělat hodně, ale **pevný základ je vždy společné dílo učitelů a rodičů**.

## Závěrem: pevné základy nejsou proti moderním technologiím, ale pro ně

Děti, které mají jistotu v základech, jsou ty, které budou jednou umět využívat technologie **smysluplně, kriticky, tvořivě a samostatně**.

Děti, které základy nemají, budou na technologiích:

- závislé,  
- nejisté,  
- a nedokážou poznat, kdy se mýlí.

Úkolem školy i rodiny není konkurovat umělé inteligenci, ale dát dětem to, co ona neumí: **pevné základy, jistotu, soustředění a schopnost rozlišit správné od nesprávného**.

To je skutečná výbava pro 21. století.
""",

"Učitelé":
"""
### Roli učitele dnes podceňujeme. Přitom je důležitější než kdykoliv předtím.

Ve veřejné debatě o školství se často objevuje myšlenka, že učitel už není tím, kdo předává znalosti. Předpokládá se, že žáci si vše dokážou vyhledat sami, učební postupy najdou na internetu a na dotazy odpoví umělá inteligence. Tím vzniká nebezpečný omyl: že učitel ztrácí význam. Skutečnost je pravý opak. **Právě v době digitálních technologií a umělé inteligence je učitelova role zásadnější než kdy dřív.** Ne proto, že má žákům říkat věci, které lze dohledat, ale protože vytváří podmínky, bez nichž se žádné skutečné učení nemůže odehrát.

## Učitel nevysvětluje jen látku. Učí dítě, jak se učit.

Dnešní dítě je obklopené informacemi — někdy správnými, někdy nesmyslnými, často protichůdnými. Umí je však zpracovat? Umí poznat, co je podstatné? Umí vyhodnotit, čemu věřit a čemu ne?

V tom spočívá první klíčová role učitele: **dává učení strukturu**.

Učitel pomáhá dítěti orientovat se v chaosu. Třídí, vysvětluje, propojuje. Dává směr. Vede dítě k tomu, aby si všímalo vztahů, pochopilo, jak věci souvisí, a aby se naučilo klást otázky. Jeho úkolem není naučit žáka všechno, ale předat mu způsob, *jak poznání vzniká* a *jak se k němu dostat*. Bez učitele by se dítě v množství informací ztratilo.


## Učitel vytváří pracovní návyky — základ každého výsledku

Soustředění, vytrvalost, pečlivost, schopnost dokončit úkol, zodpovědnost — to nejsou vrozené vlastnosti.  
To jsou **návyky**, které dítě přejímá z prostředí, v němž pracuje.

A právě učitel je tím, kdo toto prostředí utváří.

Ve třídě vytváří rytmus, dává očekávání, pomáhá dítěti pracovat krok za krokem. Ukazuje mu, že úkol má začátek a konec, že přesnost se vyplácí a že vytrvalost přináší výsledky.

V době, kdy je vše digitální, rychlé a zkratkovité, je systematická práce dítěte jedním z nejcennějších darů, které může škola nabídnout. Umělá inteligence může vytvořit odpověď — **ale nenaučí dítě vytrvat nebo být pečlivé**. To dokáže jen učitel.

## Učitel je garantem pevného základu

Čtení s porozuměním, jistota v aritmetice, schopnost vyjádřit myšlenku, orientace v základních faktech — to není zastaralý model výuky. To je **základ, na kterém stojí komplexní myšlení**.

Učitel je ten, kdo hlídá, aby tento základ vznikl.

Pod jeho vedením dítě postupně získává jistotu:  
umí číst, rozumí textu, dokáže spočítat příklad, vyjádřit myšlenku, ověřit výsledek.

Bez této jistoty se žák později v matematice, jazyce ani v životě neobejde.

Na první pohled se může zdát, že technologie tyto věci usnadňují. Ale technologie mohou nahradit jen postup, ne porozumění. **A bez porozumění nemá strategie ani algoritmus žádnou hodnotu.**  
Učitel hlídá, aby se dítě naučilo chápat podstatu — ne jen opisovat postupy.

## Učitel je korektor umělé inteligence a kompas v době nejistoty

V době, kdy AI dokáže zmást i dospělého, je učitel jediným člověkem ve třídě, který dokáže vysvětlit, proč je něco špatně, jak poznat chybu a jak ji opravit.

Když umělá inteligence vytvoří přesvědčivou, ale chybnou odpověď, žák bez znalostního základu nemá šanci to poznat.

Učitel učí žáky nejen látku, ale **způsob ověřování**:

- Podívej se na jednotky.  
- Zkus výsledek odhadnout.  
- Vysvětli, proč si myslíš, že to tak je.

To jsou dovednosti, které AI neumí a které dítě nenaučí technologie.

Učitel dává žákům nejen znalosti, ale **dovednost orientovat se** v době, kdy už samotné informace nejsou spolehlivé.

## Učitel je vzorem — a vzory nelze digitalizovat

Každý z nás si pamatuje učitele, který ho podporoval, povzbudil, pomohl, ukázal cestu, nebo otevřel oči tam, kde to jiní nedokázali. To není náhoda.  
Dítě se neučí jen z učebnic. Učí se z lidí kolem sebe.

Učitel svým jednáním ukazuje, jak:

- zacházet s chybou,  
- reagovat na problém,  
- komunikovat s druhým,  
- přemýšlet nahlas,  
- sdílet radost z úspěchu,  
- zvládat neúspěch.

Digitální technologie dokážou napodobit mnoho věcí, ale nenapodobí osobní vztah, povzbuzení ani lidskou oporu. **Učitel vychovává nejen mozek, ale i charakter.**

## Učitel je architekt komplexního myšlení

Když dítě získá základní dovednosti, právě učitel ho vede dál — k pochopení vztahů, k širším tématům, k práci s daty, k interpretaci informací.

**Komplexní myšlení přichází až tehdy, když je postaveno na pevném základě.**

Učitel zná správný okamžik, kdy dítěti znalosti „přerůstají v porozumění“.  
Dobří učitelé vědí, kdy zjednodušit, kdy zpomalit, kdy naopak otevřít širší perspektivu.  
Jsou to oni, kdo vytvářejí most mezi jednoduchým a složitým.

Bez učitele by se komplexita stala pouze abstraktním pojmem — a ve skutečnosti nedosažitelným cílem.

## Závěrem: Učitel je nejdůležitější proměnná každé reformy

Ať se mění učební plány, technologie nebo politická atmosféra, jedna věc zůstává stálá: **kvalita učitele**.

Učitel je ten, kdo dává dětem smysl ve světě informací, jistotu v práci, odvahu v učení a lidský rámec v digitálním chaosu.

**Učitel není přežitek minulosti.  
Učitel je budoucnost školy.**

A pokud to společnost pochopí, pochopí i to nejdůležitější:  
že žádná reforma nebude úspěšná, pokud nezačne právě u lidí, kteří každý den stojí před dětmi — a konají jednu z nejdůležitějších profesí vůbec.""
""",

"Žáci a studenti":
"""
### Proč jsou učitelé důležití – i v době mobilů, Google a umělé inteligence

Možná máš občas pocit, že ve škole děláš věci, které bys „stejně našel na internetu“.  
Možná ti připadá, že učitel jen říká něco, co si můžeš vyhledat za pár vteřin.  
A možná si myslíš, že je to celé zastaralé.

Ale realita je jiná.  
A je mnohem zajímavější, než se zdá.

## 1. Umělá inteligence ti všechno neřekne správně. Ty musíš poznat rozdíl.

Dnes umí AI napsat sloh, spočítat příklad, vysvětlit látku nebo vyhledat informace rychleji než člověk.  
Jenže někdy se splete. A někdy dokonce vymyslí úplný nesmysl — a přitom to zní strašně chytře.

A tady přichází na řadu tvoje hlava.

Když nepoznáš, co je správně a co ne, staneš se jen pasivním příjemcem informací.  
Ale když umíš poznat chybu, dokážeš AI využívat tak, abys byl o krok napřed.

A přesně proto tě učitelé učí základní věci:

- jak číst tak, aby sis věci fakt zapamatoval,  
- jak počítat tak, aby sis výsledek uměl ověřit,  
- jak psát tak, aby tvé myšlenky dávaly smysl.

To jsou dovednosti, které žádná umělá inteligence nenahradí.

## 2. Překvapení: nejdůležitější věci se nenaučíš z mobilu

Mobil ti řekne odpověď.  
Ale **nenaučí tě pracovat**.

Pracovní návyky — soustředění, vytrvalost, dokončení úkolu, pečlivost — vznikají jen tehdy, když na sobě makáš, i když se ti nechce.  
A když máš kolem sebe lidi, kteří tě povedou.

Tvoje schopnost pracovat (a nejen kliknout) je něco, co rozhodne o tom, jak dobře se ti povede ve škole i v životě.

Učitel ti ukazuje, jak se dělá práce, která má začátek, postup a výsledek.  
A to je dovednost, bez které bys později nemohl dělat nic složitějšího — ani s AI.

## 3. Učitel není jen člověk, který stojí před tabulí

Možná si to neuvědomuješ, ale učitel je člověk, který ti každý den pomáhá pochopit svět.

Když vysvětluje, vede tě k tomu, abys své myšlenky dal dohromady.  
Když tě opraví, není to proto, že ho to baví, ale protože ví, že chyba je cesta k učení.  
Když tě pochválí, dává ti sílu pokračovat.

Učitel není robot.  
Učitel reaguje na tebe — podle toho, jak přemýšlíš, co potřebuješ, kde tápeš.  
A to žádná aplikace neumí.

## 4. Základy nejsou nuda. Základy jsou síla.

Každý sportovec musí nejdřív zvládnout techniku.  
Každý hudebník musí umět stupnice.  
Každý programátor musí znát logiku.

A každý člověk musí umět:

- dobře číst,  
- dobře psát,  
- dobře počítat.

Bez toho nejsi svobodný — ne ve světě, kde informace přicházejí ze všech stran.

Když nemáš základy, neumíš říct „tohle je blbost“ nebo „tohle se mi nezdá“.  
A to je v době internetu a AI nebezpečné.

Základy nejsou věci, které tě brzdí.  
Naopak — **umožňují ti být rychlejší, chytřejší a samostatnější**.

## 5. Komplexní věci přijdou — ale až tehdy, když budeš mít na čem stavět

Učitelé dnes mluví o „souvislostech“, „kritickém myšlení“ a „komplexních úlohách“.  
A mají pravdu — budeš je potřebovat.

Ale komplexita a souvislosti nejsou start.  
**Je to cíl.**

Nejdřív se naučíš jednotlivé kroky.  
Pak je spojíš dohromady.  
A pak zjistíš, že umíš víc, než sis myslel.

To je moment, kdy tě učitel nechá tvořit.  
A kdy ti AI pomůže.

Ale musíš k tomu nejdřív dorůst.

## 6. A proč to všechno? Protože jde o tebe.

Na svět přicházejí nové technologie, které mohou být úžasné — ale jen pokud jim dokážeš porozumět a používat je bezpečně.  
Aby ses ve světě neztratil, potřebuješ někoho, kdo tě naučí, jak na to.

Ten někdo je **tvůj učitel**.

Ať už se ti to zdá nebo ne, učitel je dnes tvůj nejdůležitější spojenec.  
Pomáhá ti získat dovednosti, které budou rozhodovat o tvé budoucnosti — bez ohledu na to, kolik nových aplikací a AI nástrojů přijde.

Protože škola není jen o tom, co se naučíš.  
Je hlavně o tom, **kým díky tomu můžeš být**.
""",


}

# -----------------------
# LOGIKA – získání textu
# -----------------------

def get_content(topic: str) -> str:
    """Vrátí text podle zvoleného tématu."""
    return CONTENT.get(
        topic,
        "*(Pro toto téma zatím není připraven text.)*",
    )



# -----------------------
# SIDEBAR – výběr
# -----------------------

st.sidebar.title("Obsah")

topic = st.sidebar.selectbox(
    "Téma",
    list(TOPICS.values()),
    index=0,  # výchozí: Změna paradigmatu
)



st.sidebar.markdown("---")


# -----------------------
# MAIN PAGE
# -----------------------

st.title("📊 kompetence+")


st.markdown("---")

text = get_content(topic)
st.markdown(text)


