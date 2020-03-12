(defun findNode(tree node)
	(if (eq node (car tree)) (return-from findNode tree))
	(loop for x in (cdr tree)
   		do 	(progn
   				(setf result (findNode x node)) 
				(if result (return-from findNode result))  
   			)
	)
	(return-from findNode nil) 
)

;(printTreeBFS '(a (b(d(e)(f))) (c (z(r)(h)) (y)) (k)))

(defun print1(tree)
	(if (null tree)(progn 
						(format t "Tree is Empty~%")
						(return-from print1 "Tree is Empty"))
					)
	(setf queue (cons tree '()))
	(main_bfs1 queue)
)

(defun main_bfs1(nodes)
	(if (null nodes)(return-from main_bfs1))
	(format t "~a:" (car (car nodes))) 
	(if (not(null (cdr (car nodes)))) (progn 
									(setf nodes (append nodes (get_all_childs (cdr (car nodes)) 1)))
							  ))
	(terpri)
	(main_bfs1 (cdr nodes))
)

(defun main_bfs2(nodes)
	(if (null nodes)(return-from main_bfs2))
	(format t "~a:" (car (car nodes))) 
	(if (not(null (cdr (car nodes)))) (progn 
									(setf nodes (append nodes (get_all_childs (cdr (car nodes)) 2)))
							  ))
	(terpri)
	(main_bfs2 (cdr nodes))
)

(defun get_all_childs(tree type)
	(if 	
		(eq type 1)(format t "~a " (car (car tree)))
		(format t "~a " (car (car (car tree))))
	)
	(cond 
		((null (cdr tree)) (return-from get_all_childs tree))
		((return-from get_all_childs (cons (car tree) (get_all_childs (cdr tree) type))))
	)
)
                        
(defun print2(tree)
	(if (null tree)(progn 
						(format t "Tree is Empty~%")
						(return-from print2 "Tree is Empty"))
					)
	(setf wrapper (cons tree '()))
	(main_bfs2 wrapper)
)

(defun main_bfs3(nodes)
	(if (null nodes)(progn 
		(terpri)
		(return-from main_bfs3))
	)
	(format t "~a " (car (car nodes))) 
	(if (not(null (cdr (car nodes)))) (progn 
									(setf nodes (append nodes (cdr (car nodes))))
							  ))
	(main_bfs3 (cdr nodes))
)

(defun main_dfs(tree)
	(format t "~a " (car tree))
	(if (not (cdr tree)) 
		(return-from main_dfs))
	(loop for x in (cdr tree)
   		do (main_dfs x))
)

(defun sch(tree node type)
	(if (null tree)(progn 
						(format t "Tree is Empty~%")
						(return-from bfs "Tree is Empty"))
					)
	(setf subtree (findNode tree node))
	(if (not subtree) (progn 
						(format t "No Such Element~%")
						(return-from bfs "No Such Element")))


	(cond	((eq type 1) (main_dfs subtree))
			(t (main_bfs3 (cons subtree '())))
	)
)

