#!/usr/bin/env python3
"""
Script pour enregistrer du Twitch
Nécessite streamlink : pip install streamlink
"""

import subprocess
import sys
from datetime import datetime
import os
#Changer les configs de nom de la chaine,par la chaine que vous voulez enregistrer
def check_streamlink():
    """Vérifie si streamlink est installé"""
    try:
        subprocess.run(["streamlink", "--version"], 
                      capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def record_stream(channel="twitch", quality="best", output_dir="./recordings"):
    """
    Enregistre le stream Twitch
    
    Args:
        channel: nom de la chaîne Twitch (défaut: Twitch)
        quality: qualité du stream (best, 1080p, 720p, etc.)
        output_dir: dossier de sortie pour les enregistrements
    """
    
    # Vérifie que la dependance Python streamlink est installé, sinon faut le recuperer via pip install streamlink
    if not check_streamlink():
        print("❌ Erreur: streamlink n'est pas installé")
        print("Installez-le avec: pip install streamlink")
        sys.exit(1)
    
    # Crée le dossier de sortie s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)
    
    # Génère le nom du fichier avec la date et l'heure
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"{channel}_{timestamp}.mp4")
    
    # URL du stream Twitch
    stream_url = f"https://www.twitch.tv/{nom de la chaine}"
    
    print(f"🎥 Démarrage de l'enregistrement de {channel}")
    print(f"📁 Fichier de sortie: {output_file}")
    print(f"⚙️  Qualité: {quality}")
    print(f"🔴 Appuyez sur Ctrl+C pour arrêter l'enregistrement\n")
    
    try:
        # Commande streamlink pour enregistrer le stream
        command = [
            "streamlink",
            stream_url,
            quality,
            "-o", output_file,
            "--twitch-disable-ads"  # Désactive les pubs (si possible)
        ]
        
        subprocess.run(command)
        
        print(f"\n✅ Enregistrement terminé: {output_file}")
        
    except KeyboardInterrupt:
        print(f"\n⏹️  Enregistrement arrêté par l'utilisateur")
        print(f"📁 Fichier sauvegardé: {output_file}")
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Modification des parametres
    CHANNEL = "Twitch[nom de la chaine]"
    QUALITY = "best"  # Options: best, 1080p60, 1080p, 720p60, 720p, 480p, 360p, 160p, worst
    OUTPUT_DIR = "./recordings"
    
    print("=" * 50)
    print("  Script d'enregistrement Twitch")
    print("=" * 50 + "\n")
    
    record_stream(channel=CHANNEL, quality=QUALITY, output_dir=OUTPUT_DIR)
