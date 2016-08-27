# Installare il programma

# Linux/Mac
### Requisiti (clicca su di ognuno per la guida d'installazione)
- [Python 2.7.x](http://docs.python-guide.org/en/latest/starting/installation/)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [virtualenv](https://virtualenv.pypa.io/en/stable/installation/) (Recommended)

### Installazione da eseguire solo la prima volta
0. aprire la shell (Terminale) e andare su una cartella a piacimento, per esempio sul desktop: `cd ~/Desktop/`
1. Clonare il progetto con git: `git clone https://github.com/swmerko/fantacalcio-asta-helper.git`
2. Entrare nella cartella appena creata: `cd fantacalcio-asta-helper`
3. Installare il programma scrivendo nel terminale `./setup.sh`  
   questo script installerà e caricherà tutti i dati necessari a far partire il programma
4. Lanciare l'ultimo comando `./run.sh`
    Una volta fatto il setup dovrete solamente lanciare il comando di Run, senza ripetere tutta la trafila.
5. Completato il run, aprire un browser a questo indirizzo: [localhost:8000/admin](http://localhost:8000/admin)
6. Inserire nome utente e password (admin e admin)

### Per lanciare il programma dopo aver eseguito l'installazione
0. Andare nella cartella del programma (per esempio `cd ~/Desktop/fantacalcio-asta-helper/`)
1. Lanciare l'ultimo comando `./run.sh`
    Una volta fatto il setup dovrete solamente lanciare il comando di Run, senza ripetere tutta la trafila.
2. Completato il run, aprire un browser a questo indirizzo: [localhost:8000/admin](http://localhost:8000/admin)
3. Inserire nome utente e password (admin e admin)


# Windows
Non ho un computer con windows a disposizione, quindi non riesco a fare una guida. Se qualcuno avesse dimestichezza di python su windows sappia che gli aiuti sono bene accetti :)

# Anteprima
Ecco una anteprima di com'è l'interfaccia: a destra avete tutti i filtri, mentre a sinistra potete segnare come venduto (sold) il giocatore. (ricordatevi poi di cliccare salva in basso a destra)

![Anteprima schermata giocatori](https://drive.google.com/file/d/0B0xPuH3mfS-fNUJRTVhWME0ybU0/view?usp=sharing)

# Errori e problemi
Per eventuali problemi o errori per adesso aprite un issue o contattatemi a matteo.ercolani@gmail.com. Valuteremo se aprire un canale slack.

# Credits
Attenzione, i dati delle valutazioni sono stati presi da questo excel: http://www.fantamagazine.com/consigli-fantacalcio/algoritmo-evilzzx-20152016-stima-dei-prezzi-dei-giocatori-in-sede-dasta/

