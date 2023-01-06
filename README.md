# MATGOL (MATCOM Graph Oriented Language)

## Dominio

MATGOL es un lenguaje de dominio específico para la manipulación y graficado de grafos dirigidos y no dirigidos.

## Sintaxis del Lenguaje:

### Palabras clave

MATGOL cuenta con las siguientes palabras clave:

**graph**, **multigraph**, **pseudograph**, **digraph**, **if**, **else**, **elif**, **edge**, 
**plot**, **foredge**, **forvertex**, 
    
    
     
     
     
    
    
     
     
     
    begin, end, in, union, intersection, difference, complement, add, nodes_count, concat
    edges_count
    weight_sum
    contain_vertex
    contain_edges
    k_color_plot
    weighted_plot
    kruskal
    prim
    bfs
    dijkstra

## Arquitectura general del compilador:

El compilador puede ser dividido a nivel macro en tres fases: análisis léxico, análisis sintáctico e intérprete.
Para el análisis léxico y sintáctico se utiliza la biblioteca de pyhton PLY.

### Análisis léxico:
El análisis léxico se lleva a cabo en el archivo **lexer_rules.py**. Para este utilizamos _ply.lex_.

### Análisis sintáctico:
El análisis sintáctico se lleva a cabo en el archivo **parser_rules.py**. Para este utilizamos _ply.yacc_. Para construir el AST durante el análisis sintáctico se importan las clases (tipos de nodos del AST) del archivo **ast_nodes.py**

### Intérprete:
Este se implementa en el archivo **matgol.py**. En dicho archivo además, se lee el código a parsear, importado de la carpeta **input_codes** en formato .txt. Además para ejecutar el intérprete se utiliza una tabla de símbolos, que permite el almacenamiento y recuperación de los valores de las variables, la implementación de esta como una clase, y de sus componentes está en el archivo **symbol_table.py**. En el intérprete se itera por las instrucciones en un ámbito y estas son ejecutadas.

## Ejecución:
Para correr la aplicación se debe ejecutar el archivo matgol.py, durante la ejecución de dicho programa es pedido el nombre del fichero, que debe estar contenido en la carpeta **input_codes** con el código a compilar y ejecutar.