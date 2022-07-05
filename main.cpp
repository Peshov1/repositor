#include <iostream>

using namespace std;


class poly {

private:
    int order; // order - порядок многочлена: x^2+3x+1 , order = 2

    double* A; // A - указатель на 1 член многочлена. A+1 - указатель на 2 член многочлена. A+i - указатель на i член многочлена те при x^i
public:


    poly(){ // конструктор без параметров его вызов: poly p;
        // создаёт просто 1 потому что я так захотел можно сделать по другому
        order = 0; // у 1 порядок 0
        A = new double[1];// функция new выделяет память и создаёт указатель на неё как нам и надо. в квадрат скобках число коэф.
        A[0]=1; // A[0] - это значение на которое указывает A, можно было напсать *(A)=1; где * - разыменовывание указателя.
    }
    poly(int N){  // конструктор с параметров его вызов: poly p(N) он должен создавать x^N
        order = N;// очевидно
        A = new double[N+1]; //у нас N+1  коэф поэтому нужно столько памяти
        for (int i =0; i<=N;i++){ // здесь мы инициализируем коэффициенты многочлена а0 =0, а1 = 0 ... аN-1 = 0, aN =1
            if (i == N){
                A[i] = 1;
                break;
            }
            A[i] = 0;
        }
    }
    double& operator[](int n)const { // оператор [] возвращает ссылку на n коэфициент p[n] = an
        double & a = *(A+n); // a - ссылка на коэф
        return a;

    }
    poly operator+(const poly &p)const{ // сложение возвращает новый элемент который равен сумме
        int N;
        if (order >= p.order) N = order;
        else N = p.order; // таким образом N- наибольшая степень у двух многочленов

        poly sum(N); // конструрируем сумму
        for (int i = 0; i <=N; i++){
            *(sum.A+i) = *(A+i)+ *(p.A+i); // делаем сумму суммой
        }
        return sum;


    }
    poly  operator*(const double &d)const{
        poly multy(order);


        for (int i = 0; i <= order; i++) {
            multy.A[i] = A[i]*d;
        }
        return multy;
    }
    friend ostream &operator << (ostream &os, const poly &p){ // просто оператор вывда




        for(int i = p.order; i >=0; i--){ // бегаем по укащателям разыменовываем с помощью * и печатаем приписывая "+"

            if (i != p.order) os << " + ";

            os << *(p.A + i) << "x^"<<i;



        }
        return os;
    }



};


int main()
{

    poly a(4);
    a[2] = -5;
    cout <<"Polynominal: " <<a<<endl;
    poly p1(4), p2(3), p3;
    for (int i = 0; i<5;++i) p1[i] = 1+i;
    for (int i = 0; i<4;++i) p2[i] = 3-2*i;
    cout << "First poly = "<<p1<<endl<<endl;
    cout << "Second poly = "<<p2<<endl<<endl;
    p3 = p1 + p2;
    cout << "Addition   = "<<p3<<endl<<endl;
    cout << p3*12 + p1*7 + p2*(-5.7)<<endl;




    return 0;
}
