import numpy as np  # Na potrzeby różnych obliczeń
# Liczy dystans (odległość) pomiędzy parami punktów z przekazanych kolekcji
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt  # Wykorzystane do rysowania wykresu
# tworzy koła w oparciu o krzywe Beziera zamiast wielokątów.
from matplotlib.patches import Circle
# Wyświetla dane wynikowe (koła określające pozycję cząstek)
from matplotlib.collections import PatchCollection

# Główna funkcja programu szukająca agregacji cząstek w procesie DLA.


def fraktal2D(n, r=1.0, s_len=1.0, plot=True):
    # Inicjalizowanie zerami punktów środkowych cząstek, promieni agregacji
    # Punkty środkowe
    centers = np.zeros((n, 2))  # x, y
    # Promienie agregacji
    r_max = np.zeros((n, 1))
    # Początkowa pozycja
    r_current = 2.5*r

    for i in range(1, n):
        r_realese_pos = r_current + 5.0*r  # Pozycja początkowa
        # Ruch chaotyczny w losowym kierunku - tu określamy losową wartość kąta
        theta = 2*np.pi*np.random.random()
        position_current = r_realese_pos * \
            np.array([[np.cos(theta), np.sin(
                theta)]])  # Obecna pozycja ustalana w oparciu o losowo określony kąt theta i pozycję poprzednią
        # Uaktualnienie pozycji na liście punktów środkowych
        centers[i, :] = position_current
        # Określenie odległości między punktami środkowymi (od zerowego do i-tego) a wyliczoną obecną pozycją
        space = cdist(centers[:i, ], position_current)
        # Określenie minimalnej odległości w tym kroku (pętli for)
        current_gap = np.amin(space[:i])

        # Pętla while wykonywana dopóki nie ma zderzenia
        while current_gap > (2*r):
            theta = 2*np.pi*np.random.random()  # losowy kąt theta (ruch chaotyczny)
            # kolejny krok w losowym kierunku
            step = s_len*np.array([[np.cos(theta), np.sin(theta)]])
            position_current += step  # Aktualizacja pozycji o losowy krok
            # Obliczenie odległości od aktualnej pozycji do punktów środkowych
            r_current = cdist(position_current, centers[[0, ]])
            # Jeśli bieżąca odległość r_current jest za duża, pozycja jest aktualizowana do początkowej wartości
            if r_current > 2.0*r_realese_pos:
                position_current = r_realese_pos * \
                    np.array([[np.cos(theta), np.sin(theta)]])
                continue

            # Aktualizacja zmiennych dla pierwszych i cząstek
            space = cdist(centers[:i, ], position_current)
            # Aktualizacja bieżącego minimalnego dystansu
            current_gap = np.amin(space[:i])
            # Określenie indexu (pozycji w liście) dla minimalnego dystansu
            gap_idx = np.argmin(space[:i])

            # Czy cząstki zachodzą na siebie? ( Tutaj korzystam z pracy Bragi i Ribeiro
            # aby skorygować lokalizację cząstek po dotknięciu )
            if current_gap <= (2*r):
                # W tej pracy wykorzystano proste przegrupowanie cząstek za pomocą sumowania wektorowego i algebry.
                # Najpierw rozważamy dwie cząstki, A i B w pozycjach (Xd, Yd) i (X1, Y1).
                # One mają tę konfigurację przed krokiem rozmiaru α cząstki B.
                # Po kroku cząstka B znajduje się na pozycji (X2, Y2),
                # po czym możemy wyznaczyć użyteczny zbiór wektorów.
                print('Wykryto nałożenie się obiektów: ', i)
                p2 = position_current  # bieżąca lokalizacja kroku
                angle = s_len/r*step  # kierunek wektora kroku
                p1 = p2 - angle  # lokalizacja poprzedniego kroku
                # regulacja punktu końcowego do prawidłowej lokalizacji bez nakładania się
                Asquare = np.dot((p2[0, ] - p1[0, ]),
                                 (p2[0, ] - p1[0, ]))
                Bsquare = np.dot((p2[0, ] - centers[gap_idx, ]),
                                 (p2[0, ] - centers[gap_idx, ]))
                AB = np.dot((p2[0, ] - p1[0, ]),
                            (p2[0, ] - centers[gap_idx, ]))

                # Szukamy pierwiastki, pierwiastek z najbliższą pozycją to prawidłowa zmieniona pozycja.
                alpha = np.roots([Asquare, 2*AB, (Bsquare - (2*r)**2)])

                # Dwie nowe możliwe pozycje środków, pierwiastki z 'alpha'
                probf1 = p2 + alpha[0]*angle
                probf2 = p2 + alpha[1]*angle

                # Wybrania najbliższej pozycji
                if cdist(probf1, p1) > cdist(probf2, p1):
                    nearest_pf = probf2
                else:
                    nearest_pf = probf1

                # Aktualizacja danych
                centers[i] = nearest_pf
                r_max[i] = cdist(nearest_pf, centers[[0, ]])
                r_current = np.amax(r_max)
                break

    # Wyświetla na wykresie fraktal (agregację cząstek)
    if plot:
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plots = []

        # Dodaje do listy n kół w punktach określonych w liście punktów środkowych "centers" na potrzeby
        # późniejszego wyświetlenia tych danych na wykresie
        for i in range(n):
            circle_point = Circle((centers[i]), radius=r)
            plots.append(circle_point)

        # Wyświetlanie danych na wykresie
        p = PatchCollection(plots, color='black')
        ax.add_collection(p)
        plt.axis('off')
        plt.axis('equal')
        plt.show()


# execute function
fraktal2D(70)
