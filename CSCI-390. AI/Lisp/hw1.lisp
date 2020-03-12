;;First Task
(defun print-children (sec)
    (cond ((null sec) nil)
        ((atom (car sec)) (print (car sec)) (print-children (cdr sec)))
		(t (print-children (car sec)) (print-children (cdr sec)))
        ))
		 
(defun depth (arg)
    (cond ((null arg) nil)
        ((atom (car arg)) (print-children arg) (depth (cdr arg)))
        (t (depth (car arg)) (depth (cdr arg)))
		))
		
