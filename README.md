# Polyglots database

This repository is a data set of polyglot files.
It's purpose is to be used to test a polyglot file detector.

This table is an overview of the contained formats for each file:

|                    |afsk|agc|apk|bpg|elf64|gif|gitbundle|html|ild|iso|jar|jpg|js|lsmv|mbr|mp4|nes|pdf|png|ps|rb|sh|tar|tc|wv|zip|
|--------------------|----|---|---|---|-----|---|---------|----|---|---|---|---|--|----|---|---|---|---|---|--|--|--|---|--|--|---|
|PDF+ELF-1.pdf       |    |   |   |   |x    |   |         |    |   |   |   |   |  |    |   |   |   |x  |   |  |  |  |   |  |  |   |
|PDF+ELF-2.pdf       |    |   |   |   |x    |   |         |    |   |   |   |   |  |    |   |   |   |x  |   |  |  |  |   |  |  |   |
|GIF+JAR.gif         |    |   |   |   |     |x  |         |    |   |   |x  |   |  |    |   |   |   |   |   |  |  |  |   |  |  |x  |
|GIF+JS-1.gif        |    |   |   |   |     |x  |         |    |   |   |   |   |x |    |   |   |   |   |   |  |  |  |   |  |  |   |
|GIF+JS-2.gif        |    |   |   |   |     |x  |         |    |   |   |   |   |x |    |   |   |   |   |   |  |  |  |   |  |  |   |
|JPG+JAR.jpg         |    |   |   |   |     |   |         |    |   |   |x  |x  |  |    |   |   |   |   |   |  |  |  |   |  |  |x  |
|MP4+JAR.mp4         |    |   |   |   |     |   |         |    |   |   |x  |   |  |    |   |x  |   |   |   |  |  |  |   |  |  |x  |
|neszip-example.nes  |    |   |   |   |     |   |         |    |   |   |   |   |  |    |   |   |x  |   |   |  |  |  |   |  |  |x  |
|PDFGitPolyglot.pdf  |    |   |   |   |     |   |x        |    |   |   |   |   |  |    |   |   |   |x  |   |  |  |  |   |  |  |   |
|PNG+JAR.png         |    |   |   |   |     |   |         |    |   |   |x  |   |  |    |   |   |   |   |x  |  |  |  |   |  |  |x  |
|pocorgtfo01.pdf     |    |   |   |   |     |   |         |    |   |   |   |   |  |    |   |   |   |x  |   |  |  |  |   |  |  |x  |
|pocorgtfo02.pdf     |    |   |   |   |     |   |         |    |   |   |   |   |  |    |x  |   |   |x  |   |  |  |  |   |  |  |x  |
|pocorgtfo03.pdf     |x   |   |   |   |     |   |         |    |   |   |   |x  |  |    |   |   |   |x  |   |  |  |  |   |  |  |x  |
|pocorgtfo04.pdf     |    |   |   |   |     |   |         |    |   |   |   |   |  |    |   |   |   |x  |   |  |  |  |   |x |  |x  |
|pocorgtfo05.pdf     |    |   |   |   |     |   |         |    |   |x  |   |   |  |    |   |   |   |x  |   |  |  |  |   |  |  |x  |
|pocorgtfo06.pdf     |    |   |   |   |     |   |         |    |   |   |   |   |  |    |   |   |   |x  |   |  |  |  |x  |  |  |x  |
|pocorgtfo07.pdf     |    |   |   |x  |     |   |         |x   |   |   |   |   |  |    |   |   |   |x  |   |  |  |  |   |  |  |x  |
|pocorgtfo08.pdf     |    |   |   |   |     |   |         |    |   |   |   |   |  |    |   |   |   |x  |   |  |  |x |   |  |  |x  |
|pocorgtfo09.pdf     |    |   |   |   |     |   |         |    |   |   |   |   |  |    |   |   |   |x  |   |  |  |  |   |  |x |x  |
|pocorgtfo10.pdf     |    |   |   |   |     |   |         |    |   |   |   |   |  |x   |   |   |   |x  |   |  |  |  |   |  |  |x  |
|pocorgtfo11.pdf     |    |   |   |   |     |   |         |x   |   |   |   |   |  |    |   |   |   |x  |   |  |x |  |   |  |  |x  |
|pocorgtfo12.pdf     |    |   |x  |   |     |   |         |    |   |   |   |   |  |    |   |   |   |x  |   |  |  |  |   |  |  |x  |
|pocorgtfo13.pdf     |    |   |   |   |     |   |         |    |   |   |   |   |  |    |   |   |   |x  |   |x |  |  |   |  |  |x  |
|pocorgtfo14.pdf     |    |   |   |   |     |   |         |    |   |   |   |   |  |    |   |   |x  |x  |   |  |  |  |   |  |  |x  |
|pocorgtfo15.pdf     |    |   |   |   |     |   |         |    |x  |   |   |   |  |    |   |   |   |x  |   |  |  |  |   |  |  |x  |
|pocorgtfo16.pdf     |    |   |   |   |     |   |         |    |   |   |   |   |  |    |   |   |   |x  |   |  |  |x |   |  |  |x  |
|pocorgtfo17.pdf     |    |x  |   |   |     |   |         |    |   |   |   |   |  |    |   |   |   |x  |   |  |  |  |   |  |  |x  |
|resume_iso.pdf      |    |   |   |   |     |   |         |    |   |x  |   |   |  |    |   |   |   |x  |   |  |  |  |   |  |  |   |
|stegosploit_tool.png|    |   |   |   |     |   |         |x   |   |   |   |   |  |    |   |   |   |   |x  |  |  |  |   |  |  |   |

## This repository

This repository contains a [files](files) directory, which contains the polyglot files.
The CSV file [list.csv](list.csv) contains the metadatas of each file: its types, the source of the file if found elsewere, and a misc section for details, for example the known softwares which accept to read the file.

Notice that JAR files are also ZIP files.

## Acknowledgments

- The PDF files are mostly part of POC||GTFO and the work of https://github.com/corkami.
