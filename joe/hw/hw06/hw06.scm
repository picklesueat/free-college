(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (sign val) (cond
          ((< val 0) -1)
          ((> val 0) 1)
          (else 0)
          )
        )

(define (square x) (* x x))

(define (pow base exp) 'YOUR-CODE-HERE)
