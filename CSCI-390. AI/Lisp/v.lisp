
(setq graph '(
	(Bucharest (Pitesti 101)(Fagaras 211)(Giurgiu 90)(Urziceni 85))
	(Sibiu (Arad 140)(Oradea 151)(Rimnicu_Vilcea 80)(Fagaras 99))
	(Pitesti (Rimnicu_Vilcea 97)(Craiova 138)(Bucharest 101))
	(Arad (Zerind 75)(Sibiu 140)(Timisoara 118))
	(Craiova (Dobreta 120)(Rimnicu_Vilcea 146)(Pitesti 138))
	(Urziceni (Bucharest 85)(Vaslui 142)(Hirsova 98))
	(Rimnicu_Vilcea (Craiova 146)(Sibiu 80)(Pitesti 97))
	(Oradea (Zerind 71)(Sibiu 151))
	(Zerind (Oradea 71)(Arad 75))
	(Timisoara (Arad 118)(Lugoj 111))
	(Lugoj (Timisoara 111)(Mehadia 70))    
	(Mehadia (Lugoj 70)(Dobreta 75))
	(Dobreta (Mehadia 75)(Craiova 120))
	(Fagaras (Sibiu 99)(Bucharest 211))
	(Hirsova (Urziceni 98)(Eforie 86))
	(Vaslui (Urziceni 142)(Iasi 92))
	(Iasi (Vaslui 92)(Neamt 87))
	(Neamt (Iasi 87))
	(Eforie (Hirsova 86))
	(Giurgiu (Bucharest 90))
    )
)

(setq heuristic '(
(Arad 366)
(Bucharest 0)
(Craiova 160)
(Dobreta 242)
(Eforie 161)
(Fagaras 178)
(Giurgiu 77)
(Hirsova 151)
(Iasi 226)
(Lugoj 244)
(Mehadia 241)
(Neamt 234)
(Oradea 380)
(Pitesti 98)
(Rimnicu Vilcea 193)
(Sibiu 253)
(Timisoara 329)
(Urziceni 80)
(Vaslui 199)
(Zerind 374)
))

(setq random-number 2500)

(setq destination '(Bucharest))

(defun check-children (arg tree)
	(cond
	((null arg))
	((null tree))
	((eq arg (caar tree)) (setq rootTree (cdar tree)))
	(t (check-children arg (cdr tree)))))

(defun check-heuristic (arg cities)
	(cond
	((null arg))
	((null cities))
	((eq arg (caar cities)) (setq needHeuristic (cadar cities)))
	(t (check-heuristic arg (cdr cities)))))
	
(defun sum-path (arg)
	(cond
	((null arg))
	(t (setq sum-p (+ (car (cdr arg)) (check-heuristic (car arg) heuristic))))))
	
(defun select-small-one (arg)
	(cond 
	((null arg))
	((< (sum-path (car arg)) random-number) (setq random-number sum-p) (setq smallest sum-p) (setq smal-city (car arg)) (select-small-one (cdr arg)))
	(t (select-small-one (cdr arg))))
	(setq random-number 2500))
	

(defun hello-world (arg)
	(cond
		((eq arg destination))
		((eq arg nil))
		(t (check-children arg graph) (select-small-one rootTree) (print smallest) (print smal-city) (print destination)
		(hello-world (car smal-city))
		)))
	
;
