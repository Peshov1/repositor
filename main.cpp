#include <iostream>

using namespace std;


class poly {

private:
    int order; // order - ������� ����������: x^2+3x+1 , order = 2

    double* A; // A - ��������� �� 1 ���� ����������. A+1 - ��������� �� 2 ���� ����������. A+i - ��������� �� i ���� ���������� �� ��� x^i
public:


    poly(){ // ����������� ��� ���������� ��� �����: poly p;
        // ������ ������ 1 ������ ��� � ��� ������� ����� ������� �� �������
        order = 0; // � 1 ������� 0
        A = new double[1];// ������� new �������� ������ � ������ ��������� �� �� ��� ��� � ����. � ������� ������� ����� ����.
        A[0]=1; // A[0] - ��� �������� �� ������� ��������� A, ����� ���� ������� *(A)=1; ��� * - ��������������� ���������.
    }
    poly(int N){  // ����������� � ���������� ��� �����: poly p(N) �� ������ ��������� x^N
        order = N;// ��������
        A = new double[N+1]; //� ��� N+1  ���� ������� ����� ������� ������
        for (int i =0; i<=N;i++){ // ����� �� �������������� ������������ ���������� �0 =0, �1 = 0 ... �N-1 = 0, aN =1
            if (i == N){
                A[i] = 1;
                break;
            }
            A[i] = 0;
        }
    }
    double& operator[](int n)const { // �������� [] ���������� ������ �� n ���������� p[n] = an
        double & a = *(A+n); // a - ������ �� ����
        return a;

    }
    poly operator+(const poly &p)const{ // �������� ���������� ����� ������� ������� ����� �����
        int N;
        if (order >= p.order) N = order;
        else N = p.order; // ����� ������� N- ���������� ������� � ���� �����������

        poly sum(N); // ������������� �����
        for (int i = 0; i <=N; i++){
            *(sum.A+i) = *(A+i)+ *(p.A+i); // ������ ����� ������
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
    friend ostream &operator << (ostream &os, const poly &p){ // ������ �������� �����




        for(int i = p.order; i >=0; i--){ // ������ �� ���������� �������������� � ������� * � �������� ���������� "+"

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
