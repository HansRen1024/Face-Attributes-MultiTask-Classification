echo "Creating train lmdb..."
~/caffe-multi/build/tools/convert_multilabel \
-resize_height=227 \
-resize_width=227 \
-shuffle=false \
/home/hans/data/face/CelebA/Img/img_align_celeba/ \
train.txt \
./train_db \
./train_lb \
3

echo "Creating val lmdb..."
~/caffe-multi/build/tools/convert_multilabel \
-resize_height=227 \
-resize_width=227 \
-shuffle=false \
/home/hans/data/face/CelebA/Img/img_align_celeba/ \
val.txt \
./val_db \
./val_lb \
3
