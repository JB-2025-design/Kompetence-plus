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
    "Analytický rozbor PISA 2022 v kontextu českého kurikula, kompetencí a AI gramotnosti":"Analytický rozbor PISA 2022 v kontextu českého kurikula, kompetencí a AI gramotnosti",
    "Kompetence plus": "Kompetence plus",
    "Rodiče": "Rodiče",    
    "Učitelé": "Učitelé",
    "Žáci a studenti": "Žáci a studenti",     
    "Slovní hodnocení": "Slovní hodnocení",
    "AI gramotnost jako nová součást vzdělávacího paradigmatu":"AI gramotnost jako nová součást vzdělávacího paradigmatu",
    "Komenského vize jako základ kompetenčně-znalostního modelu pro 21. století": "Komenského vize jako základ kompetenčně-znalostního modelu pro 21. století",
    "Hierarchie pojmů a kompetenčních úrovní": "Hierarchie pojmů a kompetenčních úrovní",
    "Znalosti + kompetence":"Znalosti + kompetence"
        
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

Současná debata o podobě českého kurikula se již dvacet let opírá o kompetenční model vzdělávání, který se stal východiskem rámcových vzdělávacích programů i návrhů jejich revizí. Kompetence jsou zásadní pro přípravu žáků na proměnlivý svět: mají podporovat samostatné myšlení, řešení problémů, komunikaci, spolupráci, digitální gramotnost a schopnost učit se. Tyto požadavky odpovídají globálním trendům i potřebám společnosti založené na informacích.

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

## 2. Původní osnovy – dovednosti, vědomosti, návyky

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
A právě tímto směrem míří koncept **Kompetence plus.**

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
    "Slovní hodnocení":
"""
## Slovní hodnocení
Slovní hodnocení dnes přichází do škol v době, kdy se celý český vzdělávací systém potýká s hlubší, dlouhodobou nejasností: vágností kompetenčního modelu, na němž jsou postaveny rámcové vzdělávací programy. Stejně jako slovní hodnocení, i kompetence byly do systému zavedeny s dobrým úmyslem, ale bez přesného vymezení obsahu, úrovní a kritérií. Výsledkem je dvojí vágnost: vágní kompetence se potkávají s vágním hodnocením.

Pokud slovní hodnocení popisuje dovednosti, které nejsou pevně ukotvené v žádném standardu, nemůže být srozumitelné, spravedlivé ani měřitelné. Existuje reálné riziko, že se slovní hodnocení stane pouze „obecným komentářem“ k výkonu dítěte, podobně jako kompetence v RVP zůstaly roky obecnými ideály bez konkrétního obsahového ukotvení. Stejně jako věta „žák řeší problémy“ neříká, jaké problémy, jakým způsobem a v jaké úrovni, tak ani věta „žák se zlepšil“ neříká, v čem přesně, o kolik, nebo zda to odpovídá očekávanému standardu daného ročníku.

Tato vágnost je hlavním důvodem toho, že se systém stále vrací ke známkám. Ať už jsou známky sebevíc kritizované, mají jednu vlastnost, která v současném kurikulu chybí: jsou jednoznačné. Neříkají sice dost o procesu učení, ale dávají jasný signál o výsledku. Problém však není v samotné známce – problém je v tom, že známka nestojí na jasně definovaných kompetencích a standardech. Hodnotí se „pocitově“, na základě dojmů, podle individuálního výkladu učitele. A právě to lze změnit.

Jasně vymezené obsahové kompetence (co má dítě vědět a umět v jednotlivých oborech) a procesní kompetence (jak má žák přemýšlet, argumentovat, řešit úlohy, aplikovat poznatky) by umožnily navázat známkování i slovní hodnocení na konkrétní, měřitelný rámec. V praxi by to znamenalo, že známka už není subjektivní průměr pocitů, ale číselným vyjádřením toho, do jaké míry žák splňuje konkrétní standard. A slovní hodnocení by se stalo detailním popisem procesu podle jasné struktury – nikoli improvizovaným komentářem.

Pokud chceme slovní hodnocení, které je opravdu užitečné, a školství, které je skutečně kompetenční, musí obojí stát na stejném základě: na jednoznačném vymezení toho, co je výkon žáka, jaké jsou úrovně a jak vypadá očekávaný výsledek. Jen tehdy může být slovní hodnocení konkrétní, pravdivé a individuální. A jen tehdy může známka vyjadřovat něco jiného než náhodný signál.

Kompetenčně-znalostní model, který propojuje obsah (znalosti, gramotnosti) a proces (kompetence), vytváří cestu z dvojí vágnosti. Umožňuje hodnotit spravedlivě, srozumitelně a v souladu s tím, co má být skutečným cílem vzdělávání: porozumění, růst a schopnost obstát v komplexním světě. Slovní hodnocení i známky mohou být smysluplné – pokud stojí na sdíleném, jasně popsaném rámci.

## Gramotnosti jako chybějící druhá dimenze

Řada evropských zemí tento problém vyřešila tak, že do vzdělávacích standardů vložila druhou dimenzi, která doplňuje kompetence o obsah. Rakouský model iKM PLUS je v tomto ohledu příkladem dobré praxe: vedle procesních kompetencí (modelování, počítání, interpretace, argumentace) pracuje s jasnými obsahovými oblastmi (čísla, algebra, geometrie, statistika). Každý test i úloha tak ověřuje dvě věci najednou:
– jak žák postupuje (proces),
– zda postup vede ke správnému výsledku (obsah).

V novém českém RVP existují gramotnosti, ale nejsou zakotveny jako funkční součást hodnoticí matice. Nepůsobí jako druhá osa, která by kompetence ukotvila. Jsou spíše doprovodným dokumentem, druhořadým vysvětlením, nikoli strukturovaným standardem.

Právě gramotnosti jako druhá dimenze by umožnily, aby kompetence nezůstaly vágní a aby školství bylo schopné výsledky žáků měřit a spravedlivě hodnotit.

## Komplexní úlohy jako třetí rozměr hodnocení

Rakousko jde dokonce ještě dál a pracuje s komplexními úlohami, které propojují více oblastí i více kompetenčních procesů. Takové úlohy reflektují realitu: skutečný problém není „o geometrii“ nebo „o procentách“. Je to problém, který vyžaduje kombinaci dovedností, modelování, výpočtů, ověřování i interpretace dat.

Podobná třetí dimenze by v ČR vytvořila systém, který:
– je porovnatelný,
– je měřitelný,
– podporuje kompetence,
– zároveň chrání znalostní minimum,
– a reflektuje reálné požadavky 21. století.

## Nutnost standardů jako podmínka spravedlivého školství

K tomu všemu se pojí jedna zásadní věc: potřebujeme standardy. Ne vágní formulace, ale jasná kritéria, která říkají:
– co přesně má žák umět,
– jak to ověřit,
– jak vypadá minimální úroveň,
– jaké jsou úrovně pokročilejší.

Standardy nejsou bič, ale kompas. Pomáhají učitelům, žákům i rodičům. Omezují chaos, sjednocují kvalitu a dávají školám jistotu. Bez nich bude paradox českého školství přetrvávat.

České školství dnes stojí na křižovatce mezi dvěma světy: konstruktivistickým ideálem kompetenční výuky a realistickým tlakem na ověřitelné znalosti. Jeden bez druhého nefunguje. Žák potřebuje pevné znalostní minimum, aby mohl rozvíjet kompetence, a kompetence, aby mohl své znalosti správně používat a dávat jim smysl.

Jestliže má česká škola připravit žáky na svět, kde budou muset korigovat umělou inteligenci, rozpoznávat chyby, přemýšlet v souvislostech a obstát v nejasném informačním prostředí, musí být kompetence doplněny o jasné obsahové standardy a učivo musí být zasazeno do dvou- až třírozměrné struktury hodnocení.

Teprve tehdy zmizí paradox, o kterém dnes všichni víme, ale který nikdo dosud nevyřešil.

# Demonstrace: Kompetenční matice (4. ročník ZŠ, české učivo)

### Obsahové oblasti – 4. třída
## Procesní kompetence × Obsah učiva (4. ročník)

| **Obsah učiva / Procesní kompetence** | **Čísla a operace do 1 000 000** | **Jednoduché závislosti** | **Geometrie** | **Data a grafy** |
|---------------------------------------|-------------------------------|----------------------------|----------------|------------------|
| **ZNÁZORNIT / MODELOVAT** | **Proces:** Žák převede slovní úlohu na příklad (např. „Máme 2450 Kč a utratíme 670 Kč…“ → 2450 − 670). **Výsledek:** Model odpovídá situaci; nejsou zaměněna čísla ani operace. | **Proces:** Žák vytvoří tabulku vztahu (např. počet balíčků – počet sušenek). **Výsledek:** Tabulka odpovídá pravidlu („1 balíček = 5 sušenek“). | **Proces:** Žák nakreslí obdélník podle popisu, vyznačí strany a pravoúhlé rohy. **Výsledek:** Model odpovídá zadání – strany jsou správné, tvar je obdélník. | **Proces:** Žák zakreslí jednoduchý sloupcový graf podle dat. **Výsledek:** Osové hodnoty i výška sloupců odpovídají údajům. |
| **POČÍTAT / PROVÁDĚT OPERACE** | **Proces:** Žák postupuje podle algoritmu (písemné sčítání, odčítání, násobení). **Výsledek:** Výpočet je správný (např. 367 + 458 = 825). | **Proces:** Žák doplní chybějící hodnoty podle pravidla (řada o 100, násobky 5). **Výsledek:** Všechny hodnoty odpovídají danému vztahu. | **Proces:** Žák vypočítá obvod obdélníku podle vzorce O = 2·(a + b). **Výsledek:** Výsledek odpovídá správnému výpočtu a jednotkám (např. cm). | **Proces:** Žák spočítá četnosti nebo porovná dvě hodnoty v tabulce. **Výsledek:** Výsledky přesně odpovídají datům. |
| **INTERPRETOVAT VÝSLEDEK** | **Proces:** Žák posoudí, zda výsledek (např. 825 Kč) dává smysl. **Výsledek:** Interpretace je správná – žák rozpozná nemožný výsledek (např. záporné peníze). | **Proces:** Žák vysvětlí, podle čeho se mění hodnoty v tabulce. **Výsledek:** Popis odpovídá pravidlu (např. přičítá se vždy 3). | **Proces:** Žák určí, zda útvar je pravoúhlý nebo zda plocha odpovídá měření. **Výsledek:** Závěr odpovídá skutečným rozměrům. | **Proces:** Žák přečte z grafu nejvyšší/nejnižší hodnotu. **Výsledek:** Výběr i interpretace odpovídají grafu. |
| **ARGUMENTOVAT / ZDŮVODŇOVAT** | **Proces:** Žák vysvětlí, proč zvolil násobení místo sčítání (např. „5 krabiček po 8 tužkách“). **Výsledek:** Zdůvodnění vede ke správnému výsledku. | **Proces:** Žák odůvodní pravidlo v číselné řadě. **Výsledek:** Závěr odpovídá všem hodnotám v řadě. | **Proces:** Žák vysvětlí, proč se jedná o obdélník nebo proč obvod vychází tak, jak vychází. **Výsledek:** Zdůvodnění odpovídá vlastnostem útvaru. | **Proces:** Žák vysvětlí, proč je určitý sloupec vyšší než jiný a co to znamená. **Výsledek:** Argumentace správně odpovídá datům. |


Tato matice ukazuje, jak lze i na prvním stupni ZŠ (zde konkrétně ve 4. třídě) propojit kompetence s obsahem učiva, podobně jako v rakouském iKM PLUS. Žák je hodnocen dvěma způsoby:

• procesně: jak uvažuje, jak sestaví model, jak postupuje, jak argumentuje;  
• výsledkově: zda jeho řešení dává smysl, je správné a odpovídá realitě.

Právě tato dvojí optika — postup + správnost — v českém RVP dlouhodobě chybí. Rakouský model ukazuje, že i malé děti lze vést k přesné formulaci problémů, jednoznačnému modelování a k tomu, aby nejen spočítaly výsledek, ale i věděly, proč je správný.

Následující část vysvětluje, jak má vypadat hierarchie a vazby v kompetenčně-znalostním modelu, pokud stojí na stupňovitosti:

Znalosti → Gramotnosti → Kompetence → Komplexita  
a zároveň hodnotí obsahové i procesní kompetence v rámci každého předmětu.

## Model čtyřúrovňové závislosti ve vzdělávání

Tento model řeší hlavní problém českého kurikula: kompetence existují, ale nejsou k ničemu připojené. Výsledkem je roztříštěnost výuky, nejednotné hodnocení a neschopnost popsat výkon žáka přesně.

Nový model pro střední školy staví na jasně definované vertikále čtyř úrovní:

1. ZNALOSTI (Knowledge) – základní úroveň

Otázka: Co žák zná?

Znalosti zahrnují fakta, pojmy, pravidla, postupy a struktury.  
Příklady:
• čísla, operace, jednotky  
• slovní druhy, čtenářské postupy  
• vlastnosti útvarů  
• přírodopisné pojmy  
• digitální nástroje a jejich funkce  

Znalosti jsou měřitelné. Vždy mají:
• minimální standard  
• jasný obsah pro daný ročník  
• konkrétní očekávané výstupy  

2. GRAMOTNOSTI (Literacies) – aplikační úroveň

Otázka: Jak žák používá znalosti v situacích?

Gramotnost = schopnost použít znalosti v reálných kontextech.  
Nejde o kompetence, ale o obsahové dovednosti s přesnými kritérii (podle OECD/PISA):

• čtenářská gramotnost – práce s textem  
• matematická gramotnost – modelování, výpočty, interpretace  
• přírodovědná gramotnost – práce s daty, pokusy, vysvětlení jevů  
• digitální gramotnost – práce s informacemi, nástroji, bezpečností  

Gramotnosti tvoří most mezi znalostí a kompetencí.

3. KOMPETENCE (Competences) – procesní úroveň

Otázka: Jak žák pracuje, přemýšlí a řeší problémy?

Kompetence popisují postup, nikoli výsledek. Říkají:

• jak žák volí strategii  
• jak propojuje informace  
• jak argumentuje  
• jak plánuje  
• jak spolupracuje  
• jak vyhodnocuje chybu  
• jak se učí  

Kompetence samy o sobě nic neříkají, pokud nejsou ukotvené v obsahu a gramotnostech.

4. KOMPLEXITA (Complex Tasks) – nejvyšší úroveň

Otázka: Jak žák řeší složité úlohy, kde se vše propojuje?

Komplexita znamená schopnost:

• kombinovat více znalostí  
• uplatnit gramotnosti  
• volit vhodné metody (kompetence)  
• řešit nejednoznačné, realističtější problémy  
• interpretovat data, simulace a schémata  
• korigovat chybu vlastní i chybu AI  

Komplexní úlohy jsou tím, na co má moderní vzdělávání žáka postupně připravovat – ale teprve tehdy, když má vybudovaný základ.

# Závěr

Slovní hodnocení i známky mohou fungovat –  
ale pouze tehdy, pokud stojí na **stejně pevném kompetenčně-znalostním rámci**. 

České školství dnes učí kompetence, ale zkouší znalosti.  
Tento rozpor lze překonat jen tehdy, když:

- kompetence dostanou obsah,
- gramotnosti se stanou druhou osou,
- komplexní úlohy třetí,
- a učivo bude mít jasné standardy.

Teprve pak bude možné hodnotit děti spravedlivě, srozumitelně a moderně.
""",
    
"AI gramotnost jako nová součást vzdělávacího paradigmatu": 
"""
# AI gramotnost jako nová součást vzdělávacího paradigmatu

Umělá inteligence je dnes prostředím, se kterým se žáci setkávají dříve než se složitější matematikou, literární teorií nebo fyzikou. Schopnost pracovat s AI není luxusní nadstavbou – přímo navazuje na čtenářskou, matematicko-logickou a přírodovědnou gramotnost. 

Mezinárodní rámce, včetně připravovaných standardů PISA 2029 pro AI Literacy, považují AI gramotnost za klíčovou schopnost, bez níž není možné rozvíjet komplexní kompetence pro 21. století.

## Co je gramotnost v oblasti AI?

AI gramotnost **není** „umět používat aplikace“.  
Stejně jako čtenářská gramotnost není jen čtení písmen a matematická gramotnost není jen počítání, AI gramotnost není jen psaní promptů.

Podle PISA 2029 zahrnuje tři hlavní oblasti:

### A) Porozumět
- co je model, algoritmus, tréninková data, předpojatost, halucinace, pravděpodobnostní výstup,  
- jak vznikají chyby AI a proč jsou přesvědčivé,  
- že AI negarantuje správnost ani pravdivost.

### B) Používat
- umět zadat úkol tak, aby měl smysl,  
- umět ověřit výstup (zejména čísla, grafy, tvrzení),  
- porovnat více zdrojů (AI není jediný autoritativní zdroj).

### C) Kriticky vyhodnotit (kritická kontrola)
- poznat, že AI udělala chybu,  
- rozlišit fakt, tvrzení a domněnku,  
- nenechat se zmást sebevědomým tónem chybných výstupů.

AI gramotnost je tedy schopnost AI **rozumět, používat ji a kriticky hodnotit** – bezpečně, eticky a vědomě.

## AI gramotnost stojí na základu, ne na technologiích

Z předběžné analýzy PISA-AI 2029 vyplývá klíčový závěr:

> **Žáci s nízkou čtenářskou a matematickou gramotností nedokážou AI efektivně použít – protože nerozeznají chybu.**

AI tak paradoxně prohlubuje nerovnosti:  
slabší žáci pouze reprodukují chyby, silnější žáci AI využívají k hlubšímu porozumění.

To potvrzuje model:

- **Znalosti** – bez pojmového rámce žák nepozná nesmysl.  
- **Gramotnosti** – bez čtení, práce s daty a grafy nelze nic ověřit.  
- **Kompetence** – bez argumentace, plánování a kontroly nelze AI použít smysluplně.  
- **Komplexita** – teprve zde AI skutečně pomáhá (simulace, modelování problémů).

AI gramotnost tedy není „další předmět“, ale **průřezová vrstva spojující všechny úrovně modelu**.

## Vědomosti – dovednosti – postoje (návyky)
Triáda OECD *knowledge–skills–attitudes* odpovídá českému členění:

**Vědomosti – dovednosti – postoje (návyky).**

### 1. Vědomosti (Knowledge): Co žák ví o AI
- jak fungují modely (vzory v datech, ne myšlení),  
- odkud se berou tréninková data,  
- co je halucinace a proč vzniká,  
- rozdíl mezi generativní AI a vyhledáváním,  
- riziko zaujatosti (bias) nebo chybných závěrů.

To jsou základní orientační informace, nikoli informatické podrobnosti.  
Bez nich nelze žádný výstup ověřit.

### 2. Dovednosti (Skills): Co žák dokáže s AI udělat
- formulovat dotaz přesně a jednoznačně,  
- ověřit výstup (jednotky, operace, logika),  
- rozpoznat chybu a pokusit se ji opravit,  
- interpretovat graf, tabulku nebo kód vytvořený AI,  
- používat AI jako nástroj učení, ne jako náhradu myšlení.

### 3. Postoje / návyky (Attitudes): Jak žák přistupuje k AI
- zvyk ověřovat informace,  
- porozumění rizikům (bezpečnost, manipulace),  
- schopnost odhalit dezinformaci, i když vypadá věrohodně,  
- odpovědné používání AI při učení,  
- ochota přemýšlet o hranicích automatizace.

Tyto návyky nejsou „měkké“.  
Jsou to **praktické bezpečnostní postoje**, bez nichž AI žákovi škodí.

## AI gramotnost jako chybějící vrstva v českém kurikulu

AI gramotnost se přirozeně hodí do čtyřstupňového rámce:

**Znalosti → Gramotnosti → Kompetence → Komplexita**

V českém RVP však zatím chybí:

- explicitní zmínka o AI,  
- jasná definice dovedností práce s AI,  
- kritéria bezpečného a odpovědného používání,  
- napojení na procesní kompetence (modelování, interpretace, argumentace).

Bez jasného obsahu není možné kompetence měřit, popisovat ani hodnotit.

## Co lze čekat od výsledků PISA-AI 2029

### 1) Silní čtenáři → nejlepší uživatelé AI
- ověřují tvrzení,  
- odhalují chyby,  
- kombinují AI s vlastní prací.

### 2) Slabší čtenáři → nejohroženější skupina
- přebírají odpovědi bez kontroly,  
- nerozumí logice ani faktům.

### 3) Matematicky silní žáci
- rozpoznají nesmyslné grafy či výpočty,  
- posoudí realističnost výsledku.

### 4) Slabší matematická gramotnost = slepá důvěra
- neumí odhadnout chybu,  
- přehlížejí falešné vzorce i nesprávné jednotky.

## Co z toho plyne pro vzdělávání

### Základní závěry:
1. **Bez znalostí není AI gramotnost.**  
2. **Bez gramotností není kontrola AI.**  
3. **Bez kompetencí není smysluplná práce s AI.**  
4. **Bez komplexity není reálné učení.**

AI se dá využít pro simulace, modely a projekty –  
ale jen tehdy, pokud žák rozumí samotnému problému.

## Závěr

AI gramotnost vrací do popředí to, co škola vždy měla učit:  
**přemýšlet správně, přesně a odpovědně.**

Je to nová součást vzdělávacího paradigmatu, která propojuje všechny složky:  
znalosti, gramotnosti, kompetence i komplexitu.  
Je nezbytná, chcete-li, aby žáci byli uživateli AI – **ne jejími oběťmi**.
""",

    "Komenského vize jako základ kompetenčně-znalostního modelu pro 21. století": 
"""
# Komenského vize jako základ kompetenčně-znalostního modelu pro 21. století

Strategie vzdělávací politiky ČR do roku 2030+ se vědomě vrací k odkazu Jana Amose Komenského — nejen jako k symbolickému zdroji, ale jako ke skutečnému metodickému základu. Komenský ve svých textech formuloval soubor principů, které dnes znovu nabývají významu, protože přesně odpovídají na problémy současného kurikula: roztříštěnost, vágnost kompetencí, přetížení obsahu, nejasné hodnocení a ztrátu orientace ve světě rychlých změn a umělé inteligence.

Komenského myšlenky lze systematizovat do čtyř oblastí, které překvapivě přesně kopírují moderní rámec:

**Znalosti – Gramotnosti – Kompetence – Komplexita.**

## 1. Účel vzdělávání: Člověk se stává člověkem vzděláním

> „Má-li se člověk stát člověkem, musí se vzdělat.“  
> „Škola je dílna lidskosti…“  
> „Všichni na jednom jevišti velikého světa stojíme…“

Pro Komenského je vzdělání procesem formování člověka — nikoli jen nabíráním informací. Vzdělaný člověk má být připraven rozumět světu, jednat v něm moudře a sloužit společnosti. To přesně odpovídá dnešnímu pojetí kompetencí, které nejsou cílem samy o sobě, ale jsou cestou k odpovědnému jednání, spolupráci a občanskému životu.

Dnešní doba k tomu přidává nový rozměr: orientaci v prostředí digitalizace, algoritmů a umělé inteligence. I zde Komenský rezonuje překvapivě přesně:

> „Cílem vzdělání a moudrosti je, aby člověk viděl před sebou jasnou cestu života, po ní opatrně vykračoval, pamatoval na minulost, znal přítomnost a předvídal budoucnost.“

To je velmi blízké dnešní AI gramotnosti: umět rozpoznat rizika, předvídat důsledky, ověřovat informace a chápat mechanismy digitálního světa.

## 2. Učení má být smysluplné, užitečné a opřené o pevné znalosti

> „Nic není marnějšího než vědět a učit se mnoho, totiž co nepřinese užitku.“  
> „Moudrý není ten, kdo ví mnoho věcí, nýbrž ten, kdo ví užitečné věci.“  
> „Práci škol usnadníme, vynecháme-li věci nikoli potřebné, nepříslušné, přílišné podrobnosti.“

Komenský kritizuje to, co kritizujeme i dnes: přeplněné osnovy, roztříštěnost obsahu a zahlcení dětí balastem. Znalosti mají být:

- výběrové,  
- jasné,  
- užitečné,  
- propojené,  
- měřitelné.

To je přesně role znalostí v moderním čtyřstupňovém modelu: tvoří základ, bez kterého nelze rozvíjet gramotnosti ani kompetence, a zároveň musí být redukované na to, co je skutečně nutné.

Komenský by dnešní RVP pravděpodobně kritizoval podobnými slovy jako v 17. století: mnoho „papírů“, nejasnost, chaos, podrobnosti bez účelu:

> „Ten zvyk trousit do obecenstva podle libé vůle jakékoli papíry musí naprosto přestat, jakožto pařeniště všeho zmatku.“

## 3. Učitel jako vedoucí učení, nikoli pasivní „průvodce“

> „Posláním od začátku do konce budiž hledati způsob, aby učitelé méně učili, žáci se však více naučili…“  
> „Naši učitelé nesmějí být podobni sloupům u cest, které ukazují, kam jít, ale samy nejdou.“

V posledních letech se v české debatě zabydlelo zjednodušené heslo: *učitel má být průvodce*. Často je však vykládáno tak, že učitel má pouze sledovat zájmy žáků, poskytovat jim prostor a být spíše nenápadným moderátorem. Tento výklad je nejen neúplný, ale odporuje jak pedagogickému výzkumu, tak i samotnému odkazu Jana Amose Komenského.

Komenský učitele nikdy nechápal jako pozorovatele či facilitátora. Naopak — učitel je podle něj **vedoucí učení**, člověk, který:

- organizuje učení,  
- staví jasnou strukturu,  
- určuje směr,  
- odlišuje podstatné od nepodstatného,  
- vyžaduje vytrvalost, přesnost a myšlení,  
- je osobním vzorem práce, kultivovanosti a charakteru.

> „…aby učitelé méně učili, žáci se však více naučili…“ neznamená menší roli učitele, ale **efektivnější roli**: méně mluvení, více řízené, smysluplné činnosti.

> „Naši učitelé nesmějí být podobni sloupům u cest…“

Učitel nemá stát stranou. Má jít první a ukazovat cestu vlastním krokem.

Moderní didaktika to potvrzuje: učení je účinné tehdy, když je řízené odborníkem, nikoli ponechané samo sobě. Učitel je vedoucí, který:

- volí cíle, důraz a posloupnost,  
- udržuje úroveň náročnosti,  
- vysvětluje strategie a myšlenkové postupy,  
- poskytuje okamžitou zpětnou vazbu,  
- kultivuje jazyk, myšlení a argumentaci,  
- nese odpovědnost za růst každého dítěte.

To je zásadní rozdíl proti chápání učitele jako „průvodce zájmů“. Dětské zájmy jsou důležité, ale samy o sobě neuvedou žáka do světa komplexity, matematiky, logiky, přírodovědných zákonů, etiky ani technologie.

**Učitel jako vedoucí** zajišťuje, že se dítě dostane tam, kam by se samo nedostalo. Dává mu oporu, systém, korekci a základní kulturní i věcné rámce. To je ještě důležitější ve světě umělé inteligence: dítě nemusí vědět, co je pro jeho učení rozhodující. Učitel to ví — a jeho vedení brání tomu, aby se žák stal pouhým příjemcem povrchních informací.

Dobrý učitel proto není jen „průvodce“, ale **architekt učení, manažer třídy a lídr**, který vede děti nahoru — krok za krokem, jistě a bezpečně. Tato role je nezastupitelná v kompetenčně-znalostním modelu i v době AI.

## 4. Vzdělání musí být trvalé, hluboké a zakotvené v realitě

> „Dosáhnout, aby každý, kdo je vzděláván, byl vzdělán natrvalo…“  
> „Neboť lidé, rostou-li bez vzdělání, rostou jako plané stromy, jako trní, kopřivy a hloží…“  
> „Ve hře se dá hodně naučit, co poté bude použito, když to okolnosti budou vyžadovat.“  
> „Teorie zůstane pouhou teorií, pokud nepřikročíme k činu.“

Trvalé vzdělání nevzniká učením nazpaměť. Vzniká:

- aktivním modelováním,  
- řešením úloh,  
- procvičováním v různých kontextech,  
- používáním znalostí v hrách, projektech, simulacích, datových úlohách,  
- propojením teorie s praxí.

To je přesně logika **komplexity**: žáci musí umět kombinovat znalosti, využívat gramotnosti a aplikovat kompetence v realistických situacích, které nejsou jednoznačné. Komenský by nejspíš dnešní digitální simulace, AI nástroje, robotiku a projektovou výuku považoval za ideální nástroje „učení činem“.

## 5. Vzdělávací reforma musí být systémová a propojená

> „Má-li být však náprava úspěšná, musí být komplexní a všestranná, neboť nebude-li současně napravovat všechno, co vzájemně souvisí, nikdy se nedostanete kupředu…“  
> „Co máš udělat, do toho se dej s chutí; co sám můžeš udělat, to nečekej od jiných… Když můžeš někomu pomoci, učiň to s největší radostí.“

Komenský míří na jádro problému českého školství: reforma není možná po částech. Nestačí měnit jen hodnocení, jen obsah, jen digitální dovednosti nebo jen učebnice. Všechno se musí měnit současně, protože:

- kompetence bez znalostí jsou prázdné,  
- znalosti bez gramotností jsou nepoužitelné,  
- gramotnosti bez kompetencí jsou mechanické,  
- kompetence bez komplexity nejsou skutečnou přípravou na svět,  
- slovní hodnocení bez standardů je nečitelné,  
- AI bez kritického myšlení je hrozbou, ne pomocí.

Komenský by zřejmě řekl, že současné české školství zůstává „na půli cesty“, protože chybí jednotící rámec. A právě **kompetenčně-znalostní model**, který propojuje:

**Znalosti – Gramotnosti – Kompetence – Komplexitu,** je odpovědí na tuto potřebu.

## Co by si Komenský myslel o výuce matematiky a jazyka dnes

### Matematika

Komenský by pravděpodobně řekl:

> „Matematika je řád stvoření. Učí mysl nepodléhat zmatku.“

Pro něj byla matematika vzorem jasnosti — učí přesnosti, řádu a rozlišování, tedy základním vlastnostem rozumu. Dnes by patrně zdůraznil, že:

- matematika nemá být jen počítání výsledků, ale učení postupům, odůvodnění a pochopení;  
- dítě má vědět, **proč** je výsledek správný, ne jen **že** je;  
- výuka má směřovat k užitečným, obecným a přenositelným postupům;  
- každá úloha má vést k pochopení podstaty problému, ne jen k povrchnímu algoritmu.

> „Nic není marnějšího než vědět a učit se mnoho, totiž co nepřinese užitku.“ dnes dokonale sedí na řady mechanických příkladů bez kontextu. Komenský by pravděpodobně řekl:

- učte méně příkladů,  
- ale učte je důkladně,  
- aby každý žák rozuměl, ne jen počítal.

V dnešní terminologii by podporoval model:

**Znalosti → Gramotnosti → Kompetence → Komplexita**,  
kde matematická gramotnost (modelování, interpretace, kontrola výsledku) spojuje přesnost, praktické užití a jasný rozum.

### Jazyk

> „Jazyk je nástroj lidskosti. Kdo neumí slovo, nerozumí světu.“ 

Pro Komenského byl jazyk, zejména mateřský, základem veškerého vzdělání. Prosazoval učení jazykům od nejjednoduššího k nejsložitějšímu, skrze jasné texty, skutečné věci a praktické situace.

Dnes by pravděpodobně řekl, že:

- učení jazyka má vycházet z porozumění, ne z pouhého memorování definic;  
- dítě má číst skutečné texty a umět o nich mluvit;  
- gramatika je nástroj, ne cíl — bez ní však jazyk ztrácí strukturu;  
- výuka jazyka má vést k přesnému vyjadřování a kultivovanému myšlení.

Jeho obraz „školy jako dílny lidskosti“ by se vztahoval i ke komunikaci:

> „Škola je dílna lidskosti, kdež lidé mladí a suroví bývají ku přijetí plných pravých obrysů vzdělávání…“

V dnešní řeči:

- dítě, které nerozumí textu, neroste,  
- dítě, které neumí vyjádřit myšlenku, nemůže myslet složitě,  
- dítě, které neumí kriticky číst, je vydáno napospas manipulaci i umělé inteligenci.

Jazyk pro něj není „měkký předmět“. Je to základ všech kompetencí.

## Komenský a kompetenčně-znalostní model: přehled

| Komenského princip                     | Dnešní pojem                            |
|----------------------------------------|------------------------------------------|
| Řád, jasnost, postup                   | Znalosti a dovednosti                    |
| Užitečnost, propojenost, praktické učení | Gramotnosti                            |
| Rozum, úsudek, vedené myšlení          | Kompetence                               |
| Realistické, smysluplné úlohy          | Komplexita                               |

A dodal by:

> „Teorie zůstane pouhou teorií, pokud nepřikročíme k činu.“

Tedy: není třeba jen přepisovat RVP. Je třeba dát školám:

- jasné standardy,  
- oporu a strukturu,  
- a učitele, kteří **vedou**.

## Závěr: Komenský jako průvodce do éry AI a komplexity

Když Komenský psal o „jasné cestě života“, neměl na mysli seznam učiva, ale schopnost člověka zorientovat se v nejasném světě, jednat moudře a obstát v situacích, které nejsou předvídatelné.

Po více než 350 letech se jeho vize znovu stává naléhavou. Dnešní žák nežije v době knih, ale v době umělé inteligence, dat a neustálých změn. A přesto potřebuje totéž, co popsal Komenský:

- pevné znalosti,  
- schopnost používat je v kontextech,  
- moudré a odpovědné jednání,  
- propojené vzdělávání,  
- školu jako skutečnou „dílnu lidskosti“.

Komenský není historickým ornamentem české vzdělávací politiky. Je — zcela nečekaně — **přesným inspirátorem kurikula pro 21. století**.
""",

    "Analytický rozbor PISA 2022 v kontextu českého kurikula, kompetencí a AI gramotnosti": 
"""
# Analytický rozbor PISA 2022 v kontextu českého kurikula, kompetencí a AI gramotnosti

**Zdroj dat:** Všechna použitá data a grafy pocházejí z 8. odborného panelu IPS DATA, který se konal 20. 11. 2025. [Prezentace MŠMT](https://edu.gov.cz/shrnuti-8-odborneho-panelu-ips-data-vysledky-ceskych-zaku-v-setreni-pisa-2022-a-moznosti-rozvoje-jejich-potencialu/).

## A) Výsledky českých žáků: stabilní, ale se závažnými strukturálními problémy

### Dlouhodobý pokles a stagnace

Z grafů matematické a přírodovědné gramotnosti je patrné:

- 2003–2022: trvalý pokles o ~30 bodů (zhruba půl roku učení).
- Po roce 2012 dochází ke stagnaci na nižší úrovni, nikoliv k návratu k původním výsledkům.
- Matematika 2022: 487 bodů.
- Přírodovědná gramotnost 2022: 499 bodů.

To ukazuje, že český systém nekolabuje – ale nedokáže žáky posouvat nahoru. Málo selhává, ale málo inspiruje.

### Slabší výkon 15letých vs. 4. a 8. ročníků (TIMSS)

TIMSS pravidelně ukazuje, že:

- 4. a 8. ročníky jsou nad průměrem OECD,
- 15letí žáci (PISA) jsou pod průměrem – dochází k výraznému poklesu.

To znamená:

- problém vzniká mezi 8. a 9. ročníkem a pokračuje na středních školách,
- systém v pozdější fázi málo kultivuje znalosti, nerozvíjí gramotnosti a už vůbec ne kompetence,
- výuka je roztříštěná, obsahově přetížená, bez jasných standardů – žáci ztrácejí orientaci, motivaci i výkon.

To přesně potvrzuje náš model: Bez pevného základu (znalosti + gramotnosti) nelze rozvíjet kompetence ani komplexitu.

## B) Extrémní nerovnosti – největší slabina českého školství

### Vliv rodinného zázemí (ESCS) – grafy nerovností

Česko patří mezi 5 nejhorších zemí OECD, pokud jde o závislost výsledků na rodině.

Klíčová fakta:

- 49 % žáků ze socioekonomicky znevýhodněného prostředí nedosahuje ani úrovně 2 – základní funkční gramotnosti.
- U zvýhodněných je to jen 9 %.
- Podíl tzv. „odolných žáků“ (ti, kteří se přes znevýhodnění vypracují) je pouze 7 % – druhý nejnižší výsledek v OECD.

### Co tím grafy ukazují v našem kontextu

- české školy neumí vyrovnávat rozdíly, pouze přebírají nerovnost z rodin;
- výuka není strukturovaná, takže silné děti si pomohou samy – slabé nikoli;
- chybí standardizace znalostí a gramotností – učitelé často nevědí, „co musí umět každý žák“;
- bez jasných obsahových kritérií vzniká chaos, který nejvíce zasáhne děti bez domácí podpory.

Náš kompetenčně-znalostní model přesně řeší tento problém:  
Jasná znalostní minima + měřitelné gramotnosti + definované procesní kompetence = menší role náhody a rodiny.


## C) Kvalita vztahů žák–učitel: zásadní pro výkon, v ČR však podprůměrná

### Co ukazují grafy o sounáležitosti a vztazích

Česká republika je téměř nejhorší z OECD v kvalitě vztahů s učiteli.

- Pouze 63 % žáků uvedlo, že je učitelé respektují (OECD: 86 %).
- Jen 38 % má pocit, že by se o ně učitelé zajímali v těžké situaci.
- 49 % žáků říká, že učitele zajímá, jak se mají (OECD: 70 %+).

### Proč je to problém

PISA ukazuje jasně:

- dobré vztahy → vyšší výsledky (až +20 bodů),
- dobré vztahy → nižší matematická úzkost,
- dobré vztahy → větší motivace, sounáležitost a lepší klima.

Grafy navíc ukazují, že žáci s nejvyšší mírou sounáležitosti mají o 21 bodů lepší výsledky než žáci s nejnižší.

# Proč učitelé nepracují se vztahovou rovinou – skutečná příčina paradoxu RVP

Na první pohled by se mohlo zdát, že čeští učitelé by měli podle RVP pracovat s klimatem, sociálními dovednostmi, vztahy a motivací žáků: rámcový vzdělávací program už dvacet let zdůrazňuje klíčové kompetence, měkké dovednosti, individualizaci i podporující prostředí. Přesto mezinárodní výzkumy (včetně PISA 2022) dlouhodobě ukazují pravý opak – česká škola má jedny z nejslabších vztahů žák–učitel v OECD. Žáci uvádějí nízký pocit zájmu, nízkou podporu a nízkou sounáležitost.  

Proč? Pokud na úrovni politiky deklarujeme kompetence, proč se neprojevují v praxi?

Skutečná odpověď je jednoduchá: **RVP deklarovalo změnu, ale nevytvořilo podmínky pro její implementaci.**  
Kompetenční model je jen napsaný v dokumentu; nevstoupil do praxe. Realita škol je nastavena tak, aby rozvoj vztahů byl téměř nemožný.

## 1. Kompetence existují jen „na papíře“, nikoli ve standardech, nástrojích ani výuce  

RVP sice vyhlásilo změnu, ale:

- nevznikly standardy, co má dítě skutečně umět,
- neexistuje úroveň minimálního výkonu pro jednotlivé kompetence,
- nejsou vytvořené žádné diagnostické nástroje,
- učitelé nedostali metodiky ani podporu pro pedagogickou práci s kompetencemi,
- inspekce nikdy netlačila na procesní dovednosti, jen na formální dokumenty.

Kompetence se tak staly **abstraktním ideálem, ne didaktickým nástrojem**.  
Ve skutečnosti je česká škola dál řízena skrytým kurikulem, které je založeno na znalostech, učivu a jejich přenosu. V takovém nastavení „měkké kompetence“ a vztahy přirozeně mizí — nejsou uchopitelné, nejsou měřitelné, nejsou požadované, nejsou vyžadované.

## 2. Skryté kurikulum zůstalo encyklopedické  

RVP formálně redukovalo učivo, ale realita redukovaná není:

- učebnice zůstaly přetížené,
- přijímací zkoušky ověřují znalosti, nikoli kompetence,
- maturita je obsahová,
- většina školních testů zůstává memorovací,
- rodiče očekávají „toho hodně“,
- učitelé hodnotí hlavně reprodukci.

Tlak na výkon → tlak na tempo → tlak na obsah → **nulový čas na vztahy**.

Ve chvíli, kdy musí učitel „stihnout kapitolu“, je vztah první věc, která jde stranou.

## 3. Učitelé nemají didaktické nástroje pro práci se vztahem  

Pedagogické fakulty 15 let připravovaly učitele skoro výhradně na oborovost a teorii didaktiky, ale ne na:

- řízení třídy,
- socio-emocionální učení,
- práci s klimatem,
- budování důvěry,
- prevenci úzkosti a konfliktů,
- psychologii skupiny.

Vztahová rovina není intuice. Je to **profesní dovednost**, kterou je třeba učit – tak jako učíme matematiku nebo gramatiku. Český systém ji však nikdy systematicky neučil.  

Učitelé vztah nezanedbávají proto, že by nechtěli – ale protože **k tomu nebyli vycvičeni, vybaveni ani vedeni**.

## 4. Velké třídy a nedostatek podpůrného personálu práci s klimatem znemožňují  

Česko má jedny z největších tříd v Evropě a jeden z nejnižších podílů školních psychologů, speciálních pedagogů a asistentů. Učitelé běžně pracují:

- ve třídách o 25–32 žácích,
- s několika integrovanými žáky,
- s dětmi s úzkostmi, poruchami chování, nepozorností,
- bez podpory dalšího profesionála.

Za těchto podmínek je **vztahová práce fakticky neproveditelná** – ne proto, že by byla nedůležitá, ale proto, že je zastíněna elementární potřebou zvládnout skupinu, obsah a organizaci.

## 5. Administrativní a projektová zátěž ubírá energii i čas  

Čeští učitelé patří mezi nejzatíženější administrativou v EU. Tráví hodiny:

- vyplňováním dokumentace pro inspekci,
- papírováním kolem podpůrných opatření,
- projektovou administrativou,
- přípravou výkazů,
- vedením povinných formulářů.

Práce se vztahem vyžaduje čas a pozornost — obojí však systém učitelům bere.

## 6. V systému chybí profesní norma, že vztah je součást výkonu  

Ve Finsku, Kanadě či Nizozemsku je práce s klimatem:

- sledována inspekcí,
- součástí profesního standardu,
- explicitně popsaná ve výstupech,
- podporovaná metodicky i finančně.

V ČR není:

- popsána,
- ověřována,
- odměňována,
- hodnocena,
- systematicky trénována.

Co není profesní norma → **neexistuje v praxi**.

## Tedy: Učitelé vztah nezanedbávají — systém jim brání v tom, aby ho mohli dělat  

Formálně deklarujeme kompetenční model, inkluzi a podporující klima.  
Reálně ale provozně jedeme encyklopedický, znalostní a obsahově přetížený model z minulého století.  

Učitelé nepracují se vztahovou rovinou ne proto, že by nechtěli, ale proto, že:

- nemají standardy, nástroje ani trénink,
- nemají čas, podporu ani systém,
- jsou zahlceni obsahem, administrativou a velkými třídami,
- a jsou tlačeni k výkonům, které jdou proti vztahové práci.

Právě proto je třeba model, který staví na čtyřech úrovních:  
**Znalosti → Gramotnosti → Kompetence → Komplexita**, doplněný o jasné standardy, strukturu a AI gramotnost.

Tento model řeší přesně to, co českému školství chybí:  
**řád, strukturu, měřitelnost, obsahové ukotvení a učitele jako lídra učení.**
Náš model říká: Kompetence jsou proces – a jejich základní podmínkou je bezpečný vztah a řízené učení.  

## D) Narůstající podíl slabých žáků 

Podíl žáků „pod úrovní 2“ v matematické gramotnosti se zvýšil:

- 2003: 17 %
- 2015: 21 %
- 2022: 26 %

Každý čtvrtý žák nedosahuje funkční matematické gramotnosti. Graf navíc ukazuje silnou expanzi nejnižších úrovní 1a a pod úroveň 1.

### Co to znamená pro české školství

Systém nezajišťuje minimální znalostní a gramotnostní standard. Bez těchto základů děti:

- nedokážou odvozovat,
- neumějí řešit reálné úlohy,
- nedokážou pracovat se složitějšími texty či daty,
- nejsou schopné kriticky používat AI.

Tento trend není náhodný – odpovídá tomu, že české kurikulum má:

- vágní kompetence,
- nejasné výstupy,
- nekonzistentní hodnocení,
- přetížené učivo,
- žádné standardy minimálního výkonu.

Náš kompetenčně-znalostní model navrhuje: Znalostní minimum (jasné), gramotnostní úroveň (měřitelná), kompetence (proces), komplexita (aplikace).  

To je nástroj proti zhoršování výsledků.

## Všechny grafy potvrzují jednu věc: český systém nemá jasnou strukturu

Problémy, které se opakují napříč daty:

- stagnace výkonu,
- vysoké nerovnosti,
- slabé vztahy učitel–žák,
- růst podílu nejslabších žáků,
- nízká motivace a sebevědomí,
- propad obliby matematiky (73 % → 44 % mezi 4. a 8. ročníkem).

### Hlavní příčina

Chybějící spojení mezi:

- znalostmi,
- gramotnostmi,
- kompetencemi,
- komplexními úlohami,
- jasnými standardy.

Český systém učí hodně, ale neuspořádaně.  
Učitelé pracují poctivě, ale bez opor a jednotných rámců.  
Žáci jsou zahlceni obsahem, ne strukturou.  
AI a digitální prostředí zvýrazňuje chyby, které systém dlouhodobě přehlížel.

## Závěrečný vhled – přímé napojení na náš model

Všechny grafy – bez výjimky – ukazují, že ČR potřebuje:

1. **Znalostní minimum** – jasné, stručné, přenositelné „co má umět každý“.
2. **Gramotnostní rámec** – aplikace znalostí v textech, datech, grafech a úlohách.
3. **Procesní kompetence** – modelování, argumentace, ověřování, kontrola, plánování.
4. **Komplexitu** – úlohy, projekty, mezioborové problémy.
5. **AI gramotnost jako nový „test reality“** – žák bez základních gramotností nedokáže AI používat, pouze kopíruje její chyby.
6. **Učitele jako lídry** – učitel potřebuje strukturu, jasné cíle, jednoduché standardy, jednotné hodnocení a profesní podporu.
""",


"Hierarchie pojmů a kompetenčních úrovní": 
"""
# KAPITOLA: Hierarchie pojmů a kompetenčních úrovní ve vzdělávání a v matematice

Proces kurikulárního řízení v gymnáziu využívá dvě hierarchie pojmů, které spolu sice souvisejí, 
ale vycházejí z odlišných úrovní abstrakce. Aby byla výuka konzistentní, je nutné jasně rozlišit 
obecný vzdělávací kompetenční rámec (Schéma 1) od předmětově specifického matematického 
kompetenčního modelu používaného ve středních všeobecně vzdělávajících školách
(Schéma 2).  
**Schéma 1 – obecný vzdělávací rámec** a  
**Schéma 2 – předmětově specifický kompetenčně-znalostní model**.

Tyto modely nelze slučovat, protože pracují s pojmem *kompetence* v rozdílných kontextech. 
Schéma 1 vymezuje celkový profil absolventa gymnázia, zatímco Schéma 2 popisuje způsob 
matematického myšlení žáka a strukturu matematických dovedností.

## SCHÉMA 1: Obecná vzdělávací hierarchie
## **ZNALOSTI → GRAMOTNOSTI → KOMPETENCE → KOMPLEXITA**
*(platí pro celé ŠVP G a všechny vyučovací předměty)*

Obecné vzdělávání v gymnáziu se opírá o čtyřstupňový vývojový řetězec:

### 1. ZNALOSTI  
Základní pojmy, fakta, vztahy, pravidla a algoritmy – základní stavební prvky učení.

### 2. GRAMOTNOSTI  
Dovednosti využívat znalosti v konkrétním kontextu: matematická, jazyková, čtenářská, digitální, přírodovědná aj.
  
Do této úrovně patří nově definované gramotnosti RVP G:

- **Čtenářská gramotnost** – schopnost porozumět textům, interpretovat je a využívat k řešení problémů.  
- **Matematická gramotnost** – logické a matematické myšlení, schopnost pracovat s čísly, daty, grafy.  
- **Digitální gramotnost** – bezpečné, kritické a tvořivé využívání digitálních technologií.

Gramotnosti tvoří **spojovací vrstvu**, která propojuje znalosti s globálními / klíčovými kompetencemi.

### 3. KOMPETENCE (globální / klíčové kompetence)  
Průřezové životní dovednosti: kompetenci k učení, k řešení problémů, komunikativní, sociální a personální, občanskou, k podnikavosti, digitální. 
Jinými slovy: schopnosti jednat, řešit problémy, komunikovat, učit se a spolupracovat.

### 4. KOMPLEXITA  
Vysoká úroveň integrace: tvořivost, adaptace k novým situacím, reflexe, syntéza.

Tento model popisuje **obecné rozvíjení žáka bez ohledu na předmět** a vystihuje, kým má být žák jako absolvent gymnázia.

## Význam Schématu 1

- Jedná se o nadpředmětový rámec.  
- Klíčové kompetence nejsou matematické ani oborové – jsou obecné.  
- Gramotnosti fungují jako přechod mezi znalostmi a kompetencemi.  
- Model popisuje celkový profil absolventa, nikoli práci v konkrétním předmětu.

## SCHÉMA 2: Matematická hierarchie kompetencí 
*(předmětově specifické, využívá se pro plánování obsahu, výuky a hodnocení v matematice)*

Zatímco Schéma 1 je obecné, Schéma 2 specifikuje kompetence **uvnitř matematiky**.  
Vychází z mezinárodních standardů a opírá se o dvě hlavní vrstvy:

- **PROCESNÍ KOMPETENCE** (P - proces) – JAK žák myslí,  
- **OBSAHOVÉ DOMÉNY** (I - obsah)– S ČÍM žák pracuje.

Kombinací těchto dvou vrstev vzniká struktura 25 kompetenčních uzlů (P×I), které umožňují 
přesné plánování a diagnostiku matematických výkonů.

## Schéma 2 navazuje na vrstvy obecného modelu, ale matematicky je konkretizuje:

- **Matematické znalosti**  
- **Matematická gramotnost**  
- **Matematické procesní kompetence**  
- **Komplexita matematického myšlení**  

Teprve pod těmito vrstvami se objevují **obsahové domény RVP** a **uzly P×I**.

**Schéma 1 – obecný vzdělávací rámec** a  
**Schéma 2 – předmětově specifický kompetenční model**.

Tyto dva modely nelze zaměňovat, protože slovo *kompetence* znamená v každém z nich něco jiného.

## DETAILNÍ HIERARCHIE SCHÉMATU 2

### 1. MATEMATICKÉ ZNALOSTI  
(po úrovni „Znalosti“ ze Schématu 1)

- operace s čísly, vztahy a algoritmy  
- algebraické výrazy a rovnice  
- funkce, tabulky, grafy  
- geometrické vlastnosti a konstrukce  
- statistika a pravděpodobnost  
- definice, axiomy, vlastnosti  

### 2. MATEMATICKÁ GRAMOTNOST  
(po úrovni „Gramotnosti“ ze Schématu 1)

- aplikace znalostí v reálných situacích  
- interpretace grafů, tabulek a modelů  
- práce s daty a informacemi  
- řešení kontextových slovních úloh  
- přechod mezi reprezentacemi  

### 3. MATEMATICKÉ PROCESNÍ KOMPETENCE 
(„JAK žák pracuje“ – epistemická rovina matematiky)

- **modelovat** – převod situací do matematických modelů  
- **operovat** – výpočty, algebraické postupy, manipulace  
- **řešit problémy** – strategie, heuristiky, analýza chyb  
- **znázorňovat** – tvorba grafů, tabulek, schémat, symbolických zápisů  
- **komunikovat** – argumentace, vysvětlení postupu, přesnost  

### 4. OBSAHOVÉ DOMÉNY MATEMATIKY 
(„S ČÍM žák pracuje“ – ontologická rovina matematiky)

- čísla a měření  
- algebra a rovnice  
- funkce a jejich reprezentace  
- geometrie v rovině i prostoru  
- statistika a pravděpodobnost  

### 5. KOMPETENČNÍ UZLY (25 uzlů P×I)

Každá matematická úloha spadá do kombinace:

**procesní kompetence × obsahová doména**, například:

- modelovat × funkce → **K13**  
- operovat × algebra → **K22**  
- znázorňovat × statistika → **K45**  

Tento systém umožňuje přesné formální hodnocení jednotlivých dovedností.

## Matice procesních kompetencí × obsahových domén 

| Procesní kompetence | Čísla a měření | Algebra | Funkce | Geometrie | Statistika |
|---------------------|----------------|---------|--------|-----------|-----------|
| modelovat           | K11            | K12     | K13    | K14       | K15       |
| operovat            | K21            | K22     | K23    | K24       | K25       |
| řešit problémy      | K31            | K32     | K33    | K34       | K35       |
| znázorňovat         | K41            | K42     | K43    | K44       | K45       |
| komunikovat         | K51            | K52     | K53    | K54       | K55       |

Každý uzel reprezentuje konkrétní měřitelnou matematickou dovednost.

## Jak se Schéma 1 a Schéma 2 liší?

### Schéma 1 – všeobecné vzdělávání 
- popisuje úroveň celého profilu žáka  
- pracuje s pojmy: znalosti, gramotnosti, klíčové kompetence, komplexita  
- je nadpředmětové  
- kompetence zde znamenají *schopnosti pro život*  
→ odpovídá na otázku **„CO má žák umět obecně?“**

### Schéma 2 – matematické myšlení 
- popisuje matematické procesy, nikoli celkový profil  
- pracuje s procesními kompetencemi a obsahovými doménami  
- kompetence zde znamenají *matematické způsoby myšlení a jednání*  
→ odpovídá na otázku **„JAK má žák matematicky myslet?“**

## Proč je nutné mít dvě oddělená schémata?

- Slovo *kompetence* znamená v obou schématech něco jiného.  
  – RVP G globální cíle: životní dovednosti a postoje  
  – RVP G specifické cíle: matematické poznávací procesy  
- Každé schéma má odlišnou funkci:  
  – Schéma 1 definuje cíl gymnaziálního vzdělávání  
  – Schéma 2 definuje, jak matematika k tomuto cíli přispívá  
- Nepřekrývají se, ale doplňují.  
  – Schéma 1 je horizontální rámec  
  – Schéma 2 je vertikální oborová struktura  

## SPOJOVACÍ MATICE Schéma 1 ↔ Schéma 2

| Úroveň Schéma 1 | Matematická vrstva               | Charakter vztahu |
|-----------------|----------------------------------|------------------|
| ZNALOSTI        | Matematické znalosti             | obsah, pojmy     |
| GRAMOTNOSTI     | Matematická gramotnost           | aplikace         |
| KOMPETENCE      | Procesní kompetence (modelovat, operovat, …) | oborová konkretizace |
| KOMPLEXITA      | Kompetenční uzly P×I             | nejvyšší integrace |

## Závěr

Schéma 1 a Schéma 2 je nezbytné jasně rozlišovat, protože každé operuje na jiné úrovni 
vzdělávací struktury.

- **Schéma 1** (ZNALOSTI → GRAMOTNOSTI → KOMPETENCE → KOMPLEXITA)  
definuje univerzální vzdělávací rámec gymnázia.

- **Schéma 2** (matematické ZNALOSTI → matematická GRAMOTNOST → procesní KOMPETENCE → kompetenční uzly P×I)  
definuje strukturu matematického myšlení žáka a způsob, jak se hodnotí jeho konkrétní matematické dovednosti.
Společně tvoří **dvojrozměrnou mapu vzdělávání**, kde Schéma 1 stanovuje cíl a Schéma 2 popisuje 
konkrétní cestu v matematice.

""",

"Znalosti + kompetence":
"""
# Hierarchie dokumentů

# KAPITOLA: Česká republika schválila první RVP již v roce 2004

Česká republika schválila první RVP již v roce 2004 jako součást evropské transformace školství a první moderní kurikulární reformy po roce 1989.

## 1. Mezinárodní tlak a evropské trendy (1990–2005)

V 90. letech se vzdělávání napříč Evropou začalo posouvat od osnov (syllabus – seznam učiva) k výstupově orientovaným kurikulům (curriculum – očekávané kompetence).

Tento posun byl způsoben:

- společnou vzdělávací politikou OECD,
- prvním evropským kompetenčním rámcem (2000, 2006),
- kurikulárními reformami ve Velké Británii, Nizozemsku, Skandinávii,
- tlakem na srovnatelnost výsledků (PISA začíná 2000),
- snahou o přípravu dětí na důležitost celoživotního vzdělávání.

ČR chtěla:

- modernizovat školství,
- přejít na evropské standardy,
- podpořit decentralizaci,
- dát školám autonomii při tvorbě školního vzdělávacího programu.

Proto vzniká kurikulární reforma č. 1 (2001–2007), jejímž výsledkem je RVP.

## 2. Potřeba nahradit zastaralý model „učivo = cíle“

Do roku 2004 fungovaly v ČR tradiční osnovy, které:

- předepisovaly učivo po předmětech a ročnících (definovaly posloupnost probíraného učiva),
- definovaly očekávané znalosti,
- nepracovaly s kompetencemi,
- nerozlišovaly mezi dovednostmi, postoji, gramotnostmi.

Tento systém byl považován za:

- rigidní,
- centralizovaný,
- málo kompatibilní s EU,
- málo orientovaný na kompetence získané během studia.

RVP měl být moderní alternativou, která stanoví:

- co má žák umět (výstupy),
- ne co musí učitel probrat (osnovy).

## 3. Domácí systémová potřeba – autonomie škol

Po roce 1989 se začaly otevírat otázky:

- Může mít každá škola specifický profil?
- Je nutné, aby učitelé rigidně kopírovali centralizované osnovy?
- Jaký prostor má mít ředitel?
- Jak podporovat inovace, projekty, integraci předmětů?

RVP 2004 zavádí:

- dvě úrovně kurikula:
  - RVP (stát stanoví rámec),
  - ŠVP (škola ho naplňuje),
- počítá se s tím, že školy použijí autonomii na 30 % obsahu (vymezeno to však žádným předpisem nebylo),
- učitel není jen „realizátor osnov“, ale kurikulární designér.

Na otázku, zda byly tradiční osnovy zrušeny, musíme odpovědět: **ANO i NE** — a přesně zde vzniká český „kurikulární paradox“.

## 4. Český kurikulární paradox

Formálně zrušeny osnovy byly.  
RVP nahradil osnovy jako závazný dokument.  
Byl to posun od:

- „učivo je cíl“ → ke „kompetence jsou cíl“,
- „předepisujeme učitelům učivo a postup“ → k „stanovujeme minimální očekávané výstupy žáků“.

Osnovy přestaly existovat jako závazná norma.

Ale obsahová logika osnov přežívala dál.  

V praxi:

- některé školy přepsaly staré osnovy do ŠVP,
- učebnice zůstaly osnovové,
- státní maturity a přijímačky byly do roku 2018 téměř výhradně obsahové,
- tradice české didaktiky (hlavně matematiky a českého jazyka) byla silně propojená s osnovovými postupy.

Výsledkem byla **kurikulární polo-reforma**:

- RVP definoval výstupy,
- učitelé a školy většinou zachovávali obsahy,
- systém hodnocení byl převážně znalostní,
- formativní hodnocení se neprosadilo.

Tento nesoulad přetrvává přes 20 let.

## 5. Byla koncepce RVP 2004 správná?

Ano — v koncepci. Ne — v implementaci a provázání systému.

**ANO**, pokud hodnotíme:

- přechod na výstupově orientované pojetí,
- zavedení klíčových kompetencí,
- integraci průřezových témat,
- autonomii škol přes ŠVP.

**NE**, pokud hodnotíme:

- nedostatek metodické podpory,
- slabé návaznosti na evaluaci,
- chybějící předmětové standardy,
- tradiční kulturu výuky, která se nezměnila,
- výuku zaměřenou na „učení bez standardů“,
- výuku, která se osvobodila od obsahu a zaměřila na atraktivní aktivity mimo rámec předmětu.

Klíčový závěr:  
Český RVP 2004 byl historicky velmi odvážný krok.  
Ale:

- osnovy byly formálně zrušeny,
- systém, učitelé, učebnice a testování dál udržovali jejich logiku.

Proto reforma „zamrzla“ při zrodu.

## 6. Jaký byl přístup Rakouska, Německa a Nizozemska?

Jejich postup byl stabilnější, méně disruptivní a pedagogicky koherentní.

### Rakousko

Nezrušilo osnovy, ale reformovalo je tak, aby:

- byly kompaktní,
- popisovaly učivo i kompetence,
- měly jasnou vazbu na Bildungsstandards,
- byly testovatelné,
- byly učitelsky realistické.

### Německo

- zachovalo Kerncurricula (zemská kurikula),
- závazné kompetenční standardy KMK,
- silná evaluace (IQB, VERA).

### Nizozemsko

- rámcové kompetenční cíle (kerndoelen),
- učivo autonomně určují školy a učebnice,
- vysoká stabilita systému.

### Česká republika

- zrušila obsah bez náhrady,
- nechala školy tvořit ŠVP bez metodiky,
- učitelé neměli kompetenční nástroje,
- vznikly tisíce ŠVP, ale všechny opsané z osnov.

**Výsledek:  
V ČR chybí rovnováha mezi obsahem a kompetencemi.**

## 7. Jakou závaznost mají doporučení EU?

Doporučení Rady EU nejsou právně závazná — jde o **soft law**:

- vytváří společný jazyk,
- nastavuje očekávání,
- ovlivňuje národní reformy,
- poskytuje hodnotící rámce.

EU neříká, že se mají zrušit osnovy.  
Naopak zdůrazňuje:

- hluboké znalosti předmětů,
- současný rozvoj kompetencí.

ČR však:

- odstranila učivo,
- zavedla kompetence,
- nenastavila nástroje jejich rozvoje.

## 8. ČR se inspirovala Finskem a Švédskem

Ale jen deklarativně.

Finsko a Švédsko mají:

- profesní učitele,
- metodickou infrastrukturu,
- silnou evaluaci,
- vysokou autonomii škol.

ČR převzala:

- autonomii,
- flexibilní ŠVP,
- kompetenční rámec,

ale ne převodní mechanismy, které činí autonomii funkční.

Proto:

- autonomie = chaos,
- ŠVP = formální dokument,
- výsledky PISA stagnují.

## 9. Co z toho plyne pro český systém?

Rakousko, Německo, Nizozemsko → **vyvážený model** autonomie (15–30 %)  
Finsko, Švédsko → **vysoká autonomie** (50–70 %)  
ČR → **extrémní autonomie bez nástrojů** (2004–dnes)

Důsledky pro ČR:

- nerovnosti mezi školami,
- nerovnoměrná kvalita výuky,
- stagnace výsledků PISA,
- ŠVP jako formální dokument, nikoliv skutečné kurikulum.

EU dokumenty:

- 2006/962/ES – klíčové kompetence,
- Evropský referenční rámec 2008,
- doporučení 2018/C 189/01 (digitální kompetence).

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
st.markdown("**Autor: Jiří Bochez, 7. 12. 2025**")



























