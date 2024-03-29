(defn fib [f1 f2 count]
    (if (= 1 count)
        (print f2)
        (fib f2 (+ f1 f2) (- count 1))))
(setv num (int(input )))
(fib 0 1 num)
