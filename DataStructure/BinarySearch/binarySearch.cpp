/*
 * @Author: lanyongliang
 * @Email: lanyongliang@xdf.cn
 * @Date: 2021-07-14 15:25:56
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2021-07-16 00:45:46
 * @FilePath: \AlgorithmPractice\DataStructure\BinarySearch\binarySearch.cpp
 */


#include <stdio.h>
#include <windows.h>
#include <iostream>
#include <math.h>
using namespace std;



void random(int * arr, int start, int end, int count){
    srand(2);
    for (int i=0; i<count; i++){
        arr[i] = rand() % (end - start) + start;
    }

}
int search(int searchArr[], int num, int length){

    int start = 0;
    int end = length;
    std::cout<<end<<std::endl;
    int guess = floor((start + end) / 2);

    while (start <= guess){
        if (searchArr[guess] == num){
            return guess;
        }
        else if(searchArr[guess] < num){
            start = guess + 1;
        }
        else {


            end = guess;
        }
        guess = floor((start + end) /2 );

    }
    return -1;

}


int  main()
{
    int arr[10] = {10,20,24,28,29,30,50,80,99,100};
    int index;
    // std::cout<<sizeof(arr)<<"\n"<<std::endl;
    // random(arr,10,30,10);
    // for (int i=0; i<10; i++){
    //     std::cout<<"i: " <<arr[i]<<std::endl;
    // }

    index = search(arr, 28, 10);
    std::cout<<arr<<"\n"<<index<<std::endl;
    return index;
}