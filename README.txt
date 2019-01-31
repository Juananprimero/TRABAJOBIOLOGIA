Para obtener la lista de targets a partir del nombre del gen:
	Ejecutar desde el terminal el acript'targets_by_gene_name.py'.
	En el código podemos observar como hemos usado las dos listas de genes usadas en la descripción del trabajo.
	Si se quiere buscar otra combinación de targets, susituir las listas de genes.

Para obtener lista de drogas:
	Ejecutar desde el terminal el script 'non_antineoplasic_drugs.py'.
	Realiza una petición de cliente en chembl y realiza un filtrado de drogas obteniendo las que contienen el código "L01" y 		perteneciebtes a 'level5'.
	La función 'is_antenoeplasic()' es un verificador de si una droga es antineoplásica devuelviendo True en caso afirmativo.

Para obtener la lista de interacciones:
	Ejecutar desde el terminal el acript'drug_target.py'.
	Ejecutar en la misma carpeta en el que se encuentran los archivos resultantes de los dos previos script.
	Realiza una consulta a chembl y devuelve las interacciones existentes entre droga y fármaco junto a su pchembl_value.
	Se pueden modificar el valor del pchembl_value para realizar un filtrado más o menos exhaustivo.
	Devuelve un archivo con las interacciones.
	
Pintar grafo(Ejemplo):
	Ejecutar el script 'networks.R'
	Hace uso de la libraría igraph para la realización de grafos.

	
