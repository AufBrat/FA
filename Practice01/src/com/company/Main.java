package com.company;

public class Main {

    public static void main(String[] args) {
        // #1
        System.out.println("№1");
        System.out.println("Hello, World!");
        int d = 100;
        Num2(d);
        int e = 200;
        int f = e +1;
        Num3(f, e);
        int g = 300;
        int h = 400;
        Num4(g, h);
        int a = 500;
        int b = 600;
        Num5(a,b);
        int z = 789;
        Num6(z);
        int q = 123456;
        int r = 89;
        Num7(q);
        Num8(r);
        Num9(q, r);
        Num10(g, d);
        int y = 4;
        int u = 16;
        Num11(y, u);
        int n = 1;
        int m = 2;
        Num12(m, n, y, u);
    }

    static void Num2(int d) {
        // #2
        System.out.println("№2");
        System.out.println(d);
    }

    static void Num3(int f, int e) {
        // #3
        System.out.println("№3");
        System.out.println(e + 1);
        System.out.println(f);
    }

    static void Num4(int g, int h) {
        // #4 не сделал 2-ой способ // g = 300 and h = 400
        System.out.println("№4");
        System.out.println("g = " + g);
        System.out.println("h  = " + h);
        System.out.println("First way: ");
        System.out.println("g = " + (g = g+h - (h=g)));
        System.out.println("h = " + (h = g+h - (h=g)));
        System.out.println("Second way: idk");

    }

    static void Num5(int a, int b) {
        // #5
        System.out.println("№5");
        System.out.println("a = " + a);
        System.out.println("b = " + b);
        System.out.println("Hypotenuse = " + Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2)));
    }

    static void Num6(int z) {
        // #6
        System.out.println("№6");
        System.out.println("z = " + z);
        System.out.println("Last digit of the number z = " + z % 10);
    }

    static void Num7(int q) {
        // #7
        System.out.println("№7");
        System.out.println("q = " + q);
        System.out.println("The number of tens in the number = " + (q % 100)/10);
    }

    static void Num8(int r) {
        // #8
        System.out.println("№8");
        System.out.println("q = " + r);
        System.out.println("The number of tens in q = " + (r % 100)/10);
    }

    static void Num9(int q, int r) {
        // #9
        System.out.println("№9");
        System.out.println("q = "+ q);
        System.out.println("The difference between q and 21 is " + (q - 21));
        System.out.println("r = "+ r);
        System.out.println("The difference between r and 21 is " + (r -21));
    }

    static void Num10(int d, int g) {
        // #10
        System.out.println("№10");
        System.out.println("d = " + d);
        System.out.println("g = " + g);
        System.out.println("The arithmetic mean of d and g is " + ((d+g)/2));
    }

    static void Num11(int u, int y) {
        // #11
        System.out.println("№11");
        System.out.println("u = " + u);
        System.out.println("y = " + y);
        System.out.println("The geometric mean of y and u is " +  Math.sqrt(u*y));
    }

    static void Num12(int u, int y, int n, int m) {
        // #12
        System.out.println("№12");
        System.out.println("A: x1 = " + u + " and y1 = " + y);
        System.out.println("B: x2 = " + n + " and y2 = " + m);
        System.out.println("AB = " + Math.sqrt((Math.pow((n - u), 2) + Math.pow((m - y), 2))));
    }

}