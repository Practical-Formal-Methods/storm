(set-info :smt-lib-version 2.6)
(set-logic QF_BV)
(set-info :source |
Hand-crafted bit-vector benchmarks.  Some are from the SVC benchmark suite.
Contributed by Vijay Ganesh (vganesh@stanford.edu).  Translated into SMT-LIB
format by Clark Barrett using CVC3.
|)
(set-info :category "crafted")
(set-info :status unsat)
(declare-fun a () (_ BitVec 3))
(declare-fun b () (_ BitVec 3))
(declare-fun x () (_ BitVec 7))
(assert (not (and (and (or (or (or (or (or (or (or (= a (_ bv0 3)) (= a (_ bv1 3))) (= a (_ bv2 3))) (= a (_ bv3 3))) (= a (_ bv4 3))) (= a (_ bv5 3))) (= a (_ bv6 3))) (= a (_ bv7 3))) (or (or (or (or (or (or (or (= b (_ bv0 3)) (= b (_ bv1 3))) (= b (_ bv2 3))) (= b (_ bv3 3))) (= b (_ bv4 3))) (= b (_ bv5 3))) (= b (_ bv6 3))) (= b (_ bv7 3)))) (=> (= x (concat (concat (_ bv2 3) (bvadd a (concat (_ bv0 1) ((_ extract 1 0) b)))) (_ bv1 1))) (and (= ((_ extract 0 0) x) (_ bv1 1)) (= ((_ extract 5 5) x) (_ bv1 1)))))))
(check-sat)
(exit)