select NOM from Joueurs where NUM_Joueur in (select NUM_Joueur from Pion where NUM_pion=1);
select NUM_Joueur from Pion where NUM_pion=1;
