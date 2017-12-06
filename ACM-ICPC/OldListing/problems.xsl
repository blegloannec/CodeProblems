<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
    <head>
      <title>ACM</title>
      <link rel="stylesheet" href="style.css" type="text/css" />
    </head>
    <body>
      <div class="cadre">
	<div class="titre">ACM - Probl�mes r�solus</div>
	<div class="contenu">
	  <p>Juge en ligne : <a href="http://uva.onlinejudge.org/">http://uva.onlinejudge.org</a><br />
	  Forum associ� : <a href="http://acm.uva.es/board/">http://acm.uva.es/board/</a><br />
	  G�n�rateur de solutions : <a href="http://uvatoolkit.com">http://uvatoolkit.com</a><br />
	  Indications pour certains probl�mes : <a href="http://www.algorithmist.com/index.php/UVa_Problemset">http://www.algorithmist.com/index.php/UVa_Problemset</a><br />
	  Archives du concours : <a href="http://acm.uva.es/archive/nuevoportal/">http://acm.uva.es/archive/nuevoportal/</a></p>
	  <p>P : page du probl�me<br />
	  C<sub><i>n</i></sub> : <i>n</i><sup>i�me</sup> code solution<br />
	  <b><i>n</i>*</b> : code pour le probl�me num�ro <i>n</i> <i>a priori</i> correct mais non valid�, � d�boguer ou optimiser selon les cas.</p>
	  <table>
	    <tr>
	      <th>Date</th>
	      <th>Num�ro</th>
	      <th>Probl�me</th>
	      <th>Algorithme</th>
	      <th>Liens</th>
	    </tr>
	    <xsl:for-each select="problems/problem">
	      <tr>
		<td><xsl:value-of select="date"/></td>
		<td>
		  <xsl:for-each select="ref">
		    <xsl:element name="a">
		      <xsl:attribute name="href">
			<xsl:text>codes/</xsl:text>
			<xsl:value-of select="code"/>
		      </xsl:attribute>
		      <xsl:value-of select="num"/>
		    </xsl:element>
		    <xsl:text> </xsl:text>
		  </xsl:for-each>
		</td>
		<td><xsl:value-of select="name"/></td>
		<td><xsl:value-of select="desc"/></td>
		<td>
		  <xsl:element name="a">
		    <xsl:attribute name="href">
		      <xsl:value-of select="link"/>
		    </xsl:attribute>
		    <xsl:text>P</xsl:text>
		  </xsl:element>
		</td>
	      </tr>
	    </xsl:for-each>
	  </table>
	</div>
      </div>
    </body>
  </html>
</xsl:template>

</xsl:stylesheet>
