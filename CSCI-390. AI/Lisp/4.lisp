;;; Discussed theory with TA and algorithm details
;;; Steps to do:
;;; 1. Hardcode tables with edge costs and straight line values
;;; 2. There should a variable storing path so far per each node
;;; 3. h = stored_path + edge + straightLine (heuristic value)

(setq cities '(

	    ("Bucharest"         ("Pitesti"             101    )         ("Fagaras"             211    )         ("Giurgiu"             90    )         ("Urziceni" 85    )    )
	    ("Sibiu"             ("Arad"             140    )         ("Oradea"             151    )         ("Rimnicu Vilcea"     80    )         ("Fagaras" 99    )    )
	    ("Pitesti"             ("Rimnicu Vilcea"     97    )         ("Craiova"             138    )         ("Bucharest"         101    )                            )
	    ("Arad"             ("Zerind"             75    )         ("Sibiu"            140    )         ("Timisoara"         118    )                            )
	    ("Craiova"             ("Dobreta"             120    )         ("Rimnicu Vilcea"     146    )         ("Pitesti"             138    )                            )
	    ("Urziceni"         ("Bucharest"         85    )         ("Vaslui"             142    )         ("Hirsova"             98    )                            )
	    ("Rimnicu Vilcea"     ("Craiova"             146    )         ("Sibiu"             80    )         ("Pitesti"             97    )                            )
	    ("Oradea"             ("Zerind"             71    )         ("Sibiu"             151    )                                                            )
	    ("Zerind"             ("Oradea"             71    )         ("Arad"             75    )                                                            )
	    ("Timisoara"         ("Arad"             118    )         ("Lugoj"             111    )                                                            )
	    ("Lugoj"             ("Timisoara"         111    )         ("Mehadia"             70    )                                                            )    
	    ("Mehadia"             ("Lugoj"             70    )         ("Dobreta"             75    )                                                            )
	    ("Dobreta"             ("Mehadia"             75    )         ("Craiova"             120    )                                                            )
	    ("Fagaras"             ("Sibiu"            99    )         ("Bucharest"         211    )                                                            )
	    ("Hirsova"             ("Urziceni"         98    )         ("Eforie"             86    )                                                            )
	    ("Vaslui"             ("Urziceni"         142    )         ("Iasi"             92    )                                                            )
	    ("Iasi"             ("Vaslui"             92    )         ("Neamt"             87    )                                                            )
	    ("Neamt"             ("Iasi"             87    )                                                                                            )
	    ("Eforie"             ("Hirsova"             86    )                                                                                            )
	    ("Giurgiu"             ("Bucharest"         90    )                                                                                            )
    )
)

(setq straight '(
        ("Arad"             366    )
        ("Bucharest"         0    )
        ("Craiova"             160    )
        ("Dobreta"             242    )
        ("Eforie"             161    )
        ("Fagaras"             176    )
        ("Giurgiu"             77    )
        ("Hirsova"             151    )    
        ("Iasi"             226    )
        ("Lugoj"             244    )
        ("Mehadia"             241    )
        ("Neamt"             234    )
        ("Oradea"             380    )
        ("Pitesti"             100    )
        ("Rimnicu Vilcea"     193    )
        ("Sibiu"             253    )
        ("Timisoara"         329    )
        ("Urziceni"         80    )
        ("Vaslui"             199    )
        ("Zerind"             374    )
    )
)



;l - list
;i - item
;it - list of iterated items, empty initially
(defun remove_from_list_by_name (l name it)
	(cond   
		( (null l) nil ) 
		( (string-equal (caar l) name) (append it (cdr l)) )
		(t ( remove_from_list_by_name (cdr l) name (append it (list (car l) ) ) ) )
	)
)

;strl - straight list
;return (name, straight_value) by name
(defun get_straight (name strl)
	(cond
		( (null name) nil)
		( (null strl) nil)
		( (string-equal (caar strl) name) (car strl) )
		( t ( get_straight name (cdr strl) ) )
	)
)

;city_edge - name, edge pair
;returns - (name path heuristics)
(defun calc_h (city_edge prev_path)
	(list (car city_edge) (+ prev_path (cadr city_edge) ) (apply '+ (list (cadr city_edge) prev_path (cadr ( get_straight (car city_edge) straight ) ) ) ) )
)

; (defun test_tuple_eq (test_i)
; 	(eq (car straight) test_i)
; )

;tuple_list - list of cities with edge valies
;returns h_list - list of cities with heuristics, initially empty
(defun calc_h_list (tuple_list h_list prev_path)
	(cond 
		( (null tuple_list) h_list)
		(t (calc_h_list (cdr tuple_list) (append h_list ( list (calc_h (car tuple_list) prev_path ) ) ) prev_path ) )
	)
)

;tuples_list = ( (name path h) ... )
;return min tuple
;min_val - supply any big integer to get min from list
(defun min_from_array_by_value (tuple_list min_tuple)
	(cond 
		( (null tuple_list) min_tuple )
		( (< (caddar tuple_list) (caddr min_tuple ) ) (setq min_tuple (car tuple_list) ) (min_from_array_by_value (cdr tuple_list) min_tuple ) )
		(t ( min_from_array_by_value (cdr tuple_list) min_tuple ) )
	)
)

; city_name - name of the city
; l - target list
; ctsl - cities list
(defun add_children_to_list (city_path_h ctsl)
	(cond
		( (string-equal (car city_path_h) dest )  
			;add to visited nodes
			(setq reached (append reached (list (caar ctsl) ) ) )
			reached
		)
		( (string-equal (caar ctsl) (car city_path_h) ) 
			; (print "EPTA")
			; (print children)
			; (print reached)
			; add to visited nodes
			(setq reached (append reached (list (caar ctsl) ) ) )
			;calculate heuristics and add children to the list
			(setq children (append children (calc_h_list (cdar ctsl) '() (cadr city_path_h) ) ) )
			;remove min from the list
			;and return min
			(setq min_item (min_from_array_by_value children (list "a" 900 1000) ) )
			(setq children (remove_from_list_by_name children (car min_item) '()  ) )
			(add_children_to_list min_item cities)
		)
		(t (add_children_to_list city_path_h (cdr ctsl) ) )
	)
)

(defun astar(city)
	(setq dest "Bucharest")
	;list of all non-visited children and their heuristics
	(setq children '())
	;this list represents all the nodes we've visited + the current one
	(setq reached '())
	( add_children_to_list (list city 0 0) cities)
)