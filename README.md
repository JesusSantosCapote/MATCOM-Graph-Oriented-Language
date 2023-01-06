# MATGOL (MATCOM Graph Oriented Language)

## Dominio

MATGOL es un lenguaje de dominio específico para la manipulación y graficado de grafos dirigidos y no dirigidos.

## Características Generales del Lenguaje
  
MATGOL es un lenguaje de tipado dinámico. Los tipos definidos en el lenguaje son Graph, Digraph, INT, FLOAT, BOOL. Solo se pueden asignar a variables objetos de tipo Graph o Digraph. El tipo BOOL solo se maneja en las condicionales. INT y FLOAT es el tipo de retorno de algunas funciones de MATGOL, pero no pueden ser asignados a variables. Los objetos de tipo Graph o Digraph son tratados por referencia.

## Sintaxis del Lenguaje:

### Palabras clave

MATGOL cuenta con las siguientes palabras clave:

**graph**, **digraph**, **if**, **else**, **elif**, **edge**, **plot**, **foredge**, **forvertex**,   **begin, end, in, union, intersection, difference, complement, add, nodes_count, concat, edges_count, weight_sum, contain_vertex, contain_edges, k_color_plot, weighted_plot, kruskal, prim, bfs, dijkstra**.

### Vertex Expression
Las vertex_expression tienen la siguiente sintaxis: [1 4 3 5]  
Los valores dentro de los corchetes representan vértices de un grafo. Esta expresion es utilizada para crear grafos con vértices específicos.

### Edge Expression
Las edge_expression tienen la siguiente sintaxis: (u1, v1)(u2, v2)...(un, vn). Son utilizadas para crear grafos con aristas predefinidas o para añadir aristas a un grafo.

### Funciones built-in
#### **_graph(num_vertex , edge_expression)_**
Crea un grafo no dirigido, con cantidad de vértices igual a num_vertex. Los vértices son los números 0, 1, …, num_vertex - 1. Y con las aristas especificadas en edge_expression.
Las edge_expression tienen la siguiente sintaxis: (0,1)(1,2)(2,3)
El ejemplo anterior corresponde a la edge_expression del grafo camino de 4 vértices.

#### **_graph(vertex_expression , edge_expression)_**
Sobrecarga de **graph(num_vertex, edge_expression)**. El grafo creado tiene los vertices especificados en la vertex_expression.
Las vertex_expression tienen la siguiente sintaxis: [1 2 5 8]
Si se pasa como argumento la vertex_expresion anterior a **graph** se crea un grafo no dirigido cuyos vertices son los numeros 1, 2, 5, 8.

#### **_digraph(num_vertex , edge_expression)_**
 Mismo funcionamiento que **graph(num_vertex , edge_expression)**, con la diferencia que el grafo creado es dirigido.

#### **_digraph(vertex_expression , edge_expression)_**
Mismo funcionamiento que **graph(vertex_expression , edge_expression)**, con la diferencia de que el grafo creado es dirigido.

#### **_plot(graph)_**
Muestra en pantalla el grafo **graph**.

#### **_k_color_plot(graph)_**
Intenta colorear **graph** usando la menor cantidad de colores posible, donde ningún vecino de un nodo puede tener el mismo color que el nodo mismo. Muestra el resultado en pantalla.

####  _**weighted_plot(graph)**_
Muestra en pantalla al grafo **graph** con los pesos de las aristas.

####  _**kruskal(graph)**_
Retorna el grafo árbol abarcador de costo mínimo de **graph** calculado mediante el algoritmo de Kruskal.

####  _**prim(graph)**_
Retorna el grafo árbol abarcador de costo mínimo de **graph** calculado mediante el algoritmo de Prim.

####  _**bfs(graph, source)**_
Devuelve el grafo dirigido que representa el recorrido bfs sobre **graph** empezando en **source**.

####  _**dijkstra(graph, source, target)**_
Devuelve el grafo camino del camino de costo mínimo en **graph** de **source** a **target**, calculado mediante el algoritmo de Dijkstra.

### Operaciones entre grafos

####  _**graph1  union  graph2**_
Devuelve el grafo resultante de efectuar la unión conjuntual entre los vértices y aristas de **graph1** y **graph2**.

####  _**graph1  intersection  graph2**_
Devuelve el grafo resultante de efectuar la intersección conjuntual entre los vértices y aristas de **graph1** y **graph2**.

####  _**graph1  concat  graph2**_
Devuelve un grafo **G** que tiene cantidad de vértices igual a la suma de la cantidad de vértices de **graph1** más la cantidad de vértices de **graph2**; y como aristas las aristas de **graph1** y las aristas de **graph2** renombradas para que coincidan con el nuevo número de sus vértices en el grafo  **G**. Ejemplo:

Sea **graph1** : V=[0 1 2] E=[(0,1)(1,2)] y sea **graph2**: V=[0 1] E=[(0, 1)]. Entonces **graph1** **concat** **graph2** = **G**: V=[0 1 2 3 4] E=[(0,1)(1,2)(3,4)].

####  _**graph1  difference  graph2**_
Devuelve el grafo resultante de efectuar la diferencia conjuntual entre los vértices y aristas de **graph1** y **graph2**.

####  _**complement(graph)**_
Devuelve el grafo complemento de **graph**.

### Añadir Vértices y aristas

####  _**graph add(vertex_expression)**_
Añade a **graph** los vértices especificados en **vertex_expression**.

####  _**graph add(edge_expression)**_
Añade a **graph** las aristas especificadas en **edge_expression**.

####  _**graph add(vertex_expression, edge_expression)**_
Añade a **graph** los vértices especificados en **vertex_expression** y las 
aristas especificadas en **edge_expression**.

### Propiedades de los grafos
Los grafos tienen 3 propiedades: **node_count**, **edge_count** y **weight_sum**. Se puede acceder a ellas a través de la notación punto.
####  _**graph.node_count**_
Devuelve un INT con la cantidad de vértices de **graph**.

####  _**graph.edge_count**_
Devuelve un INT con la cantidad de vértices de **graph**.

####  _**graph.weight_sum**_
Devuelve un INT o FLOAT con la suma de los pesos de las aristas de **graph**.

### Query sobre grafos

####  _**graph.contain_vertex vertex**_
Devuelve True si **graph** contiene al vértice  **vertex**

####  _**graph.contain_edges edge_expression**_
Devuelve True si **graph** contiene a todas las aristas de **edge_expression**

### Aristas Ponderadas
Por defecto todas las aristas creadas tienen un atributo peso. Si el usuario no especifica el peso de una arista se por defecto en cero.

Para especificar el peso de una arista, en las edge_expression usadas en la creacion de los grafos, añada al final el peso de la arista. Ejemplo:
**graph1 = graph(5, (0,1,40)(2, 4, 3.5))**

Esta instrucción creará un grafo no dirigido, donde los pesos de las aristas (0,1) y (2,4) son 40 y 3.5 respectivamente. 

## Arquitectura general del compilador:

El compilador puede ser dividido a nivel macro en tres fases: análisis léxico, análisis sintáctico e intérprete.
Para el análisis léxico y sintáctico se utiliza la biblioteca de pyhton PLY.

### Análisis léxico:
El análisis léxico se lleva a cabo en el archivo **lexer_rules.py**. Para este utilizamos _ply.lex_.

### Análisis sintáctico:
El análisis sintáctico se lleva a cabo en el archivo **parser_rules.py**. Para este utilizamos _ply.yacc_. Para construir el AST durante el análisis sintáctico se importan las clases (tipos de nodos del AST) del archivo **ast_nodes.py**

### Intérprete:
Este se implementa en el archivo **matgol.py**. En dicho archivo además, se lee el código a parsear, importado de la carpeta **input_codes** en formato .txt. Además para ejecutar el intérprete se utiliza una tabla de símbolos, que permite el almacenamiento y recuperación de los valores de las variables, la implementación de esta como una clase, y de sus componentes está en el archivo **symbol_table.py**. En el intérprete se itera por las instrucciones en un ámbito y estas son ejecutadas.

## Instalación:
Ejecutar el comando: `pip install -r requirements.txt`

## Ejecución:
Para correr la aplicación se debe ejecutar el archivo `matgol.py` pasandole como parámetro el fichero con el codigo que se desea compilar y ejecutar.

Ejemplo: `python matgol.py input_codes/programa1.txt`