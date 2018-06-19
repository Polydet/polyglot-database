# Polyglots database

This repository is a data set of polyglot files.
It's purpose is to be used to test a polyglot file detector.

This table is an overview of the contained formats for each file:

|                          |7z|afsk|agc|apk|bmp|bpg|docx|elf|gif|gitbundle|html|ild|iso|jar|jpg|js|lsmv|mbr|mp3|mp4|nes|odf|odt|off|ogg|pdf|png|ps|rar|rb|sh|tar|tc|tiff|wav|wv|zip|
|--------------------------|--|----|---|---|---|---|----|---|---|---------|----|---|---|---|---|--|----|---|---|---|---|---|---|---|---|---|---|--|---|--|--|---|--|----|---|--|---|
|7ZIP+JAR.7z               |x |    |   |   |   |   |    |   |   |         |    |   |   |x  |   |  |    |   |   |   |   |   |   |   |   |   |   |  |   |  |  |   |  |    |   |  |x  |
|BMP+HTML+JAR.bmp          |  |    |   |   |x  |   |    |   |   |         |x   |   |   |x  |   |  |    |   |   |   |   |   |   |   |   |   |   |  |   |  |  |   |  |    |   |  |x  |
|BMP+JAR.bmp               |  |    |   |   |x  |   |    |   |   |         |    |   |   |x  |   |  |    |   |   |   |   |   |   |   |   |   |   |  |   |  |  |   |  |    |   |  |x  |
|DOCX+ELF+JAR+PDF+RAR-1.zip|  |    |   |   |   |   |x   |x  |   |         |    |   |   |x  |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |x  |  |  |   |  |    |   |  |x  |
|DOCX+ELF+JAR+PDF+RAR-2.zip|  |    |   |   |   |   |x   |x  |   |         |    |   |   |x  |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |x  |  |  |   |  |    |   |  |x  |
|DOCX+ELF+JAR+PDF.zip      |  |    |   |   |   |   |x   |x  |   |         |    |   |   |x  |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |x  |
|DOCX+JAR+PDF.pdf          |  |    |   |   |   |   |x   |   |   |         |    |   |   |x  |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |x  |
|DOCX+JAR.docx             |  |    |   |   |   |   |x   |   |   |         |    |   |   |x  |   |  |    |   |   |   |   |   |   |   |   |   |   |  |   |  |  |   |  |    |   |  |x  |
|ELF+JAR+ODT+PDF.zip       |  |    |   |   |   |   |    |x  |   |         |    |   |   |x  |   |  |    |   |   |   |   |   |x  |   |   |x  |   |  |   |  |  |   |  |    |   |  |x  |
|ELF+RAR.rar               |  |    |   |   |   |   |    |x  |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |   |   |  |x  |  |  |   |  |    |   |  |   |
|ELF+RAR5.rar              |  |    |   |   |   |   |    |x  |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |   |   |  |x  |  |  |   |  |    |   |  |   |
|ELF+JAR+RAR.rar           |  |    |   |   |   |   |    |x  |   |         |    |   |   |x  |   |  |    |   |   |   |   |   |   |   |   |   |   |  |x  |  |  |   |  |    |   |  |x  |
|GIF+JAR+PDF.gif           |  |    |   |   |   |   |    |   |x  |         |    |   |   |x  |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |x  |
|GIF+JAR.gif               |  |    |   |   |   |   |    |   |x  |         |    |   |   |x  |   |  |    |   |   |   |   |   |   |   |   |   |   |  |   |  |  |   |  |    |   |  |x  |
|GIF+JS-1.gif              |  |    |   |   |   |   |    |   |x  |         |    |   |   |   |   |x |    |   |   |   |   |   |   |   |   |   |   |  |   |  |  |   |  |    |   |  |   |
|GIF+JS-2.gif              |  |    |   |   |   |   |    |   |x  |         |    |   |   |   |   |x |    |   |   |   |   |   |   |   |   |   |   |  |   |  |  |   |  |    |   |  |   |
|GIF+PDF.gif               |  |    |   |   |   |   |    |   |x  |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |   |
|GIF+TAR.gif               |  |    |   |   |   |   |    |   |x  |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |   |   |  |   |  |  |x  |  |    |   |  |   |
|HTML+PDF-1.html           |  |    |   |   |   |   |    |   |   |         |x   |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |   |
|HTML+PDF-2.html           |  |    |   |   |   |   |    |   |   |         |x   |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |   |
|JAR+JPG+PDF.jpg           |  |    |   |   |   |   |    |   |   |         |    |   |   |x  |x  |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |x  |
|JAR+ODT+PDF.pdf           |  |    |   |   |   |   |    |   |   |         |    |   |   |x  |   |  |    |   |   |   |   |x  |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |x  |
|JAR+TIFF.tiff             |  |    |   |   |   |   |    |   |   |         |    |   |   |x  |   |  |    |   |   |   |   |   |   |   |   |   |   |  |   |  |  |   |  |x   |   |  |x  |
|JPG+JAR.jpg               |  |    |   |   |   |   |    |   |   |         |    |   |   |x  |x  |  |    |   |   |   |   |   |   |   |   |   |   |  |   |  |  |   |  |    |   |  |x  |
|JPG+PDF.jpg               |  |    |   |   |   |   |    |   |   |         |    |   |   |   |x  |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |   |
|MP3+OGG+PNG.mp3           |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |x  |   |   |   |   |   |x  |   |x  |  |   |  |  |   |  |    |   |  |   |
|MP3+OGG+PNG+WAV.mp3       |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |x  |   |   |   |   |x  |   |   |x  |  |   |  |  |   |  |    |x  |  |   |
|MP3+PDF.pdf               |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |x  |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |   |
|MP3+PNG.mp3               |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |x  |   |   |   |   |   |   |   |x  |  |   |  |  |   |  |    |   |  |   |
|MP3+ZIP.zip               |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |x  |   |   |   |   |   |   |   |   |  |   |  |  |   |  |    |   |  |x  |
|MP4+JAR.mp4               |  |    |   |   |   |   |    |   |   |         |    |   |   |x  |   |  |    |   |   |x  |   |   |   |   |   |   |   |  |   |  |  |   |  |    |   |  |x  |
|neszip-example.nes        |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |x  |   |   |   |   |   |   |  |   |  |  |   |  |    |   |  |x  |
|ODT+JAR.odt               |  |    |   |   |   |   |    |   |   |         |    |   |   |x  |   |  |    |   |   |   |   |   |x  |   |   |   |   |  |   |  |  |   |  |    |   |  |x  |
|OGG+PDF.ogg               |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |x  |x  |   |  |   |  |  |   |  |    |   |  |   |
|OGG+ZIP.ogg               |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |x  |   |   |  |   |  |  |   |  |    |   |  |x  |
|PDF+ELF-1.pdf             |  |    |   |   |   |   |    |x  |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |   |
|PDF+ELF-2.pdf             |  |    |   |   |   |   |    |x  |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |   |
|PDF+TAR.pdf               |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |x  |  |    |   |  |   |
|PDF+WAV.pdf               |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |x  |  |   |
|PDFGitPolyglot.pdf        |  |    |   |   |   |   |    |   |   |x        |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |   |
|PNG+JAR.png               |  |    |   |   |   |   |    |   |   |         |    |   |   |x  |   |  |    |   |   |   |   |   |   |   |   |   |x  |  |   |  |  |   |  |    |   |  |x  |
|pocorgtfo01.pdf           |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |x  |
|pocorgtfo02.pdf           |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |x  |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |x  |
|pocorgtfo03.pdf           |  |x   |   |   |   |   |    |   |   |         |    |   |   |   |x  |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |x  |
|pocorgtfo04.pdf           |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |x |    |   |  |x  |
|pocorgtfo05.pdf           |  |    |   |   |   |   |    |   |   |         |    |   |x  |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |x  |
|pocorgtfo06.pdf           |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |x  |  |    |   |  |x  |
|pocorgtfo07.pdf           |  |    |   |   |   |x  |    |   |   |         |x   |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |x  |
|pocorgtfo08.pdf           |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |x |   |  |    |   |  |x  |
|pocorgtfo09.pdf           |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |x |x  |
|pocorgtfo10.pdf           |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |x   |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |x  |
|pocorgtfo11.pdf           |  |    |   |   |   |   |    |   |   |         |x   |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |x |  |   |  |    |   |  |x  |
|pocorgtfo12.pdf           |  |    |   |x  |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |x  |
|pocorgtfo13.pdf           |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |x |   |  |  |   |  |    |   |  |x  |
|pocorgtfo14.pdf           |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |x  |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |x  |
|pocorgtfo15.pdf           |  |    |   |   |   |   |    |   |   |         |    |x  |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |x  |
|pocorgtfo16.pdf           |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |x |   |  |    |   |  |x  |
|pocorgtfo17.pdf           |  |    |x  |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |x  |
|RAR+ZIP-1.rar             |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |   |   |  |x  |  |  |   |  |    |   |  |x  |
|RAR+ZIP-2.rar             |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |   |   |  |x  |  |  |   |  |    |   |  |x  |
|RAR+ZIP-3.rar             |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |   |   |  |x  |  |  |   |  |    |   |  |x  |
|RAR5+ZIP-1.rar5           |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |   |   |  |x  |  |  |   |  |    |   |  |x  |
|RAR5+ZIP-2.rar5           |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |   |   |  |x  |  |  |   |  |    |   |  |x  |
|RAR5+ZIP-3.rar5           |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |   |   |  |x  |  |  |   |  |    |   |  |x  |
|resume_iso.pdf            |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |x  |   |   |   |   |   |   |   |x  |   |  |   |  |  |   |  |    |   |  |   |
|security_logo_string.jpg  |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |x |    |   |   |   |   |   |   |   |   |   |x  |  |   |  |  |   |  |    |   |  |   |
|stegosploit_tool.png      |  |    |   |   |   |   |    |   |   |         |x   |   |   |   |   |  |    |   |   |   |   |   |   |   |   |   |x  |  |   |  |  |   |  |    |   |  |   |
|TIFF+JAR+RAR-1.tiff       |  |    |   |   |   |   |    |   |   |         |    |   |   |x  |   |  |    |   |   |   |   |   |   |   |   |   |   |  |x  |  |  |   |  |x   |   |  |x  |
|TIFF+JAR-1.tiff           |  |    |   |   |   |   |    |   |   |         |    |   |   |x  |   |  |    |   |   |   |   |   |   |   |   |   |   |  |   |  |  |   |  |x   |   |  |x  |
|TIFF+RAR+ZIP.tiff         |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |   |   |  |x  |  |  |   |  |x   |   |  |x  |
|TIFF+RAR-1.tiff           |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |   |   |  |x  |  |  |   |  |x   |   |  |   |
|TIFF+ZIP-1.tiff           |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |   |   |  |   |  |  |   |  |x   |   |  |x  |
|WAV+ZIP.zip               |  |    |   |   |   |   |    |   |   |         |    |   |   |   |   |  |    |   |   |   |   |   |   |   |   |   |   |  |   |  |  |   |  |    |x  |  |x  |

Notice that DOCX,JAR and ODT files are also ZIP files.

## This repository

This repository contains a [files](files) directory, which contains the polyglot files.

The CSV file [list.csv](list.csv) contains the metadatas of each file: its types, the source of the file if found elsewere, and a misc section for details, for example the known softwares which accept to read the file.

The CSV file [analyse.csv](analyse.csv) contains the result of the analysis of each polyglot *file* with file 5.32, TrID and our own polyglot detector. For *file*, the command is used with the flag `--keep-going`, to get all the types found.

## Acknowledgments

- The PDF files are mostly part of POC||GTFO and the work of https://github.com/corkami.
