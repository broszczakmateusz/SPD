#include <iostream>
#include <fstream>


using namespace std;

//klasa z wszytskimi parametrami zadania
class Zadanie {
    public:
    int P; // czas trwania
    int W; // waga
    int D; // oczekiwany czas zakonczena
};


// tak jak na laboratorium
int ALG(int N, Zadanie zad[]) {
    int lroz = 1 << N;
    int F[lroz];
    F[0] = 0; 

    for(int id = 1; id < lroz; id++) {
        int c = 0;
        for (int i = 0, b = 1; i < N; i++, b *= 2) {
            if (id & b) {
                c += zad[i].P;
            }
        }

        F[id] = 10000000;
        for (int k = 0, b = 1; k < N; k++, b *= 2) {            
            if (id & b) {
                F[id] = min(F[id], F[id - b] + zad[k].W * max(c - zad[k].D, 0));
            }
        }
    }
    return F[lroz-1];
}


int main() { 

    int size = 100;
    int N;
    Zadanie zad[size];

    string dane[11] = {"data.10:", "data.11:", "data.12:", "data.13:", "data.14:", "data.15:", "data.16:", "data.17:", "data.18:", "data.19:", "data.20:"};
    ifstream data("./data.txt");    
    string tmp;

    //zapis do pliku
    ofstream zapis;
    zapis.open("./out.txt");
    string wyj = "";

    for (int d = 0; d < 11; d++) {

        while(tmp != dane[d]) { //wczytanie znakow przed tym co nas interesuje
            data >> tmp;
        }
        data >> N; //wczytanie liczby zadan
        for( int i = 0; i < N; i++) { //wczytanie parametrow kazdego z zadania
            data >> zad[i].P >> zad[i].W >> zad[i].D;
        }

        string rozw = to_string(ALG(N, zad));
        //uruchomienie algorytmu i zapis wynikow do pliku
        wyj += dane[d] + " " + rozw + "\n"; 
    }
    zapis << wyj;
    return 0;
}