#!/bin/bash

# Skript zur Umbenennung der Mathematik-Dateien
# Benennt sec*.md Dateien in chapter01-12 Ordnern um zu chap##_sec##.md

echo "Starte Umbenennung der Mathematik-Dateien..."
echo "Verarbeite Ordner chapter01 bis chapter12"

# Schleife durch alle chapter## Ordner
for i in 01 02 03 04 05 06 07 08 09 10 11 12; do
    chapter_dir="chapter${i}"
    
    # Prüfe ob der Ordner existiert
    if [ -d "$chapter_dir" ]; then
        echo ""
        echo "Verarbeite Ordner: $chapter_dir"
        
        # Finde alle .md Dateien im Ordner (rekursiv)
        find "$chapter_dir" -name "*.md" -type f | while read -r file; do
            # Extrahiere den Dateinamen ohne Pfad
            filename=$(basename "$file")
            # Extrahiere das Verzeichnis
            dir=$(dirname "$file")
            
            # Prüfe ob es eine sec*.md Datei ist
            if [[ $filename =~ ^sec[0-9]+\.md$ ]]; then
                # Extrahiere die Nummer aus sec##.md
                sec_num=$(echo "$filename" | sed 's/sec\([0-9]*\)\.md/\1/')
                
                # Erstelle neuen Dateinamen: chap##_sec##.md
                new_filename="chap${i}_sec${sec_num}.md"
                new_filepath="$dir/$new_filename"
                
                # Umbenennung durchführen
                mv "$file" "$new_filepath"
                echo "  $filename -> $new_filename"
            else
                echo "  Überspringe: $filename (kein sec*.md Format)"
            fi
        done
        
    else
        echo "Warnung: Ordner $chapter_dir existiert nicht!"
    fi
done

echo ""
echo "Umbenennung abgeschlossen!"
echo ""
echo "Überprüfung der umbenannten Dateien:"
find . -name "chap*_sec*.md" -type f | sort