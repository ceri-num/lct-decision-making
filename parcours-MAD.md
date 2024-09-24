## Parcour MAD sur MLS:

## Blabla et lien:

```html
<h3>1. Notions:</h3>
<ul>
<li><a href="https://bitbucket.org/imt-mobisyst/lecture-d2u/raw/master/pdf/11-intro-general.pdf">Introduction</a></li>
<li><a href="https://bitbucket.org/imt-mobisyst/lecture-d2u/raw/master/pdf/12-notion-policy.pdf">Notion of policy</a></li>
<li><a href="https://bitbucket.org/imt-mobisyst/lecture-d2u/raw/master/pdf/21-reinforcement.pdf">Reinforcement Learning</a></li>
<li><a href="https://bitbucket.org/imt-mobisyst/lecture-d2u/raw/master/pdf/23-model-learning.pdf">About Model Based Learning</a></li>
<li><a href="https://bitbucket.org/imt-mobisyst/lecture-d2u/raw/master/pdf/22-feedback-on-rl.pdf">Conclusiosns on 421 game</a></li>
<li><a href="https://bitbucket.org/imt-mobisyst/lecture-d2u/raw/master/pdf/31-state-space.pdf">The Curse of Dimensionality</a></li>
</ul>
<p></p>
<h3>2. Tutorials:</h3>
<p>Tutorials are based on <a href="https://bitbucket.org/imt-mobisyst/hackagames/src/master/">HackaGames</a> solution. Tutorials are proposed on the <a href="https://bitbucket.org/imt-mobisyst/hackagames/src/master/doc/toc.md">HackaGames documentation</a>.</p>
<h4>Get started with HackaGames</h4>
<ul>
<li>Process a <strong>Hello World</strong>: <strong>install</strong>, then <strong>First Bot</strong>.</li>
</ul>
<p></p>
<h4>Learn a policy</h4>
<ul>
<li><strong>Policy</strong> permits to get started with policy notion.</li>
<li><strong>Q-Learning</strong> focus on a first reinforcement learning algo.</li>
</ul>
<p></p>
<h4>Scale Up</h4>
<ul>
<li><strong>Scale-Up</strong> addresses a challenging new game (MoveIt) to try factorized approaches</li>
</ul>
<p></p>
<h3>3. Corrections:</h3>
<ul>
<li><a href="https://bitbucket.org/imt-mobisyst/lecture-d2u/raw/master/tutos/tuto_policy.zip">Tuto Policy</a></li>
<li><a href="https://bitbucket.org/imt-mobisyst/lecture-d2u/raw/master/tutos/tuto_qlearning.zip">Tuto Q-Learning</a></li>
</ul>
<h3>4. Evaluation:</h3>
<p>
L'évaluation du module repose sur un devoir sur table, en début de derniére séance et un mini-projet rendu sur deux échances.
</p>
```

## Evaluation

```html
<p>
Le travail peut être effectué seul ou en binôme, et le rendu s'effectue en deux temps.<br />
Dans un premier temps pour valider que vous avez correctement mis en place l'algorithme de <em>Q-Learning</em> sur le jeu <strong>MoveIt</strong>, et dans un second temps, pour montrer vos stratégies plus évoluées.
</p>
<p>Pour ce premier rendu, un unique fichier python (zip) est attendu et contient :</p>
<ul>
    <li>Le ou les noms des étudiants en commentaire.</li>
    <li>L'implémentation d'une class Bot apprenant sur le jeu MoveIt.</li>
<ul>
<p>
Les dévellopeurs auront pris soint de supprimer tous les print de debug dans la class Bot, pour rendre l'exécution du code le plus sobre possible.<br />
L'évaluation intègre une part non négligeable sur le respect des consignes.
</p>
```

```html
<p>
Pour se second travail: le rendu prend la forme d'une archive (zip par exemple).
Il contient:
</p>
<ul>
    <li>Un document textuel de description (groupe, présentation de l'IA mis en place, démarche, résultats intermédiaires si applicables, palier atteint) équivalent à une à deux pages, trois maximum.</li>
    <li>Un ou plusieurs sources de bot en python (<em>myTopBot.py</em> par exemple).</li>
    <li>Potentiellement des fichiers de ressources (exemple: donnée générée/chargée par l'IA...) attention le dépôt est limité à 100Mo.<li>
<ul>
<p>
Un unique rendu attendu par groupe (1 ou 2 étudiants).<br />
<p>Palier attendu:</p>
<ol>
<li>À minima, la solution présentée apprend à jouer à <em>MoveIt</em> avec une définition intéressante de l'état. Le document l'accompagnant est complet et propre.</li>
<li>La mise en oeuvre d'une technique vue en cours (clustering, arbre de décision...) permet à un bot proposé (ou un des bots) d'accélérer l'apprentissage.</li>
<li>Le bot proposée (ou un des bots) est particulièrement performant et permet d'augmenter la configuration du jeu (taille de la grille, nombre d'humains).</li>
</ol>
<p>À noter que la mise en place de la démarche est plus importante que le résultat pour peu qu'elle soit clairement présentée et servie avec un code propre.<br />
Une attention particulière est attendue sur le document accompagnant le rendu pour qu'il soit complet, pédagogique, mais concis.
</p>
```