(ns Solution (:gen-class))

(defn readarr [n] (loop [n n t []] (if (zero? n) t (recur (dec n) (conj t (read))))))

(defn -main [& args]
    (let [L (read) C (read) N (read) P (readarr N) nidx (fn [i] (mod (inc i) N))]

    (def ride (memoize (fn [i0]
        (loop [i (nidx i0) l (nth P i0)]
            (let [l1 (+ l (nth P i))]
            (if (or (= i i0) (> l1 L)) [i l] (recur (nidx i) l1)))))))

    (defn simu []
        (loop [i 0 c 0 s 0]
        (if (= c C) s
            (let [[i,l] (ride i)]
            (recur i (inc c) (+ s l))))))

    (println (simu))))
