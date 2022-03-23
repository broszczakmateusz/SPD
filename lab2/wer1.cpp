#include <iostream>
#include <fstream>


using namespace std;

// tak jak na laboratorium
// int ALG(int N, int *R, int *P, int *Q) {
// };

void wczytaj_dane(int N, int *P, int *W, int *D) {
 string dane[11] = {"data.10", "data.12", "data.13", "data.14", "data.15", "data.16", "data.17", "data.18", "data.19", "data.20"};
    ifstream data("./data.txt");    
    string tmp;

    for (int d = 0; d < 11; d++) {

        while(tmp != dane[d]) { //wczytanie znakow przed tym co nas interesuje
            data >> tmp;
        }
        data >> N; //wczytanie liczby zadan
        for( int i = 0; i < N; i++) { //wczytanie parametrow kazdego z zadania
            data >> P[i] >> W[i] >> D[i];
        }
    }
}

int main() { 

    int size = 100;
    int N, P[size], W[size],  D[size];

    wczytaj_dane(N, P, W, D);
    cout << N;
    int roz = 2^N;
    int F[roz];
    F[0] = 0; 

    

    // //zapis do pliku
    //     ofstream zapis;
    //     zapis.open("./out.txt");
    //     // int c = ALG(N, R, P, Q, X); //uruchomienie algorytmu
    //     // totalC += c;
    //     //zapis wynikow do pliku
    //     zapis << dane[d] << endl; 
    //     // zapis << c << endl; 
    //     for( int i = 0; i < N; i++) 
    //         // zapis << X[i] + 1 << " ";
    //     zapis << endl;
    // }
    // zapis << "Total C: " << totalC << endl;
    
    return 0;
}