(DEFUN HELLO()
	"HELLO WORLD"
	)

(DEFUN PRINTCHILD(x par)
	(cond 
		((null x))
		((not (atom x)) (PRINTCHILD(car x) par))
		(t (write  x) (write " ") ( APPENDPAIR graph (cons par (cons x '())) ))
		)
	)
(DEFUN PRINTCHILDREN(x par)
	(cond 
		((null x) (write-line "end of children list"))
		(t (PRINTCHILD x par) (PRINTCHILDREN(cdr x) par))
		)
	)
(DEFUN PARSE (x)
	(cond 
		((null x))
		((atom (car x)) (write "node is:")  (write (car x))  (write "children are ")(PRINTCHILDREN (cdr x) (car x)) (PARSE  (cdr x)))
		((cdr x) (PARSE (cdr x)) (PARSE (car x)  ))
		((car x) (PARSE (car x)))
		)

	)
;; For the  : the plan is to collect all the nodes that are possible to reach from this node  in a format (a (b c d e f))

;; accepts ((a (b c d e f))(b (c d e f)))
(DEFUN  APPENDPAIR(l h)
	(cond
		((null l) (setq graph (cons h graph)))
		((and 
			( eq (car (car l)) (car h))
			( eq (car(cdr (car l))) (car(cdr h)))) )
		(t ( APPENDPAIR (cdr l) h) )
		)
	)

(DEFUN  MARKASVISITED(l h)
	(cond
		((null l) (setq visited (cons h visited)))
		(( eq (car l) h))
		(t ( MARKASVISITED (cdr l) h) )
		)
	)

(DEFUN  ADDTOVISIT(node)
	(append to_visit node)
	)

(DEFUN  MARKASUSED(edge)
		(setq used_edges (cons edge used_edges))		
	)

(DEFUN ONEMOREUNUSEDEDGE(l source)
	(cond 
		((null l) nil)
		((CONTAINS used_edges (car l)) ONEMOREUNUSEDEDGE (cdr l source))
		( ( eq (car (car l)) source) (car l) )
	)

)

(DEFUN BFS(current_node)
	(cond
		((null current_node))
		((null to_visit))
		((null (ONEMOREUNUSEDEDGE graph current_node) )
		  	(setq temp nil)
			(MARKASVISITED (visited current_node))
			(setq temp (car to_visit))
			(setq to_visit (cdr to_visit))
			(BFS temp)
		)
		(t 
		 	(setq edge (ONEMOREUNUSEDEDGE graph current_node))
			(MARKASUSED (edge))
			(ADDTOVISIT (to_visit) (cdr (car edge)))
			(BFS current_node)
		)
	)
)




(DEFUN CONTAINS(l h)
	(cond
		((null l) nil)
		((and 
			( eq (car (car l)) (car h))
			( eq (car(cdr (car l))) (car(cdr h)))) t)
		(t ( CONTAINS (cdr l) h) )
		)
	)

(
	DEFUN mysearch(typer star)
	(cond
		((= typer 0)(setq to_visit '()) (setq used_edges '() ) (setq visited '())(BFS star))
		)

	)


(setq graph '())

(PARSE  '(A(B(D(G))(E))(C(F))))
(write graph)
(mysearch 0 1)
(write-line "")
(write used_edges)