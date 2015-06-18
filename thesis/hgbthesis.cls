%% hgbthesis.cls
%% Autor: Wilhelm Burger (wilhelm.burger@fh-hagenberg.at)
%% Diese Datei ist Teil des hagenberg-Package zur Erstellung von 
%% Bachelor- und Diplomarbeiten.

\NeedsTeXFormat{LaTeX2e}
\newcommand{\hgbthesisDate}{2013/05/17} %Versionsdatum
\ProvidesClass{hgbthesis}[\hgbthesisDate\space LaTeX-Vorlage fuer Diplomarbeiten, Masterarbeiten, Bachelorarbeiten etc.]

\RequirePackage{ifthen}

\newcommand{\hgb@MainLanguage}{german}	% also referenced in hgb.sty
\newcommand{\@matitelseiten}{}
\newcommand{\@datitelseiten}{}
\newcommand{\@batitelseiten}{}
\newcommand{\@prtitelseiten}{}
\newcommand{\@maketitlepages}{\@matitelseiten}  %default: Masterarbeit


%% begin class options ---------------------------------------------
\DeclareOption{master}{\renewcommand{\@maketitlepages}{\@matitelseiten}}
\DeclareOption{diplom}{\renewcommand{\@maketitlepages}{\@datitelseiten}}
\DeclareOption{bachelor}{\renewcommand{\@maketitlepages}{\@batitelseiten}}
\DeclareOption{praktikum}{\renewcommand{\@maketitlepages}{\@prtitelseiten}}
\DeclareOption{english}{\renewcommand{\hgb@MainLanguage}{english}}
\DeclareOption{german}{\renewcommand{\hgb@MainLanguage}{german}}
\DeclareOption*{\ClassWarning{hgbthesis}{Unknown document option "\CurrentOption"}}
\ProcessOptions
%% end class options ---------------------------------------------
 
\LoadClass[a4paper,12pt,oneside]{book}
 
\RequirePackage{hgb}	% load associated style file hgb.sty


%-------------- Setup für Seiten im Front-Teil --------------------

\newcommand{\@studiengang}{\@MissingArg{Studiengang??}}
\newcommand{\studiengang}[1]{%
	\renewcommand{\@studiengang}{#1}
}

\newcommand{\@studienort}{\@MissingArg{Studienort??}}
\newcommand{\studienort}[1]{%
	\renewcommand{\@studienort}{#1}
}

\newcommand{\@betreuerBez}{????}
\newcommand{\@betreuerName}{\@MissingArg{Betreuer??}}

\newcommand{\betreuer}[1]{%
  \renewcommand{\@betreuerBez}{Betreuer}
	\renewcommand{\@betreuerName}{#1}
}

\newcommand{\@betreuerfirma}{\@MissingArg{betreuerfirma??}}
\newcommand{\betreuerfirma}[1]{%
  \renewcommand{\@betreuerfirma}{#1}
}

\newcommand{\@betreueranschrift}{\@MissingArg{betreueranschrift??}}
\newcommand{\betreueranschrift}[1]{%
  \renewcommand{\@betreueranschrift}{#1}
}


\newcommand{\betreuerin}[1]{%
  \renewcommand{\@betreuerBez}{Betreuerin}
	\renewcommand{\@betreuerName}{#1}
}

\newcommand{\@nummer}{\@MissingArg{Arbeit Nummer??}}
\newcommand{\nummer}[1]{%
	\renewcommand{\@nummer}{#1}
}

\newcommand{\@seminargruppe}{\@MissingArg{Seminargruppe??}}
\newcommand{\seminargruppe}[1]{%
  \renewcommand{\@seminargruppe}{#1}
}

\newcommand{\@anschrift}{\@MissingArg{Anschrift??}}
\newcommand{\anschrift}[1]{%
  \renewcommand{\@anschrift}{#1}
}

\newcommand{\@gegenstand}{\@MissingArg{Gegenstand??}}
\newcommand{\gegenstand}[1]{%
	\renewcommand{\@gegenstand}{#1}
}

\newcommand{\@semester}{\@MissingArg{Semester??}}
\newcommand{\semester}[1]{%
	\renewcommand{\@semester}{#1}
}

%% -------------------------------------------------

\newcounter{@abgabetag}
\newcounter{@abgabemonat}
\newcounter{@abgabejahr}

\setcounter{@abgabetag}{\the\day}
\setcounter{@abgabemonat}{\the\month}
\setcounter{@abgabejahr}{\the\year}

\newcommand{\abgabedatum}[3]{%	%\abgabedatum{yyyy}{mm}{dd}
	\setcounter{@abgabejahr}{#1}
	\setcounter{@abgabemonat}{#2}
	\setcounter{@abgabetag}{#3}
}

\newcommand{\abgabemonat}[1]{%
	\ClassWarning{hgbthesis}{\noexpand\abgabemonat is deprecated - 
	use \noexpand\abgabedatum instead!}
}

\newcommand{\abgabejahr}[1]{%
	\ClassWarning{hgbthesis}{\noexpand\abgabejahr is deprecated - 
	use \noexpand\abgabedatum instead!}
}

%% ----------------------------------------------------------

\newcommand{\@firma}{\@MissingArg{Firma??}}
\newcommand{\firma}[1]{%
\renewcommand{\@firma}{#1}
}

\newcommand{\@firmenUrl}{\@MissingArg{www.???}}
\newcommand{\firmenUrl}[1]{%
\renewcommand{\@firmenUrl}{#1}
}

\newcommand{\@firmenTel}{\@MissingArg{Tel??}}
\newcommand{\firmenTel}[1]{%
\renewcommand{\@firmenTel}{#1}
}

\newcommand{\@license}{\@MissingArg{Lizenztext??}}
\newcommand{\license}[1]{%
\renewcommand{\@license}{#1}
}


%------------------ Titelseiten -------------------

\newcommand{\@batitel}{%
\begin{titlepage}%
\rule{0mm}{1mm}
%\vspace*{5mm}
\begin{center}%
  \setlength{\unitlength}{1cm}
  {\@studienort}
  \vskip 15mm
  {
  \parbox{12cm}{\centering\LARGE\bf%
  \setlength{\baselineskip}{20pt}%
  \@title}
    }
    \vskip 20mm
    {Bachelorthesis}
    \vskip 2mm
    {zur Erlangung der staatlichen Abschlussbezeichnung eines}
    \vskip 2mm
    {\sc Bachelor of Science (B. Sc.)}
    \vskip 2mm
    {in der Studienrichtung Informatik}
    \vskip 25mm%
\end{center}

    {\noindent\large Eingereicht von:\hspace{10mm}}
    {\large \@author\\\hspace*{45mm}}
    {\large \@anschrift\\\hspace*{45mm}}
    {\large \@seminargruppe\\\hspace*{45mm}}
    {\large \@nummer\\}
    \vskip 10mm
    {\noindent\large Betreuer:\hspace{25mm}}
    {\large \@betreuerName\\\hspace*{45mm}}
    {\large \@betreuerfirma\\\hspace*{45mm}}
    {\large \@betreueranschrift\\}
    \vskip 15mm
    {\large Leipzig, den \arabic{@abgabetag}.\arabic{@abgabemonat}.\arabic{@abgabejahr}}
    
  \vfil\null
\end{titlepage}%
}

%% -------------- Erklärung / Declaration ---------

\newcommand{\erklaerungsseiteDe}{%
\chapter*{Selbstständigkeitserklärung}
\noindent
Ich versichere, dass ich die vorliegende Arbeit ohne fremde Hilfe selbstständig verfasst und nur die angegebenen Quellen und Hilfsmittel benutzt habe. Wörtlich oder dem Sinn nach aus anderen Werken entnommene Stellen sind unter Angabe der Quellen kenntlich gemacht. Die Arbeit wurde bisher in gleicher oder ähnlicher Form weder veröffentlicht, noch einer anderen Prüfungsbehörde vorgelegt.
\par
\vspace{10mm}
\noindent
Leipzig, am \formatdate{\value{@abgabetag}}{\value{@abgabemonat}}{\value{@abgabejahr}}
\par
\vspace{12mm}
\noindent
\@author
}

\newcommand{\leadingzero}[1]{\ifnum #1<10 0\the#1\else\the#1\fi}

%------------ Struktur der Frontseiten -------------------


\renewcommand{\@batitelseiten}{
\@batitel
}

%------------ Automatischer Eintrag der PDF Metadaten ------------

\renewcommand{\maketitle}{	%replace standard LaTeX-command
\hypersetup{
		pdftitle={\@title},
		pdfauthor={\@author},
		pdfsubject={\@studiengang, \@studienort}
}%
\@maketitlepages
}

%%-------------------------------------------------------------

\usepackage{hgbheadings}
\usepackage{hgbbib}

%%-------------------------------------------------------------

\endinput

