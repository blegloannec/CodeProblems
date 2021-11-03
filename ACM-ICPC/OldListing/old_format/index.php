<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" 
   "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr">
<head>
<title>ACM</title>

<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
<meta name="author" content="Bastien LE GLOANNEC" />
<meta name="robots" content="no" />

<link rel="stylesheet" href="style.css" type="text/css" />
</head>

<body>
<div class="cadre">

<div class="titre">
ACM - Problèmes résolus
</div>

<div class="contenu">
<p>Juge en ligne : <a href="http://uva.onlinejudge.org/">http://uva.onlinejudge.org</a><br />
Forum associé : <a href="http://acm.uva.es/board/">http://acm.uva.es/board/</a><br />
Générateur de solutions : <a href="http://uvatoolkit.com">http://uvatoolkit.com</a><br />
Indications pour certains problèmes : <a href="http://www.algorithmist.com/index.php/UVa_Problemset">http://www.algorithmist.com/index.php/UVa_Problemset</a><br />
Archives du concours : <a href="http://acm.uva.es/archive/nuevoportal/">http://acm.uva.es/archive/nuevoportal/</a></p>
<p>P : page du problème<br />
C<sub><i>n</i></sub> : <i>n</i><sup>ième</sup> code solution<br />
<b><i>n</i>*</b> : code pour le problème numéro <i>n</i> <i>a priori</i> correct mais non validé, à déboguer ou optimiser selon les cas.</p>

<table>
<tr><td><b>Date</b></td><td><b>Numéro</b></td><td><b>Problème</b></td><td><b>Algorithme</b></td><td><b>Liens</b></td></tr>
<?PHP
define("PROBLEMS", "problems.txt", FALSE);
if (!file_exists(PROBLEMS)) {
   echo"Fichier des problèmes introuvable !";
}
else {
   $lines = file(PROBLEMS);
   while (list($i,$line) = each($lines)) {
   $parts = explode("||",$line);
   $d = trim($parts[0]);
   if (!empty($d)) {
   echo "<tr><td>".$d."</td><td><b>".trim($parts[1])."</b></td><td>".trim($parts[2])."</td><td>".trim($parts[3])."</td><td><a href=\"".trim($parts[4])."\">P</a> ";
   $l = sizeof($parts);
   if ($l>5) for($j=5; $j<$l; $j++) echo "<a href=\"problems/".trim($parts[$j])."\">C<sub>".($j-4)."</sub></a> ";
   echo "</td></tr>\n";
   }
}
}
?>
</table>
</div>
</div>

<div class="scadre">

<p style="text-align:right;">
<a href="http://validator.w3.org/check?uri=referer">
<img src="images/valid-xhtml11.png"
alt="Valide XHTML 1.1" height="31" width="88" /></a>
<a href="http://jigsaw.w3.org/css-validator/check?uri=referer">
<img src="images/valid-css.png"
alt="Valide CSS" height="31" width="88" /></a>
</p>

<p class="stexte">
&copy; Bastien LE GLOANNEC - 2008
</p>

</div>
</body>
</html>
