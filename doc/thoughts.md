# Thoughts
- Einen ausführlichen Vergleich zwischen einer Binär- und einer Fließkommakodierung  wurde von Michalewicz durchgeführt 
und zeigte, dass die Fließkommakodierung nicht nur schneller und genauer war als die entsprechende Binärdarstellung, 
sondern auch stabiler in den erreichten Lösungen 
(D.E. Goldberg. Real-coded genetic algorithms, virtual alphabets, and blocking. Technical report 90001, University of Illionis at Urbana-Champaign, September 1990, 
Z. Michalewicz. Genetic Algorithms + Data Structures = Evolution Programs. Springer, Berlin, 2. edition, 1996) 
Aus dem Buch: Gerdes, I.; Klawonn, F.; Kruse, R: Evolutionare Algorithmen. 1. Auflage Wiesbaden 2004
- Die Bestandteile des Algorithmus (Mutation, Rekombination, Fitness etc.) als Pseudocode erläutern

# Aufzug des Kapitels "Evolutionäre Algorithmen"
- Einführung: Darwin, Hase
- Temrinologie
    - popsize
    - Population
    - Generation
    - Individuum
    - Gen
    - etc.
- Kodierung
    - Binär
        - switches
        - uint
        - int
        - multiple ints
        - real numbers
    - Fließkomma
        - diskussion über Distanz 
- Fitnessfunktion
    - Darstellung der Güte als reelle Zahl
    - Minimierung / Maximierung
- Selektion
    - Umwelt- / Elternselektion
    - Soll die nächste Generation Individuen der Elterngeneration enthalten?
    - deterministisch / non-deterministisch
    - Turnier, Roulette, Plus, Komma
- Rekombination
    - 1-point- / 2-point-crossover
    - arithmetische Rekombination
    - etc.
- Mutation
    - Zufällige Modifizierung eines Individuums
    - Wieso braucht man überhaupt Mutation?
    - Mutationsrate und Mutationsdruck davon abhängig, wie nah die Kodierung des Problemes am eigentlichen Problem ist. 
    - Addition eines zufälligen Werts (normal verteilt)
    - Zufällige Änderung / Invertierung / Verschiebung von Bits
- Elitismus
    - Beibehalten des besten Individuums
    - Wird dann benötigt, wenn Eltern-Individuen nicht in die nächste Generation übernommen werden oder wenn keine deterministische Umweltselektion auf die Eltern ausgeführt wird. 
- Terminierungsbedingungen
    - Maximale Anzahl an Generationen
    - Zeit
    - Gütekriterium erfüllt
    - Keine Verbesserung in den letzten Generationen
- Populationsgröße?