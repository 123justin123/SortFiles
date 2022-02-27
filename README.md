
# SortFiles

Sortfiles est un programme qui permet de trier tous les fichiers d'un dossier dans des sous dossiers afin de mieux s'organiser.




## Usage

```python
    python SortFiles.py
```
Choisissez le dossier que vous voulez trier et laissez le programme faire.



## Modification

Vous pouvez modifier le programme en fonction de vos besoins ! \
Pour cela ajoutez votre nouvelle catégorie dans la liste "Folder" 
ainsi que la condition dans le match.

***Exemple:***
```python
17 folder = ["Vidéo", "Gif", "Image", "Icon", "MonNouveauDossier"]

36  case ".MaNouvelleExtension":
        shutil.move(file, "MonNouveauDossier")
```

