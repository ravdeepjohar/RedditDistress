The files in this directory is a sample proposal template in
LaTeX, which I *require* all my students to use. No exceptions!

For each student, there are three files:
    Proposal.tex  the source LaTeX document for the proposal
    Proposal.bib  the source BibTeX document for the references
    Proposal.pdf  the final proposal

For example, Proposal.tex contains a proposal template,
Proposal.bib contains his references, and Proposal.pdf is the final
proposal. In time, I expect to have additional samples of actual proposals
placed in this directory.

You can find documentation for LaTeX and BibTeX on the web, or you
can borrow a book from the library. You can download the sources
or pre-compiled version for most platforms:
   Mac OSX:	try TeXShop
   Windows:	try MiKTeX

Under the CS department's Solaris machines, you can generate your
final proposal using the following sequence of instructions:

(1) Copy the Proposal.tex file. Edit it with your
content. Call your file Lastname.tex (change Lastname to your own
last name, of course).

(2) To generate the proposal, run the following commands:
    pdflatex Lastname
    bibtex Lastname
    pdflatex Lastname
    pdflatex Lastname

You minimally need to execute the three calls to pdflatex as shown
above and in the same order. Of course, if you have bugs, you need
to fix them. Refer to the LaTeX documentation for help.

The Mac OSX and Windows implementations are probably more user
friendly so you may want to download and use LaTeX/BiBTeX on your
own machine. But remember the sequence needed for document
generation.

- RKR
Nov 2008
