from genericpath import exists
import music_tag
from pathlib import Path

# Liste des TAGs :
# Nom : ok
# Numero : A incrementer
# Titre : ????
# Interpretes : "DemocratieParticipative"
# Album : "DP_S05"

# repertoire de test = "C:\Users\OMEN\Music\DP_Test_Python
# repertoire de Prod = "C:\Users\OMEN\Music\DemocratieParticipative


DP_dir = Path(r'C:\Users\OMEN\Music\DemocratieParticipative') 
files = [f for f in DP_dir.iterdir() if f.is_file()]

for f in files:
    print(f.name + ' ' + f.suffix + ' ' + f.drive + ' ' + f.root + ' ' + f.stem)
    
    DP_episode = music_tag.load_file(f)
    print(DP_episode)

    # Changer le Tag !!!!
    album_item = DP_episode['album']
    
    DP_episode['artist'] = 'DemocratieParticipative'
    DP_episode['album'] = f.stem[:5]
    DP_episode['tracknumber'] = f.stem[6:8]
    DP_episode['year'] = 2015 + int(f.stem[3:5])
    DP_episode['genre'] = 'Politique'

    DP_episode.save()

    # Bouger le fichier dans le bon repertoire >>> DP_S05
    output_dir = DP_dir / ('DP_S' + f.stem[3:5])
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)

