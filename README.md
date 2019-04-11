# cryptography-notes

This project comprises the xml files and html output of a set of notes prepared for a course in mathematical cryptography.
The project was created using the PreTeXt typesetting language. Compiliation will require the PreTeXt files.

The main file for the project is cryptography_master.xml.

To compile the source (assuming that the pretext mathbook is in the users home directory), use the command

xsltproc -xinclude ~/mathbook/xsl/mathbook-html.xsl cryptography_master.xml

