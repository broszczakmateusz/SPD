#include <iostream>
#include <fstream>

using namespace std;

//klasa z wszytskimi parametrami zadania
class Zadanie {
    public:
    int nr;
    int R;
    int P;
    int Q;
};

//funkcja do zamiany kolejnosci zadania w tablicy
void zamien(Zadanie zad[], int a, int b){
        swap(zad[a].nr, zad[b].nr);
        swap(zad[a].R, zad[b].R);
        swap(zad[a].P, zad[b].P);
        swap(zad[a].Q, zad[b].Q);
    };

//liczenie Cmax tak jak na laboratorium
int licz_c(Zadanie zad[], int N) {
    
    int m = 0;// zjazd z maszyny
    int c = 0;// czas stygniecia

    for( int i = 0; i < N; i++) {
        m = max(zad[i].R, m) + zad[i].P;
        c = max(m + zad[i].Q, c);
    }

    return c;
};

// algorytm sortowania, najpierw dortuje po R od najmniejszego do najwiekszego,
// pozniej po kolei zamienia wszystkie zadania ze soba i sprawdza czy cmax jest mniejszy
// robi tak N(50) razy dla bo po jednym przejsciu wyznaczana jest nowa kolejnosc
int sort_zadan(Zadanie zad[], int N) {
    int kryt[N];
    for( int i = 0; i < N; i++) { 
        kryt[i] = zad[i].R;
    }

    //algorytm buuble sort
    for (int i = 0; i < N-1; i++) {
        for (int j = 0; j < N - i - 1; j++) {
            if (kryt[j] > kryt[j+1]) {
                zamien(zad, j, j+1);
                swap(kryt[j], kryt[j+1]);
            }
        }
    }
 
    // cmax dla sortR
    int c1 = licz_c(zad, N);
    int c2;

    for (int k = 0; k < N; k++) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++)	{
                zamien(zad, i, j);
                c2 = licz_c(zad, N);
                if (c2 > c1) {
                    zamien(zad, i, j);
                } else {
                    c1 = c2;
                }
            }
        }
    }

    return c1;
}

int main() {
    int size = 50;
    int N;
    Zadanie Zadania[size];
    //wczytywanie danych tak jak na laboratorium
    string dane[4] = {"data.1", "data.2", "data.3", "data.4"};
    ifstream data("./data.txt");    
    string tmp;

    //zapis do pliku
    ofstream zapis;
    zapis.open("./out.txt");

    int totalC = 0;
    for (int d = 0; d < 4; d++) {

        while(tmp != dane[d]) { //wczytanie znakow przed tym co nas interesuje
            data >> tmp;
        }
        data >> N; //wczytanie liczby zadan
        for( int i = 0; i < N; i++) { //wczytanie parametrow kazdego z zadania
            data >> Zadania[i].R >> Zadania[i].P >> Zadania[i].Q;
            Zadania[i].nr = i; //generowanie koljenosci 123...
        }

        int c = sort_zadan(Zadania, N); //uruchomienie algorytmu
        totalC += c;
        //zapis wynikow do pliku
        zapis << dane[d] << endl; //ktory zestaw danych
        zapis << "C: " << c << endl; //c dla tych danych
        for( int i = 0; i < N; i++) 
            zapis << Zadania[i].nr + 1 << " "; //kolejnosc zadan
        zapis << endl;
    }
    zapis << "Total C: " << totalC << endl; //suma c z wszystkich zadan

    zapis.close();// zamkniecie pliku
    return 0;
}