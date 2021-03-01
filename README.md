# Tugas Kecil 2 IF2211 Strategi Algoritma
# Semester II Tahun 2020/2021

## General info
Program ini bertujuan untuk menyusun rencana kuliah dengan _Topological Sort_
(Penerapan _Decrease and Conquer_)

## How the program works
1. Dari graf (DAG) yang terbentuk, hitung semua derajat-masuk (in-degree) setiap simpul, yaitu banyaknya busur yang masuk pada simpul tersebut.
2. Pilih sembarang simpul yang memiliki derajat-masuk 0.
3. Ambil simpul tersebut, dan hilangkan simpul tersebut beserta semua busur yang keluar dari simpul tersebut pada graf, dan kurangi derajat simpul yang berhubungan dengan simpul tersebut dengan 1.
4. Ulangi langkah (2) dan (3) hingga semua simpul pada DAG terpilih.

## Setup
Python 3

## How to run
1. Download Code
2. Jalankan file 'tucil2_13519125.exe' di folder bin
3. Masukkan nama file test yang mau diselesaikan

## Status
Project is: _finished_

## Contact
Dibuat oleh Habibina Arif Muzayyan (13519125)
https://www.github.com/habibinaarif
