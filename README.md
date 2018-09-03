# Face-Attributes-MultiTask-Classification
Use Cafffe to do Face Attributes MultiTask Classification based on CelebA data sets

----
1. Put **convert_multilabel.cpp** into caffe_root/tools/
2. Remake caffe by running **make clean && make all -j8 && make py**
3. Find **list_attr_celeba.txt** in CelebA_root/Anno/
4. Run **sed -i 's/    / /g' list_attr_celeba.txt** to replease double sapce to single space.
5. Use **processlist.py** to pick up which attributes you want.
6. Then, run **sed -i 's/-1/0/g' train.txt**
7. Next use **create_lmdb.sh** to create lmdb datasets.
8. Finally, change **mcnn_Attri.prototxt** suited for your situation.
----

**中文博客地址**

https://blog.csdn.net/renhanchi/article/details/81903684

----

**Reference**

https://github.com/HolidayXue/CodeSnap

https://zhuanlan.zhihu.com/p/22190532
