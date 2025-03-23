# Bot_AMG_PY

Ce projet est un bot Discord développé en Python utilisant la bibliothèque `discord.py`. Le bot inclut des fonctionnalités de modération, de journalisation et diverses commandes pour améliorer l'expérience utilisateur sur le serveur Discord.

## Installation

1. Clonez le dépôt :
    ```bash
    git clone <URL_DU_DEPOT>
    cd Bot_AMG_PY
    ```

2. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

3. Configurez les tokens dans le fichier `secu.py` :
    ```python
    # filepath: c:\Users\trist\Documents\BOT\OLD_AMG\Bot_AMG_PY\secu.py
    TOKEN_kowzy = 'VOTRE_TOKEN_KOWZY'
    TOKEN_soydex = 'VOTRE_TOKEN_SOYDEX'
    TOKEN_test = 'VOTRE_TOKEN_TEST'
    ```

## Utilisation

Pour lancer le bot, exécutez le fichier `main.py` :
```bash
python main.py
```

## Fonctionnalités

### Modération

Le bot inclut plusieurs commandes de modération situées dans `cogs/moderation.py` :
- `kick` : Expulse un membre du serveur.
- `clear` : Supprime un nombre spécifié de messages.
- `cree_role` : Crée un nouveau rôle.
- `ajouter_role` : Ajoute un rôle à un utilisateur.
- `move_all` : Déplace tous les utilisateurs vers le salon vocal de l'auteur de la commande.
- `voc` : Affiche le nombre de personnes connectées en vocal.

### Journalisation

Les événements de journalisation sont gérés dans `cogs/logs.py` :
- `on_message_delete` : Journalise les messages supprimés.
- `on_message_edit` : Journalise les messages modifiés.
- `on_member_join` : Journalise les nouveaux membres.
- `on_member_remove` : Journalise les départs de membres.
- `on_voice_state_update` : Journalise les changements d'état vocal.
- `on_guild_role_update` : Journalise les modifications de rôles.
- `on_member_update` : Journalise les modifications de membres.
- `on_command_error` : Gère les erreurs de commandes.

### Commandes Diverses

Les commandes diverses sont situées dans `cogs/commands.py` :
- `bonjour` : Répond avec "Salut !".
- `stats` : Donne les statistiques d'un message.
- `aide` : Affiche les commandes disponibles.
- `reglement` : Affiche le règlement du serveur.
- `status` : Affiche le statut actuel d'un membre.

## Contribuer

Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.