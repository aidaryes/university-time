(defun HELLO () "HELLO WORLD")

(defun SUMELEMENTS (arg) 
	(if (equal arg nil) 0 ( + (car arg) (SUMELEMENTS (cdr arg)))))
 
(defun AVG (numList)
	(if (equal numList nil) 0 (/ (SUMELEMENTS numList) (length numList))))

(defun PRINTINREVERSEORDER (var)
	(if (equal var nil) nil (append (PRINTINREVERSEORDER (cdr var)) (list (car var)))))
	
(defun CONTAINSMYVALUE (list symbol)
	(cond ((member symbol list) "YES, IT DOES")
		  ((print-line "NO, IT DOES NOT"))))
	
(defun ISMYLISTSORTED (list)
	(cond ((apply #'< list) "YES, IT IS")
		  ((if (equal (apply #'< list) nil) "NO, IT IS NOT"))))

#|| First task
	print car(if it is atom (at(car(list))))
		(if it is not, then recursionFunction(inside traverse))
		recursionFunction(cdr of list)
||#
		  
(defun print-tree (arg)
	(when arg
		(print (car arg))
		(print-tree (cdr arg))
		))
		
(defun firsttask (arg)
	(cond ((equal (atom(car arg)) T) (print (car arg)))
		  ((print "yes"))
		  ))
		  
		  
(defun print-children (s)
   (cond ((null (caar (cdr s))) nil) 
         (t (print (caar (cdr s))) (print-children (cdr s)))))

(defun print-tree (s)
  (cond ((null s) nil)
        ((atom (car s)) (print (car s)) (print-children s) (print-tree (cdr s)))
        (t (print-tree (car s)))))