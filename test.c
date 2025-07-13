#include <stdio.h>

// 一个简单的C语言项目：计算两个数的和

int main() {
    int a, b, sum;

    printf("请输入第一个整数: ");
    scanf("%d", &a);

    printf("请输入第二个整数: ");
    scanf("%d", &b);

    sum = a + b;

    printf("两个数的和是: %d\n", sum);

    return 0;
}