#include <iostream>
#include <string>
using namespace std;
int main(){
	cout<<"********************\nCalculator\n********************"<<endl;
	cout<<"Enter First Number:: ";
	float num1;
	cin>>num1;
	cout<<"Enter Second Number:: ";
	float num2;
	cin>>num2;
	cout<<"Enter Operator [+,-,*,/] :: ";
	char Operator;
	cin>>Operator;
	cout<<"********************"<<endl;
    switch(Operator){
    	case '+':
    	    cout<<"Answer:: "<<num1+num2<<endl;
    	    break;
    	case '-':
    	    cout<<"Answer:: "<<num1-num2<<endl;
    	    break;
    	case '*':
    	    cout<<"Answer:: "<<num1*num2<<endl;
    	    break;
    	case '/':
    	    cout<<"Answer:: "<<num1/num2<<endl;
    	    break;
    	default:
    	    cout<<"Invalid Input"<<endl;
    }
	cout<<"********************\nMade By Omanshu\n********************"<<endl;
}
