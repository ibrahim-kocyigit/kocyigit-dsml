Tamamdır, devam ediyoruz!

---

## 2. Vektör Normları (*Vector Norms*)

Bir vektörün **norm**u (*norm*), o vektörün "uzunluğu" veya "büyüklüğü" olarak düşünülebilir. Farklı norm türleri vardır, ancak makine öğrenmesinde en sık kullanılanları **L1 normu** (*L1 norm*) ve **L2 normu**dur (*L2 norm*).

### L1 Normu (Manhattan Normu / Taksi Normu)

**L1 normu**, bir vektörün elemanlarının mutlak değerlerinin toplamıdır.

*   **Matematiksel Gösterim:**

    $\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}$ vektörünün L1 normu, $||\mathbf{v}||_1$ şeklinde gösterilir ve şöyle hesaplanır:

    $||\mathbf{v}||_1 = |v_1| + |v_2| + \dots + |v_n| = \sum_{i=1}^{n} |v_i|$

*   **Örnek:**

    $\mathbf{v} = \begin{bmatrix} 2 \\ -1 \\ 3 \end{bmatrix}$ vektörünün L1 normu:

    $||\mathbf{v}||_1 = |2| + |-1| + |3| = 2 + 1 + 3 = 6$

*   **Python Kodu:**

    ```python
    import numpy as np

    v = np.array([2, -1, 3])

    # Yöntem 1: np.linalg.norm() ile
    l1_norm1 = np.linalg.norm(v, ord=1)

    # Yöntem 2: Manuel hesaplama
    l1_norm2 = np.sum(np.abs(v))

    print("L1 Normu (np.linalg.norm()):", l1_norm1)
    print("L1 Normu (manuel):", l1_norm2)
    ```

### L2 Normu (Öklid Normu)

**L2 normu**, bir vektörün elemanlarının karelerinin toplamının kareköküdür. Bu, vektörün başlangıç noktasından (orijin) bitiş noktasına olan Öklid uzaklığıdır.

*   **Matematiksel Gösterim:**

    $\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}$ vektörünün L2 normu, $||\mathbf{v}||_2$ veya sadece $||\mathbf{v}||$ şeklinde gösterilir ve şöyle hesaplanır:

    $||\mathbf{v}||_2 = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2} = \sqrt{\sum_{i=1}^{n} v_i^2}$

*   **Örnek:**

    $\mathbf{v} = \begin{bmatrix} 2 \\ -1 \\ 3 \end{bmatrix}$ vektörünün L2 normu:

    $||\mathbf{v}||_2 = \sqrt{2^2 + (-1)^2 + 3^2} = \sqrt{4 + 1 + 9} = \sqrt{14}$

*   **Python Kodu:**

    ```python
    import numpy as np

    v = np.array([2, -1, 3])

    # Yöntem 1: np.linalg.norm() ile
    l2_norm1 = np.linalg.norm(v)  # ord=2 default olarak gelir, belirtmeye gerek yok.

    # Yöntem 2: Manuel hesaplama (nokta çarpım kullanarak)
    l2_norm2 = np.sqrt(np.dot(v, v))
    #veya
    l2_norm3 = (np.sum(v**2))**0.5
    print("L2 Normu (np.linalg.norm()):", l2_norm1)
    print("L2 Normu (manuel):", l2_norm2)
    print("L2 Normu (manuel 2):", l2_norm3)

    ```

### L1 ve L2 Normlarının Karşılaştırması ve Kullanım Alanları

*   **L1 Normu:**
    *   Daha az hesaplama gerektirir (karekök alma işlemi yoktur).
    *   **Seyrek (sparse)** çözümler üretmeye eğilimlidir (bazı elemanları sıfır olan vektörler). Bu, özellikle **özellik seçimi (feature selection)** problemlerinde faydalıdır.
    *   **Aykırı değerlere (outliers)** karşı daha dayanıklıdır.

*   **L2 Normu:**
    *   Daha yaygın olarak kullanılır.
    *   Türevlenebilirdir (L1 normu, sıfır noktasında türevlenemez). Bu, optimizasyon algoritmaları için önemlidir.
    *   Genellikle daha kararlı çözümler üretir.
    * Aykırı değerlerden L1'e göre daha çok etkilenir.

---

Bu bölümle ilgili soruların var mı? Yoksa "Kosinüs Benzerliği" konusuna geçelim.
